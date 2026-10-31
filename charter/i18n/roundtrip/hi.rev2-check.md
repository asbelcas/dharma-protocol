# Re-verification 2026-10-27 (Day 13) — hi — A1(c)/A2/L1/Status to rev2

Method: Day-12 handoff task. Pass A (re-translation to rev2): driver session (kimi-cli Day 13),
glossary-bound per the file's key-terms header. Pass B (independent back-translation leg):
**not obtained** — the ask_kimi bridge call timed out at the bridge's 60s cap (same failure
mode documented Day 12). External-lookup budget for the day was consumed by the probe + the
fr/zh verification legs + this timeout (see day-13-synthesis.md, boundary record), so the
remaining languages were not retried. Pass B′ (single-operator verification, this file):
the driver re-read the final Hindi text cold and checked every rev2 source clause for a
Hindi counterpart (coverage check), passes separated within the session. Weaker than an
independent leg — recorded, not hidden.

## Clause-coverage check vs rev2 source (Hindi counterpart → verdict)

STATUS: rev2 lineage + independent/mechanical legs + `day-12-audit.md` + rev1/day-8
lineage + Cloudflare pending + draft scope → **present** (दिन-12 के पूर्ण-संकलन
लेखा-परीक्षण… केवल-पठन… यांत्रिक चरण… के पश्चात् rev2 / उससे पहले rev1 / अवरुद्ध — लंबित /
मसौदा; अप्रकाशित).

A1(c): post-hoc `outcome_check` → "(c) …वहाँ `outcome_check` से बाद की जाँच (post-hoc)
गुजरे" ✓; binding-level enforcement → "संदर्भ-उपकरण इसे बाइंडिंग-स्तर पर प्रवर्तित करता है" ✓;
invalid unless {condition, verifier_ref, deadline} → "जिस प्रमाणन में {condition,
verifier_ref, deadline} अंकित न हों, वह अमान्य है" ✓; full_validate applied by certify →
"(`full_validate`, `certify` द्वारा लागू)" ✓; execution at maturity = operator's duty →
"परिणाम के परिपक्व होने पर जाँच का संचालन संचालक का कर्तव्य है" ✓; not optional →
"बाइंडिंग वैकल्पिक नहीं" ✓; not automatable by format checker → "संचालन कोई प्रारूप-जाँचक
स्वचालित नहीं कर सकता" ✓. **complete**

A2: five attestation fields ✓; day-4 spec reference ✓; format-only claim ✓; evidence_ref
enforced field ✓ ("अनिवार्य क्षेत्र"); no artifact fetch / no external hash verification ✓
("न तो आर्टिफैक्ट प्राप्त करता है, न ही बाह्य स्रोतों के विरुद्ध हैश मिलाता है");
forfeit_split allocation arithmetic, not transfer ✓ ("आवंटन-अंकगणित मात्र है, हस्तांतरण
नहीं"); assumption-bound verdict with red-team §A2 + Day-12 audit refs ✓ ("अपनी
पूर्वधारणाओं से बंधा है … रेड-टीम §A2 तथा दिन-12 लेखा-परीक्षण"); no escrow/no payouts ✓;
L1-meaning sentence ✓. **complete**

L1: "format layer of each article — no more" ✓ ("प्रारूप-स्तर … और कुछ नहीं, और यह
सोपान इतना ही दावा करता है"); A1 labels + certify rejection + not-enforced truth/execution ✓;
A2 records + not-enforced identity/custody/adjudication/payouts ✓; A3 signer-of-record +
not-enforced competence/halt ✓; A4 published dated disclosure + not-enforced accuracy ✓;
A5 hashchain verify() recomputes/detects + completeness + operator-logger sentence ✓;
four outcome metrics ✓; denominators(हर)/thresholds(सीमा-मान) at adoption, not retro-fitted,
Day-13 deadline ✓; not instrumentation theater ✓; red-test rule ✓. **complete**

## Notes / residues

- "हर" for denominator and "सीमा-मान" for threshold are standard Hindi mathematical usage;
  no better native term exists in register.
- L1 level name "उपकरण-प्रवर्तित" (Day-9 residue, previously permitted) retained.
- Code tokens verified verbatim in file: {condition, verifier_ref, deadline}, full_validate,
  certify, evidence_ref, forfeit_split, hashchain, verify().

VERDICT: **PASS WITH NOTES** — coverage complete against rev2; the missing independent
back-translation leg (bridge timeout) is the note. Single-operator verification only.
