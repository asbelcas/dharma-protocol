# Day 4 — Bonded Attestation Protocol v0.1 (spec draft, 2026-10-14)

Purpose: operationalize Pillar 1 (verification liability). Karma mechanism: cost re-attached
to claim. Framing refs: day-02 (disorders), day-03 (pillars), day-04-money-trail,
day-04-planetary-scale (Type-I trust layer).

## 1. Parties
- PRODUCER: issues a claim C (proof, output, assertion) and posts bond B(C).
- CHALLENGER: disputes C within window W; posts counter-bond to prevent spam challenges.
- ADJUDICATOR: resolves disputes (see §4).
- CONSUMERS: anyone relying on C; payout beneficiaries when C fails.

## 2. Bond mechanics
- Attestation record (implemented schema, Day-12 rev): {claim_hash, statement_hash,
  artifact_hash, producer, bond_amount, currency, issued_at, challenge_window_s,
  rule_ref, signature, evidence_ref} — the Day-5 prototype's field names differ from
  this spec's original sketch (statement_text_hash→statement_hash + artifact binding;
  block/height and absolute challenge_deadline deferred to ledger integration);
  statement-match rule unchanged. `evidence_ref` is the A2 evidence pointer, now an
  enforced field.
- Amount heuristic: bond >= expected_cost_of_verification * 2 (a claim must be able to pay
  for its own checking). AI-scale claims (proofs at $15M burn) imply LARGE bonds — this is
  the point: unbondable claims are labeled unbondable, i.e., uninsurable claims cannot
  present as verified (fixes the 2610.08144 class: cert without matching statement).
- Statement-match rule (hard requirement from the NS lesson): the attestation MUST bind
  BOTH the machine-checkable artifact AND the human-readable statement hash; a mismatch
  voids the bond automatically. "Cert != claim" becomes a forfeiture condition, not a
  debate.

## 3. Lifecycle
POST -> CHALLENGE(W) -> ADJUDICATE -> PAYOUT | EXPIRE (claim certified after W unchallenged,
bond released gradually: e.g. 50% at W, 50% at 30d to catch slow falsification).

## 4. Adjudication
- Tier 1 deterministic: rule-checkers (statement-match, signature validity, spec
  conformance) — automatic.
- Tier 2 expert panel: rotating jury drawn from a staked registry; quorum 3-of-5; decisions
  published with reasoning (truthful-commons requirement).
- Tier 3 escalation: mutually agreed external arbiter / court per adjudication_rule_ref.

## 5. Failure modes & mitigations
- Whale bonds bullying: challenge bonds + jury randomization + appeal tier.
- Adjudicator collusion: jurors post bonds; bad rulings slash; transparency log.
- Griefing/spam challenges: challenger counter-bond forfeited on failed challenge.
- Bond insolvency at scale: insurance layer buys bond pools against audited loss history
  (only possible AFTER bonds exist — sequencing matters).
- Regulatory capture: protocol is content-neutral; rules referenced, not embedded.

## 6. Minimal prototype (feeds Day 5)
Schema (JSON) + local checker (Python): validate attestation structure, statement/artifact
match, expiry windows; tests: valid attest, mismatched-statement forfeiture, expired
challenge, payout math. All offline, no chain required (ledger = signed append-only log).

## 7. Open questions for Day 12 red-team
Identity binding of producer (PKI? wallet? legal entity mapping for P2 signers?);
jury incentive sufficiency; cross-jurisdiction enforceability of adjudication_ref.

## 8. Day-12 disposition of the open questions (§7)
Full audit: `day-12-audit.md`. Positions, per the charter's L2 rule (accepted findings
carry a rationale and a deadline):
- **Identity binding of producer** — *accepted-open.* v0.1 uses operational identity
  (producer string + signer-of-record registry); cryptographic or legal-entity binding
  is deferred until value custody exists (no custody → nothing to bind that matters).
  Deadline: before any real bond is custodied (v0.2 gate); restated in Day-13 synthesis.
- **Jury incentive sufficiency** — *accepted-open.* The 40% jury split + slashing rule
  (§5) is unvalidated design; no challenger market exists at n=1 operator. Deadline:
  Day-13 synthesis states the validation plan; do not claim sufficiency until the first
  real adjudications.
- **Cross-jurisdiction enforceability** — *rejected as in-scope for v0.1, with
  rationale:* the protocol is content-neutral and references rules rather than embedding
  them; Tier-1 deterministic checks (statement-match, signature format) are
  jurisdiction-independent by construction. Revisit at v0.2 only if adoption proceeds.
