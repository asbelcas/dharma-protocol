# Drift Report — zh (Simplified Chinese)

- **Language:** zh — Simplified Chinese (`charter/i18n/CHARTER.zh.md`)
- **Date:** 2026-10-23
- **Method note:** back-translated from translation alone, then diffed against source.

## Findings

| Section | Source meaning (short quote) | Back-translated rendering | Severity | Cause |
|---|---|---|---|---|
| Header/Status | "rev1 after independent red-team (Codex job_…)" | "rev1, already independently red-team reviewed (Codex job_…)" | none | faithful |
| Status | "ChatGPT advisory leg blocked by Cloudflare challenge — pending" | "ChatGPT legal-counsel session blocked by Cloudflare human-verification — still pending resolution" | none | faithful |
| Status | "binds only this operation's agents until a human chooses otherwise" | "before humans decide otherwise, it binds only the agents within this operation's system" [amb: 运营体系 = operating system / operational framework] | none | faithful |
| Derivation | "justice-as-cosmic-order" | "justice as cosmic order" (rendered as list-final item with 以及) | none | faithful |
| Preamble | "one engine: an **order that makes truthfulness load-bearing** — ṛta, Ma'at's feather, asha against druj, 天理, ubuntu's shared personhood" | same, but target adds glosses absent from source: ṛta（真理秩序）, druj（虚假） | minor | translator-error (addition, not substitution — glosses are accurate) |
| Preamble | "no price on being wrong" / "under its control" / "not decorum" | "pay no price for error" / "under its jurisdiction (所管辖)" / "not etiquette" | none | faithful |
| A1 | "Truthful claims (satya)" | "True statements (satya, 真实)" — added gloss 真实; "claim" consistently → 陈述 ("statement"), "claimant" → 陈述者 | minor | translator-error (addition; claim→statement is a defensible register choice, consistently applied) |
| A1 | "MUST match … (the 2610.08144 lesson). Unprovenanced content is ineligible for bonding, ranking, or payment" | "must match … (lesson of 2610.08144). Content without provenance must not be used for bond-binding, ranking, or payment" | none | faithful |
| A2 | "Every material agent output carries an attestation" | "Every significant/major (重大) agent output must carry attestation" — adds explicit 均须 | none | faithful |
| A2 | "signature and outcome hooks" / "does not yet escrow value or execute payouts" | "signatures and outcome-linkage" / "does not yet possess value-custody or payout-execution capability" | none | faithful |
| A3 | "Human ends, named signers" | "Human-centered (以人为本), named signatories" | minor | untranslatable-term / ambiguity-in-target — "ends" (purposes/telos) wordplay is flattened to "centered-on-people"; the normative sense survives but the pun on "ends" is lost |
| A3 | "informed assent — actually reviewed the action class, not just the UI label, (b) live authority to halt the agent, (c) real causal control" | "informed assent — genuinely reviewed that action category, not merely the interface label; power to halt the agent's operation in real time; genuine causal control" | none | faithful |
| A3 | "shown the strongest declined alternative with each single recommended approval, so 'one action, not a menu' cannot be used to suppress options" | "beyond each individual recommended approval, simultaneously see the rejected best alternative, so 'give only one action, not a bundle of options' cannot be used to suppress options" | none | faithful |
| A3 | "aviation's checklists made flight faster by making it trusted" | "aviation checklists precisely make flight faster by making it credible/trustworthy" [amb: 可信 spans credible/trustworthy/believable] | none | faithful |
| A3 | "*(Pillar 2; svadharma.)*" | "*(第 2 支柱；svadharma，分内之责。)*" — added gloss 分内之责 | minor | translator-error (accurate added gloss, absent in source) |
| A4 | "mandate outcomes no instrument can verify" / "control-rights holders" / "concentration … against a stated baseline, with review triggered when concentration increases" | "enforce results no tool can verify" / "control-right holders" / "relative to declared baseline … review triggered when concentration rises" | none | faithful |
| A4 | "makes concentration visible instead of silent" | "makes concentration visible, rather than [staying] silent" — subject of 而非默不作声 left implicit | minor | ambiguity-in-target — reads as either "concentration not silent" or "the system not silent"; both recover the source intent, but the sentence is grammatically looser than the source |
| A5 | "Auditable commerce" / "Agent-to-agent deals execute under published, human-legible rules" | "Auditable transactions" / "transactions between agents must be executed according to public, human-readable rules" | minor | translator-error (register flattening: commerce/deals → transactions; "published" → 公开 "public" — no practical change in obligation) |
| A5 | "not a speed limit" | "not a speed ceiling/cap (速度上限)" | none | faithful — "upper limit on speed" preserves the intended "not a cap on throughput" |
| A5 | "*(Pillar 5; nomos/ius.)*" | "*(第 5 支柱；nomos/ius，法则与权利。)*" — added gloss "law and rights" | minor | translator-error (accurate added gloss, absent in source) |
| L0 | "Costless by design — a starting line, not a claim" | "zero cost by design — this is the starting line, not a claim" | none | faithful |
| L1 | "L1 — Instrumented … not on instrumentation theater" | "L1 — Tooled (已工具化) … not by the performance of tool-decoration (工具摆设之表演)" | minor | ambiguity-in-target — "instrumentation theater" becomes "theater of tools-as-decoration"; the intended meaning (tooling that exists only for show) is recoverable but the phrasing is clumsier and could be misread as "decorative tools" rather than "performative compliance" |
| L1 | "A red test is a violation; a test suite may not be weakened to go green … logged and reported" | "a failed test constitutes a violation; test suite must not be weakened to pass … logged and reported" | none | faithful |
| L2 | "remediation or acceptance deadline — 'openly accepted' without a deadline does not count as resolved" | "fix-or-acceptance deadline — 'open acceptance' with no deadline not regarded as resolved" | none | faithful |
| Limits | "adharma wearing dharma's clothes" | "非法 (unlawfulness) wearing dharma's outer garment, adharma" | none | faithful — 非法 risks a juridical "illegal" reading, but adharma is retained alongside, disambiguating it |
| Limits | "the human decides what ships" | "humans decide what is published (何者发布)" | minor | translator-error (idiom flattened: "ships" → "published"; same practical meaning) |

