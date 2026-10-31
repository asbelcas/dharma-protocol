# Re-verification 2026-10-27 (Day 13) — sw — A1(c)/A2/L1/Status to rev2 + accepted-open items

Method: Day-12 handoff task (incl. both sw accepted-open items). Pass A (re-translation
to rev2 + term fixes): driver session (kimi-cli Day 13), glossary-bound per the file's
key-terms header. Pass B (independent back-translation leg): **not run** — external-lookup
budget for the day was consumed by the probe + the fr/zh verification legs + the hi/ar
timeouts (see day-13-synthesis.md, boundary record). Pass B′ (single-operator
verification, this file): the driver re-read the final Swahili text cold and checked every
rev2 source clause for a Swahili counterpart (coverage check), passes separated within the
session. Weaker than an independent leg — recorded, not hidden.

## Accepted-open items from the Day-12 addendum — both cleared

1. **A3(c) `udhibiti wa sababu halisi`** (rendered "control of the real cause"; source =
   "real causal control") → replaced with the sense-based rendering **"udhibiti
   unaosababisha kwa kweli kile wakala anachofanya"** ("control that truly causes what the
   agent does"). **resolved**
2. **L1 `vingilio vya wasaini`** (signer interventions) → the L1 section was re-translated
   to rev2 text; the metric now reads **"uingiliaji wa wasaini"** — intervention BY
   signers, distinct from the A5 tamper-gloss "inayobainisha uingiliaji wowote"
   (interference WITH the log); the collocation is disambiguated by agent and context.
   **resolved**

## Clause-coverage check vs rev2 source (Swahili counterpart → verdict)

STATUS: rev2 lineage + independent/mechanical legs + `day-12-audit.md` + rev1/day-8
lineage + Cloudflare pending + draft scope → **present** (rev2 baada ya ukaguzi kamili wa
kanzu la siku ya 12… kiwango huru… kusoma tu; kiwango cha kimitambo… / Kabla ya hapo rev1…
imezuiwa… inasubiri / Rasimu; haijachapishwa).

A1(c): post-hoc `outcome_check` ✓ ("lipite `outcome_check` ya baada-ya-tukio"); binding
level → "kwenye kiwango cha ufungo" ✓; invalid unless {condition, verifier_ref, deadline}
→ "ithibati ni batili isipokuwa imebeba {condition, verifier_ref, deadline}" ✓;
full_validate via certify → "(`full_validate`, inayotumika kupitia `certify`)" ✓;
execution at maturity = operator's duty → "kutekeleza ukaguzi wakati matokeo yamekomaa ni
wajibu wa mwenye shughuli" ✓; not optional → "ufungo si wa hiari" ✓; not automatable by a
format checker → "utekelezaji hauwezi kufanywa kwa otomatiki na kikaguzi cha muundo" ✓.
**complete**

A2: five attestation fields ✓; day-4 spec reference ✓; format-only claim ✓ ("ni *muundo*
wa ithibati"); evidence_ref enforced field ✓ ("ni uwanja lazima (`evidence_ref`)"); no
artifact fetch / no external hash verification ✓ ("hakuna kinachokwenda kuchukua vifaa au
kuthibitisha hash dhidi ya vyanzo vya nje"); forfeit_split allocation arithmetic, not
transfer ✓ ("ni hesabu ya mgawanyo tu, si uhamisho"); assumption-bound verdict with
red-team §A2 + Day-12 audit refs ✓; no escrow/no payouts ✓; L1-meaning sentence ✓.
**complete**

L1: "format layer of each article — no more" ✓ ("tabaka la muundo wa kila kifungu —
zaidi ya hayo hapana, na ngazi hii haaidai zaidi ya hayo"); A1 labels + certify rejection
+ not-enforced truth/execution ✓; A2 records + not-enforced identity/custody/adjudication/
payouts ✓; A3 signer-of-record entry + not-enforced competence/halt ✓; A4 published dated
disclosure + not-enforced accuracy ✓; A5 hashchain verify() recomputes/detects +
completeness + operator-logger sentence ✓; four metrics incl. **uingiliaji wa wasaini** ✓;
denominators (viwango vya sehemu ya chini) / thresholds (vile vya kuvuka) at adoption, not
retroactive, Day-13 deadline ✓; not instrumentation theater ✓; red-test rule ✓.
**complete**

## Notes / residues

- R2-class residue stands (Day-12 judgment call): A2 title **Matokeo yaliyodhamanishwa**
  keeps *matokeo/tokeo* for "outputs"; general Swahili also reads *matokeo* as
  outcomes/income — the revenue reading is avoided per the Day-12 fix, the
  outcome-collision is accepted and now tested in-context (A1(c) uses "matokeo
  yatachipuka" for outcomes; A2 body uses "tokeo muhimu la wakala" for outputs). Watch
  item for any future re-translation.
- A2 "kielezi cha ushahidi" (descriptor for pointer) — Day-9 judgment-call item, still
  standing, permitted by that report.
- Code tokens verbatim: {condition, verifier_ref, deadline}, full_validate, certify,
  evidence_ref, forfeit_split, hashchain, verify().

VERDICT: **PASS WITH NOTES** — accepted-open items cleared, coverage complete against
rev2; single-operator verification only (no external leg remaining in budget).
