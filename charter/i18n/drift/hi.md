# Drift Report — CHARTER.hi.md (Hindi)

- **Language:** hi (Hindi) · translation file: `charter/i18n/CHARTER.hi.md` · back-translation: `charter/i18n/roundtrip/CHARTER.hi.back-en.md`
- **Date:** 2026-10-23
- **Method:** back-translated from translation alone, then diffed against source (`CHARTER.md`).
- Sections diffed: Status/Derivation, Preamble, A1, A2, A3, A4, A5, Conformance L0–L2, Limits. All 89 source lines were covered; every bold/italic shape and list item in the source has a counterpart in the translation.

## Findings

| Section | Source meaning (short quote) | Back-translated rendering | Severity | Cause |
|---|---|---|---|---|
| Title | "The Dharma Protocol for Agent Systems — Charter" | "Dharma-Protocol for Agent-Systems — Formal Covenant (Charter)" | minor | translator-choice: added gloss "विधिवत् संविदा"; original retained in parens |
| Status | "full critique in `day-08-codex-redteam.md`" | "full review in `day-08-codex-redteam.md`" | none | faithful (समीक्षा covers critique) |
| Status | "17/17 tests green" | "17/17 tests successful" | none | faithful |
| Derivation | "justice-as-cosmic-order" | "justice in the form of cosmic-order" | none | faithful |
| Preamble | "an order that makes truthfulness load-bearing" | "an order that makes honesty a load-bearer" | none | faithful (bold preserved) |
| Preamble | "ṛta, Ma'at's feather, asha against druj" | "ṛta, Ma'at's **side** (पक्ष), asha against druj" | **material** | translator-error: पक्ष = side/faction; feather = पंख |
| Preamble | bare terms: Ma'at, druj, asha, 天理, ubuntu | same terms + added glosses ("goddess of truth and justice", "falsehood", "order-of-truth", "heavenly justice-system", "shared humanity") | minor | translator-added glosses: accurate but expand the text beyond source |
| Preamble | "generation at scale with no price on being wrong" | "production at broad scale without paying any price for being wrong" | none | faithful |
| Preamble | "not decorum, not compliance theater" | "not politeness/etiquette, not compliance-drama" | none | faithful (near-equivalent) |
| A1 | "Truthful claims (satya)" | "honest-claims (truth)" | none | faithful |
| A1(a) | "proven fact, attested output, model inference, or forecast" | "proven fact, attested product, model-inference, or prediction" | minor | output→product slight narrowing (recurs in A2) |
| A1(c) | "pass a post-hoc `outcome_check`" | "pass a post-temporal check (उत्तर-कालीन) via `outcome_check`" | minor | non-standard calque; intent recoverable from context |
| A1 | "A certificate or proof attached to a claim MUST match" | "the certificate or proof … must match (ही चाहिए)" | none | faithful (deontic force kept) |
| A1 | "Unprovenanced content is ineligible" | "without-source content is ineligible" | none | faithful |
| A2 | "Bonded outputs" / "Every material agent output" | "bonded products" / "each significant agent-product" | minor | output→product; "material"→"significant" acceptable |
| A2 | "Bond sizing" | "bond-determination" | none | faithful |
| A2 | "payout enforcement" / "does not yet escrow value or execute payouts" | "payment-fidelity (भुगतान-निष्ठा)" in both places | minor | mechanism nuance softened: executing/enforcing payouts → "payment-fidelity" |
| A2 | "'attestation format enforced,' not 'bond market live'" | "'attestation-format implemented (लागू),' not 'bond-market active'" | minor | enforced→implemented softening |
| A2 | "(Pillar 1, the keystone; Ma'at's weighing.)" | "(Pillar 1, कुंजशिल; Ma'at's weighing.)" | minor | opaque/non-standard coinage for "keystone" (would be कुंजी-शिला) |
| A2 | "simplified discovery assumptions" | "simplified search-priors" | none | faithful |
| A3 | "Human ends, named signers" | "human-end(s), named signatories" | none | faithful (source phrase itself ambiguous; kept ambiguous) |
| A3 | "'The agent did it' is void" | "'The agent did it' — this is null and void" | minor | expansion (added "null"); same legal sense, no action change |
| A3 | "aviation's checklists made flight faster by making it trusted" | "aviation's checklists made flight fast by making it trustworthy" | minor | comparative "faster" lost; "trusted"→"reliable" |
| A3 | "rather than forcing a single scapegoat" | "instead of imposing a single sacrificial-goat (बलि-बकरा)" | none | faithful (native equivalent exists and is used) |
| A4 | "tacit knowledge trained the system" | "embedded knowledge-insight (निहित ज्ञान-सूझ)" | none | acceptable rendering |
| A4 | "Widening ownership … remains the preferred design" | "extension of ownership … remains the best design (सर्वोत्तम)" | minor | "preferred" strengthened to "best" |
| A4 | "personhood through the shared substrate" | "personhood through shared infrastructure" | none | acceptable adaptation |
| A5 | "human-legible rules" | "human-readable rules" | none | faithful |
| A5 | "replayable … reconciled against real-world outcomes where they exist" | "replayable … where real-world outcomes exist, matched against them" | none | faithful |
| A5 | "(Pillar 5; nomos/ius.)" | "(Pillar 5; nomos/ius — law and system-of-rights.)" | minor | added gloss (accurate) |
| L0 | "Costless by design" | "free by hypothesis (परिकल्पना-अनुसार)" | minor | by-design→by-hypothesis nuance |
| L1 | Level name "Instrumented" | "tool-enforced (उपकरण-प्रवर्तित)" | minor | level-name shift; internally consistent ("instrumentation theater"→"tool-theater") |
| L1 | "A red test is a violation" | "a red examination/test (लाल परीक्षण) is a violation" | minor | calque of test-suite jargon; recoverable from surrounding sentences |
| L1 | "not on instrumentation theater" | "not on tool-theater" | none | faithful |
| L1 | "The tools/ test suite must stay green" | "tools/ test-suite should stay green (चाहिए)" | none | faithful-ish (deontic kept) |
| L2 | "at least annually" / "does not count as resolved" / "targets L1 now, L2 by Day 12" | "at least once a year" / "not considered a solution" / "currently targets L1, L2 by Day 12" | none | faithful |
| Limits | "it is not a legal instrument" | "it is not any legal case-document/writ (विधिक वाद-पत्र)" | minor | वाद-पत्र is narrower (court pleading); intent preserved |
| Limits | "adharma wearing dharma's clothes" | "unrighteousness wearing dharma's garments" | none | faithful |
| Limits | "the human decides what ships" | "the human decides what will be published" | none | faithful |

