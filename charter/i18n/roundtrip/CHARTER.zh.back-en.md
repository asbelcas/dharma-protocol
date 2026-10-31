<!-- key terms: epistemic status=认知状态 · attestation=证明 · bond=保证金 · challenge window=异议窗口 · adjudication=裁决 · informed assent=知情同意 · halt authority=中止权 · beneficial owners=受益所有人 · concentration=集中度 · tamper-evident=篡改可验 · append-only=仅追加 · replayable=可重放 · conformance=合规 · outcome_check=结果核验 · Dharma Protocol=正法协议 ("upright law/dharma" is chosen to convey dharma as duty and the law of cosmic order; NOT the transliteration "达摩") -->
# Agent Systems Dharma Protocol — Charter v0.1+rev1 (2026-10-23)
*(Language: Simplified Chinese Simplified Chinese · translator: ask_kimi · date: 2026-10-23 · method: DHARMA-13 Day 9, translation pass A)*

**Status:** rev1, already independently red-team reviewed (Codex job_20261023T155056Z_50d0c974, full criticism see
`day-08-codex-redteam.md`). The ChatGPT legal-counsel session was blocked by Cloudflare
human-verification —— still pending resolution (see `day-08-charter.md`). This document is a draft; not published; before
humans decide otherwise, it binds only the agents within this operating system [amb: "运营体系" can read as "operating system" in the software sense or "operations system/framework" in the organizational sense; the source presumably means the operator's own deployment/operation].
**Derivation:** the Five Pillars (Day 3) · attestation spec (Day 4) · tooling
(`tools/bondattest.py`, 2026-10-23 same-day 17/17 tests all passing) · cross-cultural validation
(Day 7: dharma/ṛta, 天理 [tiānli — "heavenly principle"], nomos/ius, Ma'at, asha, and justice as cosmic order).

## Preamble

Every tradition the alliance consulted converges on the same engine: **an order that makes truthfulness a load-bearing structure** ——
ṛta (the order of truth), the feather of Ma'at, asha's resistance to druj (falsehood), 天理 [heavenly principle], ubuntu's
shared personhood. The agent economy currently runs on the opposite default setting: generating at scale, yet paying
no price whatsoever for error (Day 2 disorder index). This charter is the operator's commitment: the agents and
artifacts under its jurisdiction run on the former engine, not the latter. The Dharma here means behavior proportionate to duty
that keeps the web of dependencies clearly legible —— not etiquette, not compliance theater.

## Articles

**A1 —— True statements (satya, truth).** Every externally-facing statement must: (a) on its very face carry its
epistemic status —— attested fact, attested output, model inference, or prediction —— and that status must be written
in human-readable form alongside the statement; (b) if that statement is a factual statement, it must be checkable
against evidence independent of the statement-maker; and (c) if a corresponding outcome later materializes, it must
undergo ex-post `outcome_check` (result verification)
(this is a stronger check already implemented in the reference tooling, not optional). Certificates or attestations attached
to a statement must match the human-readable statement they support (this is the lesson of 2610.08144). Content without
provenance must not be used for bond-binding, ranking, or payment. *(Pillar 4; asha against druj.)*

**A2 —— Bonded outputs.** Every significant agent output must carry attestation: authorship, statements,
evidence pointers, bond amount, challenge window. The assessment of the bond, challenger eligibility, adjudication,
and the execution of escrow and payout all follow the Day 4 spec (`day-04-attestation-spec.md`). Honest statement:
the current tooling (`tools/bondattest.py`) is only an attestation *format* with signatures and outcome-linkage; it does not yet
possess value-custody or payout-execution capability, and the economic simulation adopted a simplified discovery
assumption (see red-team review §A2). Therefore, L1 compliance means "attestation format is enforced," not "the bond
market is live." *(Pillar 1, keystone; the weighing of Ma'at.)*

**A3 —— Human-centered, named signatory.** Every automated action has one and only one named, accountable
human, who must satisfy: (a) informed assent —— having genuinely reviewed that action category, not merely seen an interface
label; (b) possesses the power to halt that agent's operation in real time; and (c) has genuine
causal control over the agent's behavior. The signatory, beyond each individual recommendation approval, must simultaneously see the rejected best alternative(s),
so that "give only one action, not a bundle of options" cannot be used to suppress options. Multi-party systems may use role-based
signing (one signatory per role), without forcing the creation of a single scapegoat. The claim "the agent did it"
is invalid. The point is not to add friction —— aviation checklists are precisely what make flight faster by making it credible [amb: 通过使飞行可信而令其更快 — "make flight credible/trustworthy thereby make it faster"; "credible" here renders 可信, which can mean "credible", "trustworthy", or "believable"].
*(Pillar 2; svadharma, duty within one's station / one's own duty.)*

**A4 —— Ownership transparency.** Rather than enforcing a result no tool can verify, require that systems built by agents disclose: who the beneficial owners and control-right holders are; the concentration of ownership
relative to the declared baseline, and triggering review when concentration rises; which data contributors' tacit
knowledge trained the system, and how they are compensated. Widened ownership (many small owners, cooperatives, data dividends)
remains the preferred design; what is enforced is *the disclosure itself*, which makes concentration visible rather than
[amb: 而非默不作声 — "rather than [staying] silent/tacit"; the object of "rather than" is left implicit: rather than concentration staying silent / rather than silence]. *(Pillar 3; ubuntu ——
personhood achieved through a shared substrate.)*

**A5 —— Auditable transactions.** Transactions between agents must be executed according to public, human-readable rules;
every transaction log must: (a) be append-only or tamper-evident; (b) be complete —— it must record inputs and external-state
references, not only operator-selected events, and be retained long enough to support audit; and (c) be fully replayable by an
independent auditor from the log alone, and checked against real-world outcomes where such exist. Auditability is a
compression problem, not a speed ceiling [amb: 速度上限 — "speed upper-limit/cap"; could render "speed limit" in the sense of a ceiling on throughput]. *(Pillar 5; nomos/ius, law and rights.)*

## Conformance

- **L0 —— Declared:** the operator has read and adopted this charter; self-assessment only. (Zero cost by design ——
  this is the starting line, not a claim.)
- **L1 —— Tooled:** A1–A5 are enforced in closed loop by the toolchain (attestation format implemented
  via bondattest; an append-only audit log attached to every action; every automated act has a documented signatory;
  ownership disclosure published). Compliance or non-compliance is judged by **outcome trends** —— false-statement
  rate, challenger success rate, signatory intervention count, concentration delta —— not by the performance of
  tool-arrangement [amb: 工具摆设之表演 — "the theater of tools-as-decoration / of tool display", i.e. not by tool theater]. A failed
  test constitutes a violation; the test suite must not be weakened in order to pass, and any such attempt will itself be
  logged and reported.
- **L2 —— Adversarially reviewed:** an independent red team (Day 12 of this program, thereafter at least annually)
  has attempted to break each article one by one; every accepted finding must carry a written rationale, and a deadline for
  fix or acceptance —— "open acceptance" with no deadline is not regarded as resolved.
This operating system currently targets L1, reaching L2 before Day 12. The test suite under tools/ must be kept
all-passing.

## Limits

This charter governs the agents and artifacts of this operating system [amb: 运营体系 again — "operating system" vs "operational framework"]. It asserts authority over no
other party's system, nor is it a legal instrument. It must not be cited to suppress criticism (that would be adharma — illegality/unrighteousness wearing the cloak of dharma [amb: 非法 renders "unlawful/illegitimate" — "illegal" in the moral rather than juridical sense; literally "not-law", i.e. adharma]). Whether
to publish is decided by humans (draft ready Day 10; humans decide what is published).
