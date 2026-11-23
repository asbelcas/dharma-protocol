# How to deceive this protocol (worked example)

_Added 2026-11-22, third-party advisory blind-spot #3: teach how the protocol can be
deceived before how to display compliance. Scope: the reference instrument in `tools/`
(bondattest.py, hashchain.py, sim_econ.py) as of commit 0ff4c66, plus the charter
articles it enforces. Everything below is reproducible against the current code._

## Threat model

The deceiver is not an outsider breaking in. The deceiver is the **operator
themselves** — the A3 signer — who wants the *appearance* of A1–A5 conformance for
claims they know are false, using only the public instrument and honest-looking calls.
This is the strongest adversary the charter cares about, because all five articles
assume the signer is honest and bind everyone else.

## Worked example: a false claim that passes every format check

```python
from bondattest import certify, Attestation

lie = "Our agent verified 10,000 customer contracts with 99.9% accuracy."

# The operator hashes the LIE, consistently. Nothing in the instrument ever
# re-reads the statement, fetches the artifact, or dereferences evidence_ref.
d = {
    "claim_hash": h(lie), "statement_hash": h(lie),
    "statement_text_actual": h(lie),   # convention: the actual text's hash, matching the field above
    "artifact_hash": h("fake-report.pdf bytes"), "artifact_actual": h("fake-report.pdf bytes"),
    "producer": "acme-agents", "bond_amount": 1_000_000, "currency": "USD",
    "issued_at": time.time(), "challenge_window_s": 86400,
    "rule_ref": "charter-v0.1", "signature": "sig:acme",            # ← any "sig:" prefix passes
    "evidence_ref": "https://example.com/evidence",                  # ← never fetched
    "outcome_check": {"condition": "accuracy >= 99.9% on held-out set",
                      "verifier_ref": "https://example.com/verifier", # ← never checked, may 404
                      "deadline": time.time() + 86400},
}
ok, why = certify(ledger, d)   # → (True, "outcome-linked")  — every format check passes
```

After the challenge window elapses with no challenge *recorded in this ledger*
(which the operator controls — the ledger is an in-memory list, or a file only the
operator writes), `Attestation.status()` returns **"certified-partial"** — and only
**"certified-full"** once a further 30 days pass after the window
(`now >= t0 + W + 30*86400`) — for a claim that is entirely fabricated. The bond of
1,000,000 USD moved zero value: there is no escrow, and `bond_amount > 0` is
satisfied by any number.

## Exactly which protections are absent

| Attack | What the instrument checks | What it does NOT check (absent protection) | Charter article |
|---|---|---|---|
| Consistently-hashed false claim | `statement_hash == statement_text_actual`, `artifact_hash == artifact_actual` | That the statement/artifact are TRUE, or that `evidence_ref` resolves to anything | A1 — epistemic status enforced as a field, not as truth |
| Fake signature | `signature.startswith("sig:")` | Any cryptography: no keys, no identity binding, anyone can mint `sig:anything` | A2/A3 — signer identity is self-asserted |
| Dead verifier | `outcome_check` has condition + verifier_ref + deadline | That the verifier exists, is independent, or ever runs the check — the code comments state executing the check is "the operator's duty" | A1(c) — binding ≠ execution |
| Log control | Ledger entries are validated on the way in | Append-only-ness of the ledger itself (separate tool, see below); a challenger has no write path | A5 — completeness assumed, not enforced |
| Chain replacement | `hashchain.verify()` recomputes every link | Plain `verify()` accepts a fully-replaced self-consistent forged chain or a truncated prefix — only the 2026-11-20 anchored kwargs (`expected_tip`/`expected_len`) catch this, and the anchor must be published out-of-band by... the operator. A deceiver simply never publishes one | A5 — tamper-evidence is opt-in |
| Phantom bond | `bond_amount > 0` | That any value exists or moves; `status()` labels ("certified-partial/full") explicitly state no bond moved | A2 — the honesty scope already discloses this |
| Quoted economics | `sim_econ.run()` returns a verdict string | That the verdict's assumption (`challenge_prob` input, forfeiture-on-discovery) holds in the real market — the header says "assumption-bound, not a proof" | A1 — a model output quoted as evidence |

## The one-line summary

The instrument enforces **format discipline**: present, matching, hash-consistent,
outcome-linked fields. It does not — and v0.1 does not claim to — verify that the
content is true, the signer is real, the evidence exists, the verifier runs, the
bond is funded, or the log is the only copy. Every one of those gaps is a place a
malicious operator passes all current checks with unsupported claims.

## What closes each gap (direction, not commitment)

- A1 truth: external evidence dereference + independent re-derivation, not caller-supplied hashes alone.
- A2 bonds: actual escrow with a third party; until then the "bonded" label must stay "format-enforced only" (README honesty scope).
- A3 signers: real key material; `sig:` prefix replaced by verifiable signatures.
- A5 logs: challenger write access + operator-published anchored checkpoints per append.
- A1(c): a verifier registry or reputation, so `verifier_ref` resolves to something accountable.

Until those land, L1 conformance for this instrument means **attestation format
enforced** — explicitly not "claims verified" and not "bond market live." Displaying
it as more is itself the deception this document exists to preempt.