## Explanations for non-"none" findings

1. **Preamble — Ma'at's feather → "Ma'at का पक्ष" (material).** पक्ष means side/faction/party; "feather" is पंख. The source's image is the feather of Ma'at — the standard in the weighing of the heart — and A2 later invokes "Ma'at's weighing (तौल)" with no preamble setup, leaving the Hindi text internally inconsistent about its own central cross-cultural metaphor (the document's stated Derivation is day-07 cross-cultural verification). A Hindi reader takes away "Ma'at's side/partisanship", a different model of the tradition than the source presents.
2. **Title gloss.** "विधिवत् संविदा (formal covenant)" is an addition, but "(चार्टर)" preserves the source word; no risk of misreading.
3. **Preamble added glosses.** Parenthetical explanations of Ma'at/druj/asha/天理/ubuntu are translator additions; all are accurate to day-07 usage; text expansion only.
4. **A1(a)/A2 output→product (उत्पाद).** "Output" is broader than "product"; every A2 obligation now reads as applying to products only. Borderline, kept minor because "material agent output" in context means deliverables.
5. **A1(c) "उत्तर-कालीन जाँच".** A non-standard compound (literally "post-temporal"); the intended "post-hoc/retrospective" sense is recoverable from the clause "where an outcome later materializes".
6. **A2 "भुगतान-निष्ठा" (payment-fidelity).** Used for both "payout enforcement" and "execute payouts"; the mechanism (actually running the payout) is abstracted into a quality of payments. Recoverable but less concrete than the source's honesty note intends.
7. **A2 "लागू" (implemented) for "enforced".** Slight softening inside an already-hedged honesty note; the L1 level name itself is correctly "प्रवर्तित" (enforced).
8. **A2 "कुंजशिल" for "the keystone".** Not a standard Hindi word (keystone = कुंजी-शिला / कीलक-पत्थर); likely a truncation/coinage. A Hindi reader cannot reliably recover "keystone"; the "load-bearing centrality" motif of the preamble is weakened.
9. **A3 "null and void".** Source says only "void"; harmless legal-doublet expansion.
10. **A3 aviation sentence.** Comparative "faster" becomes plain "fast (वेगवान)"; "trusted" becomes "reliable/trustworthy (विश्वसनीय)". Sense preserved, rhetorical force slightly reduced.
11. **A4 "preferred" → "best (सर्वोत्तम)".** Small strengthening; does not change the disclosure-focused recommendation.
12. **A5 added gloss** on nomos/ius ("law and system-of-rights") — accurate expansion.
13. **L0 "Costless by design" → "free by hypothesis".** परिकल्पना-अनुसार reads "according to hypothesis/assumption" rather than "by design"; slight shift in grounding of the claim.
14. **L1 level name "Instrumented" → "उपकरण-प्रवर्तित" (tool-enforced).** "Instrumented" (equipped with monitoring) becomes "enforced by tools"; the translation is internally consistent ("instrumentation theater" also becomes "tool-theater"), so no internal contradiction, but the level name's nuance shifts toward enforcement.
15. **L1 "लाल परीक्षण" for "a red test".** Calque of test-suite jargon; the following sentences (weakening the suite, going green) make the intended meaning recoverable.
16. **Limits "विधिक वाद-पत्र" for "legal instrument".** वाद-पत्र connotes a court pleading/writ — narrower than "legal instrument" — but "this is not a binding legal document" comes through.

## Untranslatable-term notes

Terms Hindi genuinely lacks a settled native equivalent for, and how the translation handled them:

- **"Charter" (as a governance document):** no exact native equivalent in this register; handled by descriptive gloss "विधिवत् संविदा" + retention of "चार्टर" in parentheses. Reasonable.
- **"Keystone" (arch metaphor):** standard term exists (कुंजी-शिला) but the translator coined "कुंजशिल", which is opaque. Needs correction, not a true untranslatable.
- **Test-suite jargon ("post-hoc", "red test", "go green"):** no native equivalents; handled by calques (उत्तर-कालीन, लाल परीक्षण, हरा) that are non-standard but recoverable in context. English glosses on first use would remove the residual ambiguity.
- **"Scapegoat":** native equivalent exists (बलि-बकरा, sacrificial goat) and is used correctly.
- **"Compliance theater" / "instrumentation theater":** calques (अनुपालन-नाटक, उपकरण-नाटक); these read naturally in Hindi.
- **"Load-bearing" (metaphorical):** calque (भारवाहक) that works.
- **"Substrate":** adapted to "आधारभूत-संरचना" (infrastructure) — an adaptation rather than a literal equivalent; acceptable here.
- **Technical tokens:** `outcome_check`, bondattest, file names, A1–A5, L0–L2 kept unaltered, as specified; "custody"/"escrow" kept with English glosses in parentheses — good practice.
- **Cross-cultural terms (ऋत, Ma'at, druj, asha, 天理, ubuntu, nomos/ius):** retained as-is with transliteration/glosses, matching the source's own practice.

## VERDICT

VERDICT: needs-revision

**Required fixes (material):**
1. Preamble, first sentence of the engine list: replace "Ma'at (मात — सत्य एवं न्याय की देवी) का पक्ष" with "Ma'at (मात — सत्य एवं न्याय की देवी) का पंख" — restoring "Ma'at's feather", the weighing image that A2's "Ma'at की तौल" presupposes.

**Strongly recommended (minor):**
2. A2 parenthetical: "कुंजशिल" → "कुंजी-शिला" (keystone).
3. A1(c): "उत्तर-कालीन जाँच" → "बाद की जाँच (post-hoc)" or "पश्च-परीक्षण" for a standard rendering.
4. L1: on first use, gloss "लाल परीक्षण" as "असफल (लाल) परीक्षण" to anchor the test-suite metaphor.
5. A2 honesty note: for "execute payouts", consider "भुगतान निष्पादित नहीं करता" instead of "भुगतान-निष्ठा नहीं करता" to keep the mechanism concrete.

Findings count: **1 material, 16 minor** (plus 20 sections/phrases checked with severity "none").

## Revision 2026-10-23

- `charter/i18n/CHARTER.hi.md`, Preamble (first sentence of the engine list): "Ma'at (मात — सत्य एवं न्याय की देवी) का पक्ष" → "Ma'at (मात — सत्य एवं न्याय की देवी) का पंख" — material fix; पक्ष means side/faction, feather is पंख; restores the weighing image that A2's "Ma'at की तौल" presupposes.
- `charter/i18n/CHARTER.hi.md`, A2 parenthetical: "कुंजशिल" → "कुंजी-शिला" — opaque/non-standard coinage for "keystone"; report's recommended minor fix #2.
- `charter/i18n/CHARTER.hi.md`, A1(c): "उत्तर-कालीन जाँच" → "बाद की जाँच (post-hoc)" — non-standard calque (literally "post-temporal") that misleads; report's recommended minor fix #3 (first of its two offered alternatives, per the report's own note favoring English glosses on first use).
- `charter/i18n/CHARTER.hi.md`, L1: "लाल परीक्षण एक उल्लंघन है" → "असफल (लाल) परीक्षण एक उल्लंघन है" — glosses the test-suite calque on first use to anchor the metaphor; report's recommended minor fix #4.
- `charter/i18n/CHARTER.hi.md`, A2 honesty note ("execute payouts" instance only): "भुगतान-निष्ठा नहीं करता" → "भुगतान निष्पादित नहीं करता" — keeps the payout mechanism concrete instead of abstracting it to payment-fidelity; report's recommended minor fix #5.

Left unchanged (observations with no concrete correction offered, or explicitly judged acceptable/recoverable by the report): title gloss "विधिवत् संविदा"; Preamble/A5 added glosses on cross-cultural terms; output→product (उत्पाद) narrowing in A1(a)/A2; "लागू" for "enforced" in the A2 honesty note; A3 "null and void" expansion and lost comparative in the aviation sentence; A4 "preferred"→"सर्वोत्तम" strengthening; L0 "परिकल्पना-अनुसार"; L1 level-name shift "उपकरण-प्रवर्तित"; Limits "विधिक वाद-पत्र". The glossary HTML comment was not touched because no glossary-listed key term changed. No conflict between report fixes and the file's established glossary.

REVISION STATUS: material fix applied

## Re-verification 2026-10-23

Method: back-translated the revised target text of the touched sections only (Preamble, A1(c), A2, L1) into English literally, from the revised Hindi alone (`charter/i18n/roundtrip/hi.rev-check.md`), then checked each revised passage against the source (`CHARTER.md`) and diffed against the Pass-1 back-translation to catch collateral edits.

Per-change verdicts:

1. **Preamble पक्ष → पंख (material): resolved.** Revised text reads "Ma'at (मात — सत्य एवं न्याय की देवी) का पंख"; पंख = feather, so "Ma'at's feather" is restored verbatim. Internal consistency with A2's "Ma'at की तौल" (Ma'at's weighing) is now established — the weighing image has its setup. No other preamble sentence was altered (bold load-bearing clause, glosses, engine order all intact).
2. **A2 कुंजशिल → कुंजी-शिला (minor #2): resolved.** कुंजी-शिला is the standard keystone term; back-translation yields "(Pillar 1, key-stone/keystone; Ma'at's weighing.)" — faithful to source.
3. **A1(c) उत्तर-कालीन जाँच → बाद की जाँच (post-hoc) (minor #3): resolved.** Back-translation: "pass a later check (post-hoc) through `outcome_check`" — faithful to "pass a post-hoc `outcome_check`"; the non-standard "post-temporal" calque is gone, the source's `outcome_check` token and the parenthetical "(this stronger check … not optional)" are intact.
4. **L1 लाल परीक्षण → असफल (लाल) परीक्षण (minor #4): resolved.** Back-translation: "A failed (red) test is a violation" — an accurate anchoring gloss for the test-suite calque "a red test", exactly as recommended; sentence structure and the go-green sentence untouched.
5. **A2 honesty note भुगतान-निष्ठा नहीं करता → भुगतान निष्पादित नहीं करता (minor #5): resolved.** Back-translation: "it does not yet protect value (escrow) or execute payouts" — matches "does not yet escrow value or execute payouts"; the mechanism is concrete again.

New-drift findings: **none.** Each edit word was checked in isolation (पंख, बाद की जाँच, कुंजी-शिला, निष्पादित, असफल (लाल)) and reads cleanly in context; all other wording in the touched sections matches the Pass-1 renderings already vetted in this report. Structure/numbering/tokens in touched sections intact: Preamble bold "**एक ऐसा क्रम जो सत्यनिष्ठा को भारवाहक बनाता है**" preserved; A1(c) marker and `outcome_check` code token preserved; A2 italic parenthetical, §A2, and file paths preserved; L1 bullet structure and bold **परिणाम-प्रवृत्तियों** preserved.

Residue notes (all pre-existing items the report itself accepted or scoped out — no action required):
- A2's first instance, source "payout enforcement", remains "भुगतान-निष्ठा" (payment-fidelity); the report's recommendation #5 deliberately targeted only the "execute payouts" instance, so this is per-spec.
- Accepted residues from the report's "left unchanged" list persist (title gloss, "लागू" for "enforced" in the honesty note, L1 level-name shift "उपकरण-प्रवर्तित", etc.).

RE-VERIFICATION: PASS WITH NOTES


## Day-12 addendum (2026-10-26, DHARMA-13 Day-12 audit)
Source bumped to v0.1+rev2. This translation's A1(c), A2, and L1 sections still mirror
rev1 text (visible drift, disclosed in the rev2 notice atop CHARTER.hi.md); full
re-verification of those three sections is a Day-13 task. Header count/date refreshed:
19/19 tests green 2026-10-26.
- hi fixes applied: `भुगतान-निष्ठा`→`भुगतान-प्रवर्तन` (payout ENFORCEMENT, per source); `सर्वोत्तम डिज़ाइन`→`अधिमान्य डिज़ाइन` (preferred, not best).


## Day-13 addendum (2026-10-27, DHARMA-13 Day-13 satya consolidation)
A1(c), A2, L1 तथा स्थिति-खंड को अंग्रेज़ी v0.1+rev2 पाठ पर पुनः अनुवादित किया गया;
`../CHARTER.hi.md` के शीर्ष पर rev2 सूचना अद्यतन। सत्यापन: **स्वतंत्र चरण प्राप्त नहीं** —
ask_kimi ब्रिज कॉल ब्रिज की 60s सीमा पर समयबाह्य (दिन-12 के दर्ज विफलता-रूप); दिन का
बाह्य-lookup बजट probe + fr/zh सत्यापन-चरणों + इस समयबाह्य से समाप्त, अतः पुनः प्रयास नहीं।
एक-संचालक सत्यापन (session में पृथक pass): अंतिम हिन्दी पाठ की प्रत्येक rev2 source
clause के लिए कवरेज-जाँच। पूर्ण साक्ष्य: `roundtrip/hi.rev2-check.md`।
- स्थिति → rev2 वंश: उपस्थित (दोनों job ID, दोनों चरण, Cloudflare लंबित)। resolved
- A1(c) बाइंडिंग-स्तर दायरा ({condition, verifier_ref, deadline}; full_validate,
  certify द्वारा; संचालक-कर्तव्य निष्पादन): सम्पूर्ण। resolved
- A2 विस्तृत सत्यनिष्ठा-टिप्पणी (evidence_ref अनिवार्य क्षेत्र; कोई आर्टिफैक्ट-प्राप्ति/
  हैश-सत्यापन नहीं; forfeit_split = आवंटन-अंकगणित; पूर्वधारणा-बद्ध निष्कर्ष, दोनों संदर्भ):
  सम्पूर्ण। resolved
- L1 प्रति-अनुच्छेद प्रवर्तन + "प्रवर्तित नहीं" सूचियाँ + परिणाम-प्रवृत्ति मेट्रिक्स +
  हर/सीमा-मान खंड: सम्पूर्ण। resolved
- शेष: L1 सोपान-नाम "उपकरण-प्रवर्तित" (दिन-9 अवशिष्ट) यथावत्।

VERDICT: **PASS WITH NOTES** — rev2 के विरुद्ध कवरेज सम्पूर्ण; नोट = स्वतंत्र
back-translation चरण अनुपलब्ध (ब्रिज टाइमआउट)। केवल एक-संचालक सत्यापन।
