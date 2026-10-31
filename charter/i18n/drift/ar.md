# Drift Report — CHARTER.ar (Modern Standard Arabic)

- **Language:** ar — Modern Standard Arabic (`charter/i18n/CHARTER.ar.md`)
- **Date:** 2026-10-23
- **Method:** back-translated from translation alone, then diffed against source
- **Back-translation:** `charter/i18n/roundtrip/CHARTER.ar.back-en.md`

## Findings

| Section | Source meaning (quote) | Back-translated rendering | Severity | Cause |
|---|---|---|---|---|
| Header | "Charter v0.1+rev1" | "Charter Version 0.1+Revision 1" (المراجعة 1) | minor | ambiguity-in-target |
| Status | "blocked by Cloudflare challenge — **pending**" | "blocked … — **suspended**" (معلَّق) | minor | ambiguity-in-target |
| Derivation | "justice-as-cosmic-order" | "justice as a cosmic system" (نظاماً كونياً) | minor | ambiguity-in-target |
| Preamble | "an **order that makes truthfulness load-bearing**" | "a system that makes truth a constitutive/structural burden" (حَمْلاً إنشائياً) | minor | ambiguity-in-target |
| Preamble | "keeps the web of **dependences** legible" | "keeps the network of **connections** legible" (شبكة الارتباطات) | minor | translator-error (narrowing) |
| Preamble | "not **decorum**, not compliance theater" | "not mere **board manners**" (أدب المجلس) | minor | translator-error (narrowing) |
| Preamble | "ṛta, Ma'at's feather, asha against druj" (bare terms) | same terms **plus added glosses**: "(the cosmic order of truth)", "(asha: truth and order)", "(druj: lies and disorder)" | minor | translator-error (source-foreign addition) |
| Preamble / A4 | "ubuntu's shared **personhood**" / "personhood through the shared substrate" | "the shared **personality/personhood**" (الشخصية المشتركة) | minor | ambiguity-in-target |
| A1(b) | "where the claim is **factual**" | "wherever the claim is **realistic/actual**" (واقعياً) | minor | ambiguity-in-target |
| A1(c) | "pass a **post-hoc** `outcome_check`" | "pass the **subsequent-results** check" (فحص النتائج اللاحقة) | minor | translator-error (paraphrase) |
| A1(c) | "the **stronger** check already implemented" | "the **strongest** check actually applied" (الأقوى) | minor | translator-error (degree shift) |
| A2 | "does not yet **escrow** value" | "does not **hold/custody** value" (لا تحتجز قيمةً) | minor | untranslatable-term |
| A2 | "Pillar 1, the **keystone**" | "Pillar 1, the **chief/main stone**" (الحَجَر الرئيس) | minor | untranslatable-term |
| A3 | "made flight faster by making it **trusted**" | "made aviation faster by making it **trustworthy/reliable**" (موثوقاً) | minor | ambiguity-in-target |
| A4 | "co-ops, **data dividends**" | "cooperatives, **data profits/earnings**" (أرباح بيانات) | minor | untranslatable-term |
| A4 | "personhood through the shared **substrate**" | "personhood through the shared **pillar/foundation**" (الركيزة المشتركة) | minor | untranslatable-term |
| A5(a) | "every deal log is (a) append-only or tamper-evident" | "(a) **for** append-only or tamper-evident" (للإلحاق فقط أو كاشفٌ للعبث) — dangling predicate | minor | ambiguity-in-target |
| Limits | "no authority over **anyone else's** systems" | "no authority over systems **other than it**" (أنظمة غيرها) | minor | ambiguity-in-target |

**18 minor, 0 material.**

### Explanations (non-"none" findings)

