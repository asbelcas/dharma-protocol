# Re-verification 2026-10-27 (Day 13) — zh — A1(c)/A2/L1/Status to rev2

Method: Day-12 handoff task. Pass A (re-translation to rev2): driver session (kimi-cli Day 13),
glossary-bound per the file's key-terms header. Pass B (cold back-translation): independent
leg via agent-bridge ask_kimi (single-file read; literal render of Status/A1/A2/L1 only).
Pass C (diff): driver, clause-by-clause against `../../CHARTER.md` v0.1+rev2.

## Back-translation (ask_kimi, literal)

STATUS: rev2, following the Day-12 whole-corpus audit (independent component: Codex
job_20261026T121510Z_18da81d3, read-only; mechanical components: tests / drift reports /
leakage scans; full disposition in `day-12-audit.md`). rev1 followed the Day-8 independent
red-team review (Codex job_20261023T155056Z_50d0c974, criticisms in
`day-08-codex-redteam.md`). The ChatGPT advisory-review step is blocked by the Cloudflare
human-verification check —— as yet unresolved (see `day-08-charter.md`). This document is
a draft; unpublished; until humans decide otherwise, it binds only the agents within this
operating system [amb: 运营体系 — "operating system/regime," i.e., this operator's own
governance setup, not a computer OS].

A1: True statements (satya, truth). Every outward-facing statement must: (a) carry on its
face its epistemic status —— established fact, attested output, model inference, or
prediction —— and that status must be written alongside the statement in human-readable
form; (b) if the statement is a factual statement, it must be checkable against evidence
independent of the statement's maker; and (c) if a corresponding outcome later
materializes, it must undergo a subsequent `outcome_check` (outcome verification). The
reference tool enforces this at the binding layer: any attestation not carrying
{condition, verifier_ref, deadline} is invalid (`full_validate`, applied by `certify`);
performing the verification once outcomes have matured is the operator's responsibility
—— binding is not optional, and performing the verification is likewise not something a
format checker can automate. A certificate or attestation attached to a statement must
match the human-readable statement it supports (this is the lesson of 2610.08144). Content
without provenance may not be used for bond binding, ranking, or payment. (Pillar 4; asha
against druj.)

A2: Bonded outputs. Every significant agent output must carry an attestation: authorship,
the statement, evidence pointer, bond amount, challenge window. The determination of the
bond amount [amb: 保证金之核定 — "sizing/assessment/ratification of the bond"], challenger
qualification, adjudication, and the execution of escrow and forfeiture payout all follow
the Day-4 spec (`day-04-attestation-spec.md`). Honest disclosure: the current tool
(`tools/bondattest.py`) enforces only the *format* of attestations —— the evidence pointer
is a mandatory field (`evidence_ref`), but it does not fetch the artifact, nor does it
verify hashes against external sources; `forfeit_split` is nothing more than apportionment
arithmetic, not a movement of funds; and the conclusions of the economic simulation are
constrained by its assumptions (a simplified discovery assumption; see red-team review
§A2 and the Day-12 audit). It neither holds value in escrow nor executes payouts.
Therefore L1 conformance means "attestation format is enforced," not "a bond market is
live." (Pillar 1, the keystone; the weighing of Ma'at.)

L1: Instrumented: the toolchain enforces, in closed loop, the format layer of every clause
—— and nothing more; this level also claims nothing more: A1: statements must carry a
status label; `certify` rejects any attestation not bound with outcome verification. (Not
enforced: the truth of statements, and the execution of outcome checks.) A2: attestation
records carrying producer, statement, `evidence_ref`, bond amount, challenge window. (Not
enforced: identity verification, bond escrow, adjudication, payout.) A3: every automated
action has a signer of record. (Not enforced: the signer's competence or halt authority.)
A4: published and dated ownership-disclosure documents. (Not enforced: the accuracy of
what is disclosed.) A5: transaction logs run on `hashchain` —— `verify()` recomputes the
entire hash chain and can detect tampering. (Not enforced: the completeness of the log; no
recorder under the operator's control can attest to its own completeness.) Conformance or
non-conformance is judged by outcome trends —— false-statement rate, challenger success
rate, signer interventions, changes in concentration —— whose denominators and thresholds
are defined at the time of adoption and may not be set retroactively [amb: 不得事后补设 —
"may not be supplemented/established after the fact"; the parenthetical "(deadline: the
Day-13 synthesis report)" attaches to this definitional requirement], not by performances
put on by tool arrangements. A failed test constitutes a violation; the test suite must
not be weakened in order to pass, and any such attempt will itself be recorded and
reported.

## Per-clause diff vs rev2 source

- Status: rev2 lineage, both job IDs, Cloudflare pending, draft scope — recovered.
  运营体系 rendered "operating system" with the verifier's own disambiguation to
  "operator's governance setup" — correct sense (EN: "this operation's agents").
- A1(c): binding-layer enforcement, {condition, verifier_ref, deadline}, full_validate
  applied by certify, operator responsibility, "binding is not optional", "not something
  a format checker can automate" — all recovered. **resolved to rev2**
- A2: four honesty elements (evidence_ref mandatory; no artifact fetch; no external hash
  verification; forfeit_split apportionment arithmetic not fund movement; assumption-bound
  with both refs) + no escrow/no payouts + L1 meaning — recovered. "执行，均遵循" correctly
  scopes escrow+forfeiture-payout to the Day-4 spec per source. **resolved to rev2**
- L1: five sub-bullets + not-enforced lists + operator-logger completeness sentence +
  four metrics + denominators/thresholds at adoption, not retroactive, Day-13 deadline
  parenthetical + red-test rule — recovered. **resolved to rev2**
- Glossary check: 认知状态/证明/保证金/异议窗口/裁决/受益所有人/集中度/篡改可验/仅追加/
  可重放/合规 honored; code tokens verbatim.

VERDICT: **PASS** (independent leg). No material drift; [amb] notes are accurate
disambiguations, none action-changing.
