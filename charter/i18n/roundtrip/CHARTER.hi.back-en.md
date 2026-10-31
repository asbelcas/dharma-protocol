<!-- Back-translation (Pass 1) of CHARTER.hi.md into English, rendered as literally as fidelity allows. Untranslated tokens kept as-is. [amb: ...] marks phrasing where the Hindi is ambiguous or non-standard. -->
# Dharma-Protocol for Agent-Systems — Formal Covenant (Charter) v0.1+rev1 (2026-10-23)
*(Language: Hindi Hindi · translator: ask_kimi · date: 2026-10-23 · method: DHARMA-13 Day 9, translation pass A)*

**Status:** rev1 after an independent red-team (Codex job_20261023T155056Z_50d0c974, full review
in `day-08-codex-redteam.md`). ChatGPT advisory-stage blocked by Cloudflare
security-challenge — pending (see `day-08-charter.md`). Draft; unpublished;
binds only this operation's agents, until a human decides otherwise.
**Derivation:** five pillars (day-03) · attestation-specification (day-04) · tool
(`tools/bondattest.py`, 17/17 tests successful on 2026-10-23) · cross-cultural verification
(day-07: dharma/rit, 天理, nomos/ius, Ma'at, asha, ubuntu, and justice as cosmic-order).

## Preamble

The traditions the consortium consulted all converge on a single engine: **an order
that makes honesty the load-bearer** — ऋत, the side of Ma'at (Maat — goddess of truth and justice),
asha (ash — order-of-truth) against druj (druj — falsehood), 天理 (tianli — heavenly
justice-system), ubuntu's (ubuntu — shared humanity) shared personhood. The agent-economy
currently runs on the opposite fundamental condition: production at broad scale
without paying any price for being wrong (day-02 disorder index). This formal-covenant is
the operator's commitment that the agents and manufactured-things remaining under its
control run on the first engine, not the second. Here the meaning of dharma is
duty-conforming conduct, which keeps the dependency-web legible — not
politeness, not compliance-theater.

## Articles

**A1 — honest-claims (truth).** Each externally-facing claim shall: (a) mark its epistemic status
on its own face — proven fact, attested product, model-inference, or prediction —
and that status be marked in human-readable form near the claim; (b) where the claim is factual, it
be checkable against evidence independent of the claim-maker; and (c) where any outcome later
materializes, pass a post-temporal check [amb: उत्तर-कालीन, lit. "post-temporal"; intent: retrospective/retroactive] via `outcome_check` (this strong check is already
implemented in the reference-tool, not optional). The certificate or evidence attached to the
claim must match that human-readable claim which it supports (lesson of 2610.08144).
Sourceless content is ineligible for bonding, ranking, or payment. *(Pillar 4; asha vs druj.)*

**A2 — bonded products.** With each significant agent-product an attestation is attached:
author-identity, claim, evidence-pointer, bond-value, challenge-window. Bond-determination,
challenger-eligibility, adjudication, custody (custody), and payment-fidelity follow the Day-4
specification (`day-04-attestation-spec.md`). Honesty-note: the current tool
(`tools/bondattest.py`) is an attestation *format* only, with signature and outcome-hook; it
does not yet do value-escrow (escrow) or payment-fidelity, and the economics-simulation
makes simplified search-priors (see red-team §A2). Therefore the meaning of L1 conformance is
"attestation-format implemented", not "bond-market active". *(Pillar 1, keystone; Ma'at's weighing.)*

**A3 — human-terminal, named signatory.** Each automated action has exactly one
named, answerable human, who has (a) informed assent — has actually reviewed the action-class,
not only the UI label, (b) a live authority to stop the agent,
and (c) real causal control over the agent's actions. The signatory must be shown, with each single
recommended approval, the strongest rejected alternative, so that the pantomime of "one action,
not a menu" does not become a means for suppressing options. Multi-party
systems may adopt role-based signatures (one signatory per role), instead of
imposing a single sacrificial-scapegoat [amb: बलि-बकरा lit. "sacrificial goat" = scapegoat]. "The agent did it" —
this is null and void. The issue is not friction — aviation's checklists made flight reliable, thereby
fast. *(Pillar 2; svadharma.)*

**A4 — ownership-transparency.** Instead of mandating those outcomes which no tool
can verify, agent-built systems must disclose: who the beneficial owners and
control-right holders are; concentration of ownership against the declared baseline, in which
review is triggered as concentration rises; by/on which data-contributors' embedded knowledge-insight [amb: निहित ज्ञान-सूझ, lit. "embedded knowledge-insight"; intent likely "tacit knowledge"] the system
was trained, and how their compensation happens. Extension of ownership (many small owners,
cooperatives, data-dividends) remains the best design; what is enforced is *disclosure*,
which makes concentration visible instead of silent. *(Pillar 3; ubuntu — personhood through
shared infrastructure.)*

**A5 — auditable commerce.** Agent-to-agent deals are executed under published, human-readable
rules; each deal-log (a) be append-only or tamper-evident, (b) be complete —
not only the operator's chosen events, but also mark the inputs and external-context
references, and be retained for a sufficiently long period for audit, and (c) be replayable from the log alone
by an independent auditor, and where real-world outcomes exist, be matched against
them. Auditability is a compression-problem, not a speed-limit. *(Pillar 5; nomos/ius — law and
system-of-rights.)*

## Conformance

- **L0 — declared:** the operator has read and adopted the formal-covenant; self-assessment only.
  (Free by hypothesis — a starting-line, not a claim.)
- **L1 — tool-enforced:** A1–A5 enforced in-loop by tools (attestation-format
  via bondattest; per-action append-only audit log; signatory-record per automated task;
  ownership-disclosure published). Conformance is based on **outcome-tendencies** —
  false-claim rate, challenger-success rate, signatory-intervention, concentration-delta —
  not on tool-theater. A red test [amb: लाल परीक्षण, lit. "red test/examination"; intent: a (failing) red test in the test-suite] is a violation; the test-suite may not be weakened in order to
  make it green, and any such attempt is itself logged and reported.
- **L2 — adversary-reviewed:** an independent red-team (this plan's Day 12, and thereafter
  at least once in a year) has attempted to break each article; with each accepted finding attached
  written justification and remediation-or-acceptance-time-limit — "accepted in open form" without a
  time-limit is not considered a solution.
This operation currently targets L1, targeting L2 by Day 12. tools/ test-suite should stay green.

## Limits

This formal-covenant governs this operation's agents and manufactured-things. It lays claim to no
authority over anyone else's systems, and neither is it any legal writ/warrant [amb: वाद-पत्र lit. "case-document"; intent: legal instrument/writ]. It may not be
cited in order to silence criticism (that would be unrighteousness wearing the garb of dharma).
Publication is a human's decision (Day 10 prepares the draft; what will be published, the human
decides).
