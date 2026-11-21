# Dharma Protocol for Agent Systems

[![tests](https://github.com/asbelcas/dharma-protocol/actions/workflows/ci.yml/badge.svg)](https://github.com/asbelcas/dharma-protocol/actions/workflows/ci.yml)

**Status:** draft charter v0.1+rev2 (2026-10-26; rev1 red-team 2026-10-23, rev2 full-corpus audit 2026-10-26 — dispositions in `day-12-audit.md` of the working corpus). **Published draft** — this repo is public (since 2026-10-31); not formally adopted as a standard, not a legal instrument.
Binds only the originating operation's agents until a human chooses otherwise.

A five-article operating charter for agent systems — truthful claims, bonded outputs,
named human signers, ownership transparency, auditable machine commerce — with a
three-rung conformance ladder: **L0 declared · L1 instrumented · L2 adversarially reviewed.**

## Why this exists

The agent economy currently runs on a simple default: generation at scale, with no
price on being wrong. The bill shows up as a disorder index — provenance failures,
certificates that don't match the claims they supposedly support, concentration
dressed as progress. Every tradition the originating project consulted converges on
the opposite engine: an **order that makes truthfulness load-bearing** — ṛta, Ma'at's
feather, asha against druj, 天理, ubuntu's shared personhood, nomos/ius. This charter
is the operator's commitment that the agents and artifacts under its control run on
the first engine, not the second. Dharma here means duty-appropriate conduct that
keeps the web of dependences legible — not decorum, not compliance theater.

## The charter

Text reproduced verbatim from the v0.1+rev2 artifact of record; only heading levels are
adjusted for nesting. The status block's `day-XX` references point to the
DHARMA-13 working corpus — see [Provenance](#provenance).

---

## The Dharma Protocol for Agent Systems — Charter v0.1+rev2 (2026-10-26)

**Status:** rev2 after the Day-12 full-corpus audit (independent leg: Codex job_
20261026T121510Z_18da81d3, read-only; mechanical leg: tests/drift/leak-scan; full
dispositions in `day-12-audit.md`). rev1 followed the Day-8 red-team (Codex
job_20261023T155056Z_50d0c974, critique in `day-08-codex-redteam.md`). ChatGPT advisory
leg blocked by Cloudflare challenge — pending (see `day-08-charter.md`). Draft; not
published *(editor's note 2026-11-19: pre-publication artifact wording — this repo is
public since 2026-10-31; treat as "Published draft; not formally adopted as a
standard")*; binds only this operation's agents until a human chooses otherwise.
**rev2 changes (no semantic shifts to article obligations):** A1(c) implementation claim
scoped to what the instrument does (requires the outcome-check *binding*; executing the
check is the operator's duty); A2 records gain the evidence pointer as an enforced field;
L1 rewritten to name exactly what tooling enforces and what it does not; honesty notes
extended (forfeit_split is allocation arithmetic; hashchain verify() recomputes).
**Derivation:** five pillars (day-03) · attestation spec (day-04) · instrument
(`tools/`, 19/19 tests green 2026-10-26) · cross-cultural verification
(day-07: dharma/ṛta, 天理, nomos/ius, Ma'at, asha, ubuntu, justice-as-cosmic-order).

### Preamble

Every tradition the alliance consulted converges on one engine: an **order that makes
truthfulness load-bearing** — ṛta, Ma'at's feather, asha against druj, 天理, ubuntu's
shared personhood. The agent economy currently runs on the opposite default: generation
at scale with no price on being wrong (day-02 disorder index). This charter is the
operator's commitment that the agents and artifacts under its control run on the first
engine, not the second. Dharma here means duty-appropriate conduct that keeps the web of
dependences legible — not decorum, not compliance theater.

### Articles

**A1 — Truthful claims (satya).** Every externally-facing claim must (a) carry its
epistemic status on its face — proven fact, attested output, model inference, or forecast
— with the status written in human-readable form next to the claim; (b) be checkable
against evidence that is independent of the claimant where the claim is factual; and
(c) where an outcome later materializes, pass a post-hoc `outcome_check`. The reference
instrument enforces this at the binding level: an attestation is invalid unless it
carries {condition, verifier_ref, deadline} (`full_validate`, applied by `certify`);
executing the check when the outcome matures is the operator's duty — the binding is not
optional, the execution is not automatable by a format checker. A certificate or
proof attached to a claim MUST match the human-readable claim it supports (the
2610.08144 lesson). Unprovenanced content is ineligible for bonding, ranking, or payment.
*(Pillar 4; asha vs druj.)*

**A2 — Bonded outputs.** Every material agent output carries an attestation: author
identity, claim, evidence pointer, bond value, challenge window. Bond sizing,
challenger eligibility, adjudication, custody, and payout enforcement follow the Day-4
spec (day-04-attestation-spec.md). Honesty note: the current instrument
(`tools/bondattest.py`) is an attestation *format* — the evidence pointer is an enforced
field (`evidence_ref`), but nothing fetches artifacts or verifies hashes against
external sources; `forfeit_split` is allocation arithmetic, not a transfer; and the
economics simulation's verdict is assumption-bound (simplified discovery; see red-team
§A2 and the Day-12 audit). It does not escrow value or execute payouts. L1 conformance
therefore means "attestation format enforced," not "bond market live." *(Pillar 1, the
keystone; Ma'at's weighing.)*

**A3 — Human ends, named signers.** Every automated action has exactly one named
accountable human who has (a) informed assent — actually reviewed the action class, not
just the UI label, (b) live authority to halt the agent, and (c) real causal control over
what the agent does. The signer must be shown the strongest declined alternative with
each single recommended approval, so "one action, not a menu" cannot be used to suppress
options. Multi-party systems may use role-based signing (one signer per role) rather
than forcing a single scapegoat. "The agent did it" is void. The point is not friction —
aviation's checklists made flight faster by making it trusted. *(Pillar 2; svadharma.)*

**A4 — Ownership transparency.** Rather than mandate outcomes no instrument can verify,
agent-built systems must disclose: who the beneficial owners and control-rights holders
are; concentration of ownership against a stated baseline, with review triggered when
concentration increases; which data contributors' tacit knowledge trained the system and
how they are compensated. Widening ownership (many small owners, co-ops, data dividends)
remains the preferred design; what is enforced is the *disclosure*, which makes
concentration visible instead of silent. *(Pillar 3; ubuntu — personhood through the
shared substrate.)*

**A5 — Auditable commerce.** Agent-to-agent deals execute under published,
human-legible rules; every deal log is (a) append-only or tamper-evident, (b) complete —
capturing inputs and external-state references, not just the operator's chosen events,
with retention long enough for audit, and (c) replayable by an independent auditor from
the log alone, reconciled against real-world outcomes where they exist. Auditability is
a compression problem, not a speed limit. *(Pillar 5; nomos/ius.)*

### Conformance

- **L0 — Declared:** operator has read and adopted the charter; self-assessment only.
  (Costless by design — a starting line, not a claim.)
- **L1 — Instrumented:** tooling in the loop enforces the format layer of each article —
  no more, and this rung claims no more:
  - A1: claims carry status labels; `certify` rejects any attestation without a bound
    outcome check. *(Not enforced: the truth of claims, or execution of outcome checks.)*
  - A2: attestation records with producer, claim, `evidence_ref`, bond value, challenge
    window. *(Not enforced: identity verification, bond custody, adjudication, payouts.)*
  - A3: a signer-of-record entry per automated act. *(Not enforced: signer competence
    or halt capability.)*
  - A4: an ownership-disclosure document, published and dated. *(Not enforced: the
    accuracy of what it discloses.)*
  - A5: the deal log runs on `hashchain` — `verify()` recomputes the chain and detects
    tampering. *(Not enforced: log completeness; no operator-controlled logger can
    prove its own completeness.)*
  Conformance is judged on **outcome trends** — false-claim rate, challenger success
  rate, signer interventions, concentration deltas — with denominators and thresholds
  defined at adoption, not retro-fitted (deadline: Day-13 synthesis), and not on
  instrumentation theater. A red test is a violation; a test suite may not be weakened
  to go green, and any such attempt is itself logged and reported.
- **L2 — Adversarially reviewed:** an independent red-team (Day 12 of this plan, and
  thereafter at least annually) has attempted to break each article; every accepted
  finding carries a written rationale and a remediation or acceptance deadline —
  "openly accepted" without a deadline does not count as resolved.
This operation targets L1 now, L2 by Day 12. The tools/ test suite must stay green.

### Limits

This charter governs this operation's agents and artifacts. It claims no authority over
anyone else's systems, and it is not a legal instrument. It may not be cited to silence
criticism (that would be adharma wearing dharma's clothes). Publication is the human's
call (Day 10 prepares drafts; the human decides what ships).

---

## Translations

Six translations, each with round-trip verification (translate → back-translate →
section-by-section drift report; two material findings found and remediated same-day,
then independently re-verified). The evidence ships in this repo: `charter/i18n/drift/`
and `charter/i18n/roundtrip/`. **Day-13 re-verification (2026-10-27):** all six
translations' A1(c)/A2/L1/Status sections now mirror the English v0.1+rev2 text —
fr/zh independent-leg PASS; hi/ar/sw/es PASS WITH NOTES (single-operator, method
disclosed in each `roundtrip/<code>.rev2-check.md`); the three Day-12 accepted-open
items (sw ×2, es ×1) are cleared. Method and dispositions: `charter/i18n/README.md`
(Day-13 addendum) and `charter/i18n/drift/<code>.md`.

| Code | Language | File | Verification verdict |
|------|----------|------|----------------------|
| fr | français | [`charter/i18n/CHARTER.fr.md`](charter/i18n/CHARTER.fr.md) | faithful-with-notes (0 material, 12 minor) |
| zh | 简体中文 | [`charter/i18n/CHARTER.zh.md`](charter/i18n/CHARTER.zh.md) | faithful-with-notes (0 material, 5 minor) |
| hi | हिन्दी | [`charter/i18n/CHARTER.hi.md`](charter/i18n/CHARTER.hi.md) | needs-revision → **re-verified PASS WITH NOTES** (material fix: Ma'at's feather पक्ष→पंख) |
| ar | العربية الفصحى | [`charter/i18n/CHARTER.ar.md`](charter/i18n/CHARTER.ar.md) | faithful-with-notes (0 material, 18 minor) |
| sw | Kiswahili | [`charter/i18n/CHARTER.sw.md`](charter/i18n/CHARTER.sw.md) | needs-revision → **re-verified PASS WITH NOTES** (material fix: A3 scapegoat idiom) |
| es | Español | [`charter/i18n/CHARTER.es.md`](charter/i18n/CHARTER.es.md) | faithful-with-notes (0 material, 4 minor) |

## Reference instrument

`tools/` holds the minimal offline prototype behind A2: `bondattest.py`
(attestation format — enforced `evidence_ref`, mandatory outcome-check binding via
`full_validate`/`certify`; `forfeit_split` is allocation arithmetic, no value moves),
`hashchain.py` (tamper-evident log — `verify()` recomputes the chain), and
`sim_econ.py` (assumption-bound economics sanity simulation), with the test suite.

```
cd tools && python3 -m pytest
```

Install (stdlib-only, no third-party dependencies; Python ≥ 3.10):

```
pip install .        # from a clone of this repo; installs bondattest, hashchain, sim_econ
python -c "from hashchain import Chain; c = Chain(); c.add('hello'); assert c.verify()"
```

Running from the repo without installing works too — `python3 -m pytest tools/ -q`
from the repo root.

21/21 tests green as of 2026-11-20 (hashchain gained anchored-checkpoint verification,
`verify(expected_tip=..., expected_len=...)`, on that date). Honest status, per the charter's own A2 note: this
instrument enforces an **attestation format** — it does not yet escrow value or execute
payouts, and the economics simulation makes simplified discovery assumptions. L1
conformance means "attestation format enforced," not "bond market live."

## Adoption

[`ADOPT.md`](ADOPT.md) is the L0 declaration template: copy it into your own repo,
fill in the brackets, sign it, and link it from your README. That is L0 — costless by
design, a starting line rather than a claim. L1 requires tooling in the loop; L2
requires an independent red-team with a deadline on every accepted finding.

## Provenance

Derived over a 13-working-day plan (2026-10-10 → 2026-10-24): a five-pillar position
paper, an attestation spec (bond sizing heuristic: a claim must be able to pay for its
own checking), the instrument above, and a cross-cultural verification pass over seven
dharma analogues (dharma/ṛta, 天理, nomos/ius, Ma'at, asha, ubuntu,
justice-as-cosmic-order). Draft v0.1 was independently red-teamed (Codex,
job_20261023T155056Z_50d0c974) and revised to rev1 the same day; the full corpus then
passed a second audit on Day 12 (Codex job_20261026T121510Z_18da81d3 + a mechanical
pass), folding fixes into the instrument and clarifications into the articles — v0.1+rev2.
The accepted findings are folded into the articles and conformance ladder. The `day-XX` references inside the
charter point at that working corpus, which is not shipped in this repo.