### Minor finding explanations

1. **Added glosses** (Preamble ṛta/druj; A1 satya; A3 svadharma; A5 nomos/ius): the target inserts short parenthetical explanations the source does not have. All glosses are accurate; risk is only tonal — the Chinese reads slightly more didactic than the spare English. No reader would act differently.
2. **A3 title "Human ends" → 以人为本**: the pun on "ends" (human purposes vs. human-centeredness) is flattened. A Chinese reader sees "people-first, named signatories" — same operative requirement, weaker rhetorical point.
3. **A4 "instead of silent"**: 而非默不作声 leaves the subject implicit; recoverable ambiguity, no action change.
4. **L1 "instrumentation theater" → 工具摆设之表演**: "摆设" (decoration/display) shifts the metaphor from performance-for-observers to mere ornament; in context (judged by outcome trends, not X) the meaning is pinned and unambiguous.
5. **Register flattening in A5/Limits**: commerce/deals → 交易， "ships" → 发布. Obligations unchanged.

## Untranslatable-term notes

- **dharma**: no native Chinese equivalent carrying both "duty" and "cosmic order". Translation chose 正法 ("upright law/dharma", Buddhist-semantic field) over transliteration 达摩， and documents the choice in the file's key-terms header. Sound choice; a general Chinese reader will read 正法 as Buddhist "true dharma/law", which is within tolerance.
- **adharma**: rendered 非法 (which on its own reads as "illegal") with the transliteration adharma kept adjacent — the pairing rescues it, but 非法 alone would drift toward juridical "unlawful"; glossing as 非法（失序/非正法） would be safer.
- **svadharma, ṛta, Ma'at, asha, druj, ubuntu, nomos/ius, satya, 天理**: proper nouns / cross-cultural terms kept as-is (with accurate added glosses); no native equivalent exists or is desirable.
- **"load-bearing"**: 承重结构 (engineering term) — exact equivalent, no issue.
- **"red-team / red test / go green"**: 红队 / 测试未通过 / 通过 — standard borrowing, no issue.

## VERDICT

VERDICT: faithful-with-notes

0 material findings; 5 minor findings (listed above with explanations). No required fixes for comprehension; recommended (optional) polish: (a) A3 title could render "ends" as 目的 to partially recover the pun (以人为本，为目的服务); (b) consider 非正法 instead of 非法 for adharma; (c) tighten A4's 而非默不作声 to 而非让集中度隐而不见 and L1's 工具摆设之表演 to 工具形式主义表演.

What was checked: every section of the source (Status, Derivation, Preamble, A1–A5, L0–L2, Limits) was diffed line-by-line against the back-translation; bold/italic shapes, numbering, file names, job IDs, and pillar/cross-cultural references all match. Untranslated tokens (A1–A5, L0–L2, outcome_check, 2610.08144, day-NN file names, Codex job id) verified intact.


## Day-12 addendum (2026-10-26, DHARMA-13 Day-12 audit)
Source bumped to v0.1+rev2. This translation's A1(c), A2, and L1 sections still mirror
rev1 text (visible drift, disclosed in the rev2 notice atop CHARTER.zh.md); full
re-verification of those three sections is a Day-13 task. Header count/date refreshed:
19/19 tests green 2026-10-26.
- zh fix applied: `法律顾问环节`→`顾问审核环节` (advisory review stage; the source claims no legal-counsel characterization).


## Day-13 addendum (2026-10-27, DHARMA-13 Day-13 satya consolidation)
A1(c)、A2、L1 与状态块已重译对齐英文 v0.1+rev2；`../CHARTER.zh.md` 顶部 rev2 告示已更新。
核验：独立环节 —— 经 agent-bridge ask_kimi 对四节做冷回译，再对照 rev2 原文逐 clause
比对。完整证据：`roundtrip/zh.rev2-check.md`。
- 状态 → rev2 源流：已恢复（两个 job ID、两个环节、Cloudflare 待解）。resolved
- A1(c) 绑定层面范围（{condition, verifier_ref, deadline}；full_validate 由 certify
  施用；运营者职责执行核验）：各 clause 全部恢复。resolved
- A2 扩展诚实说明（evidence_ref 强制字段；不抓取工件/不核哈希；forfeit_split 为分摊
  算术；结论受假设约束并附两处引用）：各要素全部恢复。resolved
- L1 分条强制执行 + 未强制执行清单 + 结果趋势指标 + 分母/阈值条款：已恢复。resolved
- 核验者 [amb] 注记（运营体系=治理体系而非计算机 OS；核定；事后补设）均为判读
  说明，无需改动。

VERDICT: **PASS**（独立环节）。无实质漂移。
