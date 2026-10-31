# Charter i18n — DHARMA-13 Day 9 (2026-10-23)

Source: `../CHARTER.md` (Dharma Protocol for Agent Systems v0.1+rev1, English).
Translations below are complete (no omissions), structurally equivalent to the
source in section shape (line counts differ by language), and carry per-language
round-trip verification.

## Method (round-trip, pass-separated)
1. **Pass A — translation.** A dedicated agent translated the source cold, with a
   per-language key-term glossary (HTML comment atop each file) and strict
   keep-as-is tokens: article codes A1–A5, conformance levels L0–L2, file names,
   `outcome_check`, and the cross-cultural terms (ṛta, Ma'at, asha, druj, 天理,
   ubuntu, nomos/ius, svadharma, adharma).
2. **Pass B — back-translation.** A *different* agent, given only the translation
   file, rendered it back into English literally (`roundtrip/CHARTER.<code>.back-en.md`),
   marking genuine target-side ambiguities inline rather than smoothing them.
3. **Pass C — drift report.** The same verifier then read the source and diffed
   section by section: `drift/<code>.md` holds a findings table with severity
   (none/minor/material), cause, untranslatable-term notes, and a verdict.
4. **Remediation + re-verification.** Verdicts of `needs-revision` were fixed the
   same day (revision section appended to the drift report = audit trail), then a
   fresh agent re-verified only the touched sections (`roundtrip/<code>.rev-check.md`,
   `## Re-verification 2026-10-23` in the drift report).

Channel: all passes run on ask_kimi (free alliance channel); zero paid-bot burns.
Boundaries honored: no accounts, no posting, no external lookups.

## Index

| Code | Language | File | Round-trip | Drift report | Verdict |
|------|----------|------|-----------|--------------|---------|
| fr | français | `CHARTER.fr.md` | `roundtrip/CHARTER.fr.back-en.md` | `drift/fr.md` | faithful-with-notes (0 material, 12 minor) |
| zh | 简体中文 | `CHARTER.zh.md` | `roundtrip/CHARTER.zh.back-en.md` | `drift/zh.md` | faithful-with-notes (0 material, 5 minor) |
| hi | हिन्दी | `CHARTER.hi.md` | `roundtrip/CHARTER.hi.back-en.md` + `hi.rev-check.md` | `drift/hi.md` | needs-revision → **re-verified PASS WITH NOTES** (material fix: Ma'at's feather पक्ष→पंख) |
| ar | العربية الفصحى | `CHARTER.ar.md` | `roundtrip/CHARTER.ar.back-en.md` | `drift/ar.md` | faithful-with-notes (0 material, 18 minor) |
| sw | Kiswahili | `CHARTER.sw.md` | `roundtrip/CHARTER.sw.back-en.md` + `sw.rev-check.md` | `drift/sw.md` | needs-revision → **re-verified PASS WITH NOTES** (material fix: A3 scapegoat idiom) |
| es | Español | `CHARTER.es.md` | `roundtrip/CHARTER.es.back-en.md` | `drift/es.md` | faithful-with-notes (0 material, 4 minor) |

## Cross-language drift patterns (from the six reports)
- **Added glosses**: every translation adds short native glosses on first use of the
  cross-cultural terms — additions, never removals; judged faithful throughout.
- **Obligation softening**: "enforced"/"MUST" occasionally lands softer
  (appliqué, लागू, implied modality). Watched; none reached material.
- **Untranslatable terms** (documented per language): keystone, escrow, substrate,
  personhood, dividends, scapegoat (Swahili — fixed with sense + gloss),
  "instrumented" as a level name.
- **Comparative→superlative** slip appeared in three languages (A1(c) "the stronger
  check"); all instances pinned by context, noted for Day-12 audit.

## Status
All six translations verified; two material findings found and remediated same-day;
zero outstanding material drift. Ready for Day 10 (publish drafts, human-gated).

## Day-12 addendum (2026-10-26, full-corpus audit)
- English source is now **v0.1+rev2**. The six translations' A1(c), A2, and L1 sections
  mirror rev1 text — disclosed as visible drift in the rev2 notice atop each translation;
  re-verification of those three sections is a Day-13 task (per the charter's L2
  acceptance-deadline rule).
- Header count/date refreshed in all six files: 19/19 tests green 2026-10-26 (was 17/17,
  2026-10-23). The count is the whole tools/ suite; the Day-12 audit replaced two vacuous
  tamper tests with real ones and added two certification tests.
- Term-level fixes applied per language (logged in each `drift/<code>.md` Day-12
  addendum): fr, zh, ar, hi, sw, es.
- ~~Accepted-open with Day-13 deadline: sw A3 `udhibiti wa sababu halisi` + L1
  `vingilio vya wasaini`; es `resultado` output/outcome disambiguation; rev2 section
  re-verification (all languages).~~ **Cleared 2026-10-27 (Day 13)** — see the Day-13
  addendum below.
- `drift/` and `roundtrip/` evidence directories now ship in the publish bundle
  (absolute local paths sanitized 2026-10-26).


## Day-13 addendum (2026-10-27, satya consolidation)
All six translations' **A1(c), A2, L1, and Status** sections now mirror the English
v0.1+rev2 text (the rev2 notice atop each file updated accordingly). The three
accepted-open items are **cleared**: sw A3(c) `udhibiti wa sababu halisi` → sense-based
`udhibiti unaosababisha kwa kweli`; sw L1 `vingilio vya wasaini` → `uingiliaji wa wasaini`
(in the re-translated L1); es `resultado` disambiguated (`salida` for outputs in A1(a) and
the A2 title; `resultado` kept for outcomes — verified by grep).

Verification record (method and limits, honestly):
- **fr, zh — independent leg PASS.** Cold back-translation via agent-bridge ask_kimi
  (single-file reads), then clause-by-clause diff vs rev2. Evidence:
  `roundtrip/fr.rev2-check.md`, `roundtrip/zh.rev2-check.md`.
- **hi, ar, sw, es — PASS WITH NOTES (single-operator).** The independent leg was not
  obtainable within the day's ≤5 external-lookup boundary: two ask_kimi batches were
  policy-blocked, the hi and ar single-language calls timed out at the bridge's 60s cap
  (Day-12 failure mode, documented). The driver re-verified these four in-session with
  translation and verification passes separated (clause-coverage check against rev2).
  Evidence: `roundtrip/{hi,ar,sw,es}.rev2-check.md`. Per the charter's L2 rule this
  weaker method is disclosed in each file rather than upgraded to "independent".
- Structural tokens (A1–A5, L0–L2, `outcome_check`, `evidence_ref`, `forfeit_split`,
  `full_validate`, `certify`, `hashchain`, `verify()`, {condition, verifier_ref,
  deadline}) verified verbatim in all six files.

Remaining known residues (all previously permitted judgment calls, logged in the
respective Day-13 addenda): sw A2-title `Matokeo`/`tokeo` output-outcome adjacency
(Day-12 fix retained, watched in-context); sw `kielezi cha ushahidi`; es `clasificación`
for ranking; hi L1 level name `उपकरण-प्रवर्तित`; ar keystone «الحَجَر الرئيس».
