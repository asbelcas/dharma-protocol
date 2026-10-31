# Re-verification 2026-10-27 (Day 13) — fr — A1(c)/A2/L1/Status to rev2

Method: Day-12 handoff task. Pass A (re-translation to rev2): driver session (kimi-cli Day 13),
glossary-bound per the file's key-terms header. Pass B (cold back-translation): independent
leg via agent-bridge ask_kimi (single-file read; literal render of Status/A1/A2/L1 only).
Pass C (diff): driver, clause-by-clause against `../../CHARTER.md` v0.1+rev2.

## Back-translation (ask_kimi, literal)

STATUS: rev2 after the full day-12 corpus audit (independent leg: Codex
job_20261026T121510Z_18da81d3, read-only; mechanical leg: tests/drift reports/leak scan;
full dispositions in `day-12-audit.md`). rev1 followed the day-8 red-team (Codex
job_20261023T155056Z_50d0c974, critique in `day-08-codex-redteam.md`). The ChatGPT
consultative route is blocked by a Cloudflare challenge — pending (see
`day-08-charter.md`). Draft; unpublished; binds only the agents of this operation until a
human decides otherwise.

A1: Truthful assertions (satya). Every assertion destined for the outside must (a) carry
its epistemic status on itself — established fact, attested output, model inference, or
forecast — the status being written in readable human language, next to the assertion; (b)
be verifiable on the basis of evidence independent of its author, when it is factual; and
(c) when an outcome materializes later, satisfy an `outcome_check` a posteriori. The
reference instrument enforces this at the link level: an attestation is invalid unless it
carries {condition, verifier_ref, deadline} (`full_validate`, applied by `certify`);
executing the verification when the result matures is the operator's duty — the link is
not optional, and the execution cannot be automated by a format checker. A certificate or
a piece of evidence attached to an assertion MUST correspond to the readable assertion it
supports (the lesson of 2610.08144). Content without provenance is ineligible for bonding,
for ranking, or for payment. (Pillar 4; asha against druj.)

A2: Bonded outputs. Every substantial output of an agent bears an attestation: author
identity, assertion, pointer to the evidence, bond value, challenge window. The sizing of
the bond, the eligibility of challengers, adjudication, custody, and the execution of
payments follow the day-4 specification (day-04-attestation-spec.md). Honesty note: the
current instrument (`tools/bondattest.py`) is an attestation *format* — the pointer to the
evidence is a required field (`evidence_ref`), but nothing fetches the artefacts nor
verifies the hashes against external sources; `forfeit_split` is a splitting arithmetic,
not a transfer; and the verdict of the economic simulation is tied to its assumptions
(simplified discovery; see red-team §A2 and the day-12 audit). It does not sequester value
nor execute payments. L1 compliance therefore means "attestation format applied," and not
"bond market in service." (Pillar 1, the keystone; the weighing of Ma'at.)

L1: Instrumented: the tooling in the loop enforces the format layer of each article — no
more, and this tier does not claim more: A1: assertions bear their status labels;
`certify` rejects any attestation without a linked outcome verification. (Not enforced:
the truth of assertions, nor the execution of outcome verifications.) A2: attestation
records with producer, assertion, `evidence_ref`, bond value, challenge window. (Not
enforced: identity verification, bond custody, adjudication, payments.) A3: one reference
signatory entry per automated act. (Not enforced: the signatory's competence or their halt
power.) A4: an ownership disclosure document, published and dated. (Not enforced: the
accuracy of what it discloses.) A5: the transaction log rests on `hashchain` — `verify()`
recomputes the chain and detects any tampering. (Not enforced: the completeness of the
log; no log kept by the operator can prove its own completeness.) Compliance is judged on
the trends of outcomes — false-assertion rates, challenger success rates, signatory
interventions, concentration variations — with denominators and thresholds defined at
adoption, not adjusted after the fact (deadline: day-13 synthesis), and not on the theatre
of instrumentation. A red test is a violation; a test suite must not be weakened to pass
green, and any attempt of this kind is itself logged and reported.

## Per-clause diff vs rev2 source

- Status: rev2 lineage + both Codex job IDs + Cloudflare pending + draft scope — all
  recovered. dispositions → "dispositions" [amb noted by verifier: findings/provisions] —
  acceptable (the EN source itself says "full dispositions in day-12-audit.md").
- A1(c): binding-level enforcement, {condition, verifier_ref, deadline}, full_validate
  applied by certify, operator-duty execution, "not optional", "not automatable by a
  format checker" — all clauses recovered. "attested output" for "sortie attestée" is the
  correct EN sense. **resolved to rev2**
- A2: all four honesty-note elements (evidence_ref enforced; no artifact fetch/hash
  verification; forfeit_split allocation arithmetic; assumption-bound verdict with both
  refs) + "does not escrow value or execute payouts" + L1-meaning sentence — recovered.
  **resolved to rev2**
- L1: five sub-bullets with correct not-enforced lists (incl. the operator-logger
  completeness sentence), four outcome-trend metrics, denominators/thresholds "at
  adoption, not adjusted after the fact (deadline: day-13 synthesis)", red-test rule —
  recovered. **resolved to rev2**
- Glossary check: statut épistémique, caution/cautionnement, fenêtre de contestation,
  arbitrage, divulgation (Day-12 fix) all honored; code tokens verbatim.

VERDICT: **PASS** (independent leg). No material drift; verifier [amb] notes are
translator-judgment calls, none action-changing.