1. **Header "rev1":** المراجعة denotes both "review" and "revision"; a reader could read "Review 1". Meaning of a version tag survives, so minor.
2. **Status "pending":** معلَّق without قيد covers both "pending" and "suspended"; standalone it leans "suspended" (work halted) rather than "pending" (awaiting). Minor mood shift, no action change.
3. **justice-as-cosmic-order:** نظام spans "order/system"; the hyphenated term of art tilts toward "system", softening the cosmic-moral "order" sense. Minor.
4. **load-bearing:** حمل إنشائي is the standard engineering collocation ("structural load"), so the correct reading dominates for technical readers; but إنشائي also reads "constitutive", leaving a possible "truth as a constitutive burden" misreading. Minor.
5. **web of dependences:** ارتباطات = connections/links; the dependency-tracking sense ("web of dependences" — who relies on what) is weakened to generic connectedness. Minor.
6. **decorum:** أدب المجلس = board/council manners — narrower than "decorum" (general seemliness), but inside the semantic field and the compliance-theater contrast survives. Minor.
7. **Added glosses:** The glosses are accurate, but they are interpretive additions not present in the source; a strict-translation reader receives extra theology. Minor.
8. **personhood (الشخصية):** الشخصية most commonly means "personality"; "personhood" (الشخصانية) is a secondary reading. Ubuntu's "shared personhood" could be misread as "shared personality". Minor.
9. **A1(b) واقعي:** primarily "realistic/pragmatic"; "factual" is a secondary sense. The verification condition could be misread as applying to "realistic" claims. Minor.
10. **post-hoc:** "after the fact" is re-rendered as "subsequent results"; temporality survives via لاحقة and the sense fits `outcome_check`, but the literal "post-hoc" framing is replaced by a results-paraphrase. Minor.
11. **stronger→strongest:** comparative becomes superlative; both mark `outcome_check` as the strictest applied check, so no action change. Minor.
12. **escrow:** no compact native equivalent; "does not hold value" loses the third-party-holding nuance but still conveys "the tool moves no money". Minor.
13. **keystone:** no single Arabic word carries the arch-metaphor; "chief stone" conveys centrality without it. Minor.
14. **trusted→trustworthy:** موثوق leans "reliable/credible" (agent property) vs "trusted" (others' stance); the aviation point survives. Minor.
15. **dividends:** أرباح = profits/earnings; "dividends" (توزيعات أرباح) as a payout mechanism is blurred, but the ownership-breadth list's intent survives. Minor.
16. **substrate:** no native philosophical "substrate"; ركيزة = pillar/foundation, which collides with the charter's "pillars" terminology and loses the "shared medium" sense. Minor.
17. **A5(a) grammar:** the (a) item is a prepositional fragment with no predicate ("for append-only or tamper-evident"); recoverable from context and list parallelism, but visibly broken. Minor.
18. **Limits "غيرها":** compressed pronoun leaves the comparison referent implicit; recoverable as "other systems / anyone else's", but an Arabic reader must supply it. Minor.

### Checked with no divergence found (severity none)

- Status/Derivation facts: red-team job id, 17/17 tests green 2026-10-23, day-03/04/07 anchors, cross-cultural term list — all present and correct.
- A1(a): status-on-its-face + four-way taxonomy (proven fact / attested output / model inference / prediction) — faithful; "the 2610.08144 lesson" retained.
- A1: certificate/proof MUST match the human-readable claim — faithful (درس 2610.08144 retained).
- A1 final line: "ineligible for bonding, ranking, or payment" — faithful (المجهول المصدر = unprovenanced).
- A2 spec hand-off list (bond sizing, challenger eligibility, adjudication, custody, payout enforcement → Day-4 spec file name) — faithful; red-team §A2 cross-ref retained.
- A2: L1 means "attestation format imposed, not bond market exists" — faithful.
- A3: informed-assent triad, strongest-rejected-alternative rule, "one action, not a menu", role-based signing, scapegoat, "The agent did it" is void — all faithful (كبش فداء is an exact native equivalent for scapegoat).
- A4: disclose list (beneficial owners, control-rights holders, concentration vs stated baseline with triggered review, tacit-knowledge contributors and compensation) — faithful; "enforced is the disclosure" retained.
- A5(b)/(c): completeness and replayability clauses, independent auditor, reconciliation vs real-world outcomes — faithful.
- A5: "Auditability is a compression problem, not a speed limit" — ضغط البيانات is the standard Arabic IT term for data compression; the literal back-translation ambiguity resolves to the correct reading.
- L0: costless-by-design starting line — faithful.
- L1: enforcement list (bondattest format, append-only audit log per action, signer of record, published disclosure) and the four outcome-trend metrics — faithful; red-test-is-a-violation and no-weakening-to-go-green retained.
- L2: Day-12 cadence + at least annually, written rationale + remediation/acceptance date, "open acceptance without a date ≠ resolved" — faithful; "targets L1 now, L2 by Day 12" and tools/-suite-green retained.
- Limits: no authority over other systems, not a legal instrument, no citing to silence criticism (adharma wearing dharma's clothes — ثوب robe for "clothes" is fine), publication is the human's call with Day-10 drafts.

## Untranslatable-term notes

- **escrow** — no single compact native equivalent (وديعة / حفظ لدى الغير are periphrases); rendered as تحتجز "holds in custody", losing third-party-holding nuance.
- **keystone** — no native arch-metaphor word; rendered الحَجَر الرئيس "chief stone" (centrality kept, metaphor dropped).
- **substrate** (philosophical sense) — no native equivalent; rendered الركيزة "pillar/foundation", which collides with the charter's "pillars" vocabulary.
- **personhood** — الشخصية doubles as "personality"; the precise philosophical term (الشخصانية) was not used.
- **dividends** — أرباح "profits/earnings"; exact term would be توزيعات أرباح.
- **load-bearing** — served adequately by the calque حمل إنشائي (standard engineering collocation for "structural load"), but with a residual "constitutive" reading.
- **append-only / tamper-evident / replayable** — calques (للإلحاق فقط / كاشف للعبث / قابل لإعادة المحاكاة); these are now standard Arabic IT register, no gap remains in practice.
- **outcome_check** — deliberately left as an untranslated code token per the translator's own glossary; consistent throughout.
- **red team / red-team** — no native term; loan-translation فريق الهجوم الأحمر used, unambiguous in context.
- **adharma / dharma** — transliterated (الدهارما / أدهارما); no native equivalent exists, as in every other language.
- **scapegoat** — exact native equivalent exists (كبش فداء, Qur'anic) and was correctly used.
- **instrument** (legal / instrumentation senses) — covered by وثيقة / أداة by context; no residual gap.

## VERDICT

VERDICT: faithful-with-notes


## Day-12 addendum (2026-10-26, DHARMA-13 Day-12 audit)
Source bumped to v0.1+rev2. This translation's A1(c), A2, and L1 sections still mirror
rev1 text (visible drift, disclosed in the rev2 notice atop CHARTER.ar.md); full
re-verification of those three sections is a Day-13 task. Header count/date refreshed:
19/19 tests green 2026-10-26.
- ar fix applied: `مسار الاستشارة القانونية`→`مسار المراجعة الاستشارية` (advisory review track; removes the unsupported legal-counsel characterization).


## Day-13 addendum (2026-10-27, DHARMA-13 Day-13 satya consolidation)
أُعيد ترجمة أقسام A1(c) وA2 وL1 وكتلة الحالة إلى نص الإصدار الإنجليزي 0.1+المراجعة 2؛
وحُدِّثت إشارة المراجعة 2 أعلى `../CHARTER.ar.md`. التحقق: **لم يُحصَّل الساق
المستقل** — انتهت مهلة استدعاء ask_kimi عند سقف الجسر (60 ثانية) (نمط الفشل المسجَّل
في اليوم الثاني عشر)؛ وقد استُنفدت ميزانية البحث الخارجي لليوم (probe + ساقا تحقق
fr/zh + هذا المهلة)، فلم يُعاد المحاولة. تحقق أحادي المشغّل (مرحلتان منفصلتان داخل
الجلسة): فُحصت كل فقرة من مصدر rev2 لوجود مقابل عربي (فحص التغطية). الدليل الكامل:
`roundtrip/ar.rev2-check.md`.
- الحالة → نسب المراجعة 2: حاضر (المعرّفان، المرحلتان، Cloudflare معلَّق). resolved
- نطاق A1(c) على مستوى الربط ({condition, verifier_ref, deadline}؛ full_validate عبر
  certify؛ التنفيذ واجب المشغّل): كامل. resolved
- ملاحظة الصدق الموسَّعة في A2 (evidence_ref حقل إلزامي؛ لا جلب للمخرجات ولا تحقق من
  البصمات؛ forfeit_split عملية توزيع حسابية لا تحويل؛ خلاصة مقيدة بالافتراضات مع
  المرجعين): كامل. resolved
- L1 التنفيذ المفصَّل لكل مادة + قوائم "غير مفروض" + مؤشرات اتجاهات النتائج + فقرة
  البسوط/العتبات: كامل. resolved
- متبقٍ: «الحَجَر الرئيس» لكلمة keystone (بند اليوم التاسع) كما هو.

VERDICT: **PASS WITH NOTES** — التغطية كاملة مقابل rev2؛ والملاحظة هي غياب ساق
الترجمة العكسية المستقلة (مهلة الجسر). تحقق أحادي المشغّل فقط.
