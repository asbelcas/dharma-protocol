# The Dharma Protocol for Agent Systems — Charter Document v0.1+rev1 (2026-10-23)

*(Language: Kiswahili (Swahili) · translator: ask_kimi · date: 2026-10-23 · method: DHARMA-13 Day 9, translation pass A)*

**Status:** rev1 after an independent red team (Codex job_20261023T155056Z_50d0c974, full critique
in `day-08-codex-redteam.md`). The ChatGPT counsel/advisory section has been blocked by a
Cloudflare challenge — it is pending (see `day-08-charter.md`). Draft; unpublished; binds only
the agents of this operation until a human chooses otherwise.
**Derivation:** five pillars (day 3) · attestation strategy (day 4) · tools
(`tools/bondattest.py`, 17/17 tests passed 2026-10-23) · cross-classical verification
(day 7: dharma/ṛta (cosmic order), 天理 (principles of heaven),
nomos/ius (law and right), Ma'at (Egyptian divine justice), asha (truth),
ubuntu (collective/shared human personhood), justice as an ordering of the universe).

## Preamble

Every tradition that the union consulted met at one axle [amb: "inji" — an unusual/borrowed
Swahili word; plausibly "hinge" or "axle"]: **an ordering that makes trust bear a load** —
ṛta, the feather of Ma'at, asha against druj, 天理, the kinship of human shared presence
in ubuntu. Now the agent economy is heading by default the opposite way:
production at scale without a price of error (the day-2 chaos metric).
This document is the operator's promise that agents and products under their authority
go onto the first axle, not the second [amb: "inji" as above]. Dharma here means conduct
befitting responsibility, which holds the web of dependency to be legible/readable — not
honor of appearance/face, not a performance of obedience.

## Articles

**A1 — Truths of claims (satya).** Every claim directed outward must (a) carry its
epistemic status [hali ya elimu, lit. "state of knowledge"] up front — verified truth,
attested output, model inference/conclusion, or
prediction — that status being written in human-readable language near the claim;
(b) be able to be audited against evidence that does not depend on the claimant, where
the claim is one of truth; and (c) where outcomes will sprout/appear later, pass the
post-event `outcome_check` (a stricter audit which is already built into the tool
of record, not optional). A certificate or evidence placed on a claim MUST match the
human-readable claim it supports (the lesson of 2610.08144). Content without provenance
has no quality of being bondable, schedulable, or payable.
*(Pillar 4; asha against druj.)*

**A2 — Bonded outcomes.** Every meaningful output of an agent bears attestation: the
author's identity, claim, evidence descriptor, bond value, challenge window. Bond
measurement/sizing, challenger eligibility, adjudication, custody, and payment verification
follow the Day-4 strategy (`day-04-attestation-spec.md`). Note for fidelity: the current
tool (`tools/bondattest.py`) is a *structure/scaffold* of attestation having signature
and outcome fittings/hooks; it still does not hold value as a deposit/escrow nor does it
settle payments, and the economic narrative makes simplified estimates of discovery
(see red team §A2). Thus, L1 conformance means "the attestation scaffold is implemented,"
not "the bond market is running." *(Pillar 1, the main pillar; the scales of Ma'at.)*

**A3 — Human goals, signers with names.** Every automated act has one single human,
with a name, accountable, who has (a) informed assent [ridhaa iliyojaa ufahamu, lit.
"consent full of understanding"] — has genuinely inspected the kind/type of act, not just
a UI element, (b) live/active halt authority over the agent at any time, and (c) real
control of the cause of what the agent is doing [amb: "udhibiti wa sababu halisi" =
"control of the real cause/reason" — plausibly "real-time control of the cause," i.e.
source-level control]. The signer must be shown one rejected alternative that is more
powerful together with every single proposed assent, so that "one action, not a menu"
is not used to hide an option. Multi-party systems may use signing for duties (one signer
per duty) instead of forcing a single sealed/air-gapped goat [amb: "mbuzi mmoja wa
kufungwa" = "one closed-up goat" — "mbuzi" is unambiguously "goat"; either the source
has a whimsical "goat" or this is a mistranslation of some other word]. "The agent is the
one who did it" is null/void. The goal is not cramming/filling [amb: "msongamano" can be
"congestion/cramming"] — sky/air checklists [amb: "orodha za ukaguzi za anga" = "sky
checklists"; plausibly "airline checklists" in source] made the airplane fast by making it
trustworthy/reliable. *(Pillar 2; svadharma.)*

**A4 — Ownership transparency.** Instead of commanding/decreeing outcomes that no tool can
verify, systems built with agents must disclose: who the beneficial owners and those
having rights of control are; concentration of ownership against a stated threshold,
audit being triggered where concentration increases; which data contributors have secret
knowledge that would injure/harm the system if leaked, and how they are paid. Expansion
of ownership (many small owners, cooperative societies, data dividends) remains the
preferred structure; what is implemented is *disclosure*, which makes concentration
visible instead of silent. *(Pillar 3; ubuntu — personhood through a shared foundation.)*

**A5 — Auditable business.** Agent-to-agent contracts are executed under published,
human-readable rules; every ledger of record is (a) append-only [huongezeka tu, lit.
"it is only added to"] or tamper-evident [inayobainisha uingiliaji wowote, lit. "that
which reveals any interference"], (b) complete — collecting inputs and references of
external state, not only the events selected by the operator, record retention lasting
a long time sufficient for audit, and (c) replayable in full by an independent auditor
from the ledger alone, being compared with the actual outcomes of the world where they
exist. The possibility of audit is a problem of reduction, not a limit of speed.
*(Pillar 5; nomos/ius.)*

## Conformance

- **L0 — Declared/Announced:** the operator has read and used this document; self-assessment
  only. (Without cost to the structure — a starting line, not a claim.)
- **L1 — Enforced with tools:** A1–A5 are implemented with tools within the loop (the
  attestation scaffold via bondattest; the audit record is append-only for every act;
  a formal signer for every automated act; ownership disclosure published). Conformance
  is measured by **behavior of outcomes** — the rate of false claims, the rate of success
  of challengers, entries of signers, differences of concentration — not by a performance
  of tools. A red-team attempt is a violation; a collection of metrics cannot be weakened
  so that it becomes green, and every attempt of that kind is itself recorded and reported.
- **L2 — Audited in an adversarial manner:** an independent red team (Day 12 of this plan,
  and later at least one year each [amb: "kwa mwaka mmoja mmoja" = "one year by one year" —
  plausibly "at least annually"]) has tried to break every clause; every accepted failure
  bears written notes and a date of fixing or of acceptance — "open accepted"
  without a date does not describe that a problem has been reconciled.
This operation is targeting L1 now, L2 when Day 12 arrives. The metrics collection of tools/ must remain green.

## Limits

This document guides the agents and products of this operation. It exercises no authority
over the systems of anyone else, nor is it a legal instrument. It must not be cited in
order to silence criticism (that would be adharma wearing the garments/robes of dharma).
Publication is a human decision (Day 10 prepares the draft; the human decides what is sent).
