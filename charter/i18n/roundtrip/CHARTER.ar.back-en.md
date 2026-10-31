<!-- key terms: epistemic status = الوضع الإبستمولوجي (الحالة المعرفية) · attestation = التوثيق · bond = الكفالة · challenge window = نافذة الطعن · adjudication = الفصل في الطعون · informed assent = الموافقة المستنيرة · halt authority = صلاحية الإيقاف · beneficial owners = المالكون المنتفعون · concentration = التركّز · tamper-evident = كاشف للعبث · append-only = للإلحاق فقط · replayable = قابل لإعادة المحاكاة · conformance = المطابقة · outcome_check = يُترك كرمز برمجي دون ترجمة -->
# Dharma Protocol for Agentic Systems — Charter Version 0.1 + Revision 1 (2026-10-23)

*(Language: Modern Standard Arabic · translator: ask_kimi · date: 2026-10-23 · method: DHARMA-13 Day 9, translation pass A)*

**Status:** Revision 1 after an independent red team (Codex job_20261023T155056Z_50d0c974, full
critique in `day-08-codex-redteam.md`). And the legal-consultation path for ChatGPT was blocked by a
Cloudflare challenge — suspended (see `day-08-charter.md`). Draft; unpublished; binds only the agents of this
process until a human decides otherwise.
**Derivation:** the five pillars (Day 3) · the attestation spec (Day 4) · the tool
(`tools/bondattest.py`, 17/17 tests passing on 2026-10-23) · cross-cultural verification
(Day 7: dharma/ṛta, 天理، nomos/ius، Ma'at، asha، ubuntu، justice as a cosmic system).

## Preamble

All the traditions the coalition consulted converge on one engine: **a system that makes truth a constitutive
burden** — ṛta (the cosmic order of truth), Ma'at's feather, and asha (asha: truth and order) as against
druj (druj: lies and disorder), and 天理، and the shared personhood in ubuntu (ubuntu). As for the agent economy,
it currently operates on the opposite assumption: generation at scale in which error is not priced
(Day 2 disorder index). And this charter is the operator's commitment that the agents and outputs
under his control operate on the first engine, not the second. And dharma here means behavior in
accordance with duty that keeps the network of connections legible and clear — not mere board manners, and not a
compliance theater.

## Provisions

**A1 — Truthful claims (satya).** Every outward-facing claim must: (a) carry its epistemic status
on its face [amb: على ظاهره — "on its outward appearance", i.e. visibly/apparently] — a proven fact,
or an attested output, or a model inference, or a prediction — written in a language humans read next
to the claim; (b) be verifiable in light of evidence independent of the claimant wherever the claim is
factual; (c) wherever an outcome materializes later [amb: حيثما تتجسّد نتيجةٌ لاحقاً — "wherever a
result is embodied later"], pass the subsequent-outcomes check `outcome_check` (the strongest check
actually applied in the reference tool, and it is not optional). And the certificate or proof attached
to the claim must match the readable written claim that the two support [amb: الادعاءَ المقروءَ المكتوبَ
الذي يدعمانه — "which the two of them (certificate and proof) support"]. And content of unknown
provenance is not eligible for bonding, or ranking, or payment. *(Pillar 4; asha vs. druj.)*

**A2 — Bonded outputs.** Every material output of an agent bears an attestation that includes: the
author's identity, the claim, the evidence pointer, the bond value, the challenge window. And the
determination of bond size, challenger eligibility, adjudication of challenges, custody, and enforcement
of disbursement, are subject to the spec approved on Day 4
(day-04-attestation-spec.md). Truth note: the current tool (`tools/bondattest.py`) is a *schema* of
attestation with hooks for signature and outcomes; it holds no value and executes no payments yet, and
the economy simulation relies on simplified assumptions in detection (see the red team §A2). Therefore
L1 conformance means "the attestation schema is imposed [amb: مفروضة — 'imposed/enforced/required']",
not "a bond market exists." *(Pillar 1, the chief stone [amb: الحَجَر الرئيس — literally "the chief/main
stone"; intended sense likely "cornerstone"]; Ma'at's balance.)*

**A3 — Human ends, and signers named by name.** For every automated act, one human named by name and
held accountable, enjoying: (a) informed assent — that is, an actual review of the action category,
not merely a designation in the user interface; (b) a live authority to halt the agent; (c) real causal
control over what the agent does. And the strongest rejected alternative must be presented to the
signer with each single approval recommendation, so that the "one action, no list" approach is not used
to hide options. And multi-party systems may use role-based signing (one signer per role) instead of
forcing a single scapegoat. And saying "the agent is the one who did it" is void. And the intent is not
slowing down — for aviation checklists made aviation faster by making it trustworthy. *(Pillar 2; svadharma.)*

**A4 — Ownership transparency.** Instead of imposing results that no tool can verify, systems built
by agents must disclose: who the beneficial owners and the bearers of control rights are; the
concentration of ownership against a published baseline, with review activation when concentration
rises; and which data contributors' implicit knowledge was used in training the system and how they are
compensated. And breadth of ownership (many small owners, cooperatives, data dividends [amb: أرباح
بيانات — "data profits/dividends"]) remains the preferred design; what is required is *disclosure*,
which makes concentration visible, not silent. *(Pillar 3; ubuntu — personhood through the shared
pillar [amb: عبر الركيزة المشتركة — "through the shared pillar"; odd collocation, see drift report].)*

**A5 — Auditable commerce.** Transactions between agents are executed per published rules that humans
understand; and every transaction record (a) for append-only or tamper-evident [amb: للإلحاق فقط أو
كاشفٌ للعبث — "append-only or tamper-evident"; the (a)/(b)/(c) sub-lettering is slightly broken in the
target], (b) complete — capturing the inputs and references to external state, not only the events the
operator chooses, with retention sufficient for a period for auditing, (c) replayable from the record
alone by an independent auditor, with matching against actual outcomes wherever they exist. And
auditability is a matter of pressure on the data [amb: ضغطٍ للبيانات — "pressure for/of the data";
sense unclear], not a limit on speed. *(Pillar 5; nomos/ius.)*

## Conformance

- **L0 — Declared:** the operator has read the charter and adopted it; self-assessment only.
  (costless by design — a starting line, not a claim.)
- **L1 — Tool-equipped:** A1–A5 are imposed by tools in the workflow (the attestation schema via
  bondattest; an append-only audit log for every action; a registered signer for every automated
  action; publication of the ownership disclosure). And conformance is assessed on the basis of **outcome
  trends** — the false-claims rate, the challengers' success rate, the signers' interventions, and
  concentration gaps — not on the theater of tooling. And the red test is a violation; and it is not
  permitted to weaken the test suite so it becomes green, and any such attempt is itself recorded and
  reported.
- **L2 — Reviewed adversarially:** an independent red team (Day 12 of this plan, and thereafter at
  least once a year) attempts to break every provision; and every accepted finding carries a written
  rationale and an appointment for remediation or for acceptance — for "open" acceptance with no date does
  not count as resolved.
  This process targets L1 now, and L2 by Day 12. And the tools/ test suite must remain green.

## Limits

This charter governs the agents of this process and its outputs. And it claims no authority over systems
other than it [amb: أنظمة غيرها — "systems other than it"; ambiguous scope], and it is not a legal
document. And citing it to silence criticism is impermissible (for that is adharma wearing the robe of
dharma). And publication is the human's decision (Day 10 prepares the drafts; and the human decides what
is published).
