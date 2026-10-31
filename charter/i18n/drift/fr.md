# Drift report — CHARTER.fr.md (French)

- Language: fr (French)
- Date: 2026-10-23
- Method: back-translated from translation alone, then diffed against source
- Back-translation: `charter/i18n/roundtrip/CHARTER.fr.back-en.md`
- Source: `CHARTER.md` (v0.1+rev1, 2026-10-23)

## Findings

| # | Section | Source meaning (short quote) | Back-translated rendering | Severity | Cause |
|---|---------|------------------------------|---------------------------|----------|-------|
| 1 | Status | "Draft; not published" | "Project; unpublished" (Projet ; non publié) | minor | faithful |
| 2 | Preamble | "an order that makes truthfulness **load-bearing**" | "an order that makes truth-bearing" (rend la véracité porteuse) | minor | ambiguity-in-target |
| 3 | Preamble | "ṛta, Ma'at's feather, asha against druj, 天理, ubuntu's shared personhood" (bare list) | same terms, each with an added gloss: "(cosmic order)", "(truth, balance, order)", "(order-truth)", "(the lie)", "(Principle of Heaven)", "(I am because we are)" | minor | untranslatable-term |
| 4 | Preamble | "Dharma here means duty-appropriate conduct…" | "Dharma (dharma: right conduct, duty) here denotes…" | minor | untranslatable-term |
| 5 | Preamble | "the agents and artifacts under its control" | "under his control" (placés sous son contrôle) | none | faithful |
| 6 | A1 | "proven fact" | "established fact" (fait établi) | none | faithful |
| 7 | A2 | "'attestation format **enforced**,' not 'bond market live'" | "'attestation format **applied**,' not 'bond market in service'" (appliqué / en service) | minor | translator near-equivalence |
| 8 | A3 | "(a) **informed assent**" | "(a) has given his **informed consent**" (consentement éclairé) | minor | translator near-equivalence |
| 9 | A3 | "aviation's checklists made flight faster by making it **trusted**" | "…by making it **reliable**" (en le rendant fiable) | minor | faithful |
| 10 | A3/A4 | "ubuntu's shared **personhood**" / "**personhood** through the shared substrate" | "the shared **person**" (la personne partagée) / "the **person** through the shared substrate" | minor | untranslatable-term |
| 11 | A5 | "*(Pillar 5; nomos/ius.)*" | "*(Pillar 5; nomos/ius — the law, the right.)*" | minor | untranslatable-term |
| 12 | A5 | "Agent-to-agent **deals** execute under…" | "Agent-to-agent **transactions** execute according to…" (transactions d'agent à agent) | none | faithful |
| 13 | A3 | "(b) **live authority** to halt the agent" | "(b) holds **permanently** the halt authority" (détient en permanence le pouvoir d'arrêter) | none | faithful |
| 14 | L1 | "A1–A5 **enforced** by tooling in the loop" | "A1–A5 **applied** by the tooling in the loop" (appliquées) | minor | translator near-equivalence |
| 15 | L1 | "ownership disclosure published" | "property revelation published" (révélation des propriétés publiée) | minor | ambiguity-in-target |
| 16 | L2 | "every accepted finding carries … a remediation **or acceptance** deadline" | "…a deadline for remediation or for acceptance" (un délai de remédiation ou d'acceptation) | none | faithful |
| 17 | Post-L2 | "targets L1 now, **L2 by Day 12**" | "targets L1 now, **L2 for day 12**" (le L2 pour le jour 12) | minor | translator near-equivalence |
| 18 | Limits | "the human decides what **ships**" | "the human decides what is **delivered**" (ce qui est livré) | none | faithful |

Explanations (all non-"none" findings):

1. French document register uses "projet" for an unpublished draft text ("projet de loi" = draft bill), so a French reader recovers "draft" exactly; only the literal English echoes "project".
2. French "porteuse" drops the complement ("load-bearing" = *porteuse de poids/charge*); alone it can read "makes truth fruitful/meaningful" (*porteuse de sens*). The structural metaphor is slightly blurred but the sense survives.
3. The glosses add information absent from the source (druj = "the lie", 天理 = "Principle of Heaven", ubuntu = "I am because we are"). Helpful for a francophone reader; nothing is removed or contradicted.
4. Added parenthetical gloss "(dharma: right conduct, duty)" — same class as #3.
7. "Enforced" carries compulsion nuance; "appliqué" is the milder "applied". In a tooling context the practical reading is identical, but the obligation tone is softened (recurs in #14).
8. "Consentement éclairé" is the standard French collocation; French has no common native term preserving the source's deliberate assent/consent distinction ("assentiment" exists but reads as intellectual agreement, not a fix). The legalistic tint of "consent" is imported.
9. "Fiable" derives from *faire confiance* (to trust) and spans English "reliable" and "trustworthy"; the English reader's "reliable" is the narrower half of the French term, not a true loss.
10. "Personhood" has no clean French noun ("personnalité" = personality, misleading; "qualité de personne" is clunky); flattened to "la personne", which can momentarily read as "a shared person" rather than "shared personhood".
11. Added gloss "— the law, the right" not present in source; same class as #3/#4.
14. Same enforced→applied softening as #7, in the L1 definition.
15. Plural "des propriétés" can momentarily read as "attributes/properties" rather than "ownership"; the A4 anchor ("Transparence de la propriété") resolves it in context.
17. "By Day 12" sets a deadline (no later than); "pour le jour 12" sets a target date. Here day 12 is the scheduled red-team day, so the practical reading coincides.

Checked with no divergence found: title/version/date; Status block (Codex job id, Cloudflare note, `day-08-*` file names); Derivation list (all seven cross-cultural terms, 17/17 tests, day references); A1 all three clauses + MUST + 2610.08144 + Pillar-4 tag; A2 attestation fields, honesty note, red-team §A2, "keystone", "Ma'at's weighing"; A3 scapegoat/"the agent did it" is void/friction sentence structure; A4 all three disclosure items, baseline-trigger, preferred design, "instead of mute"; A5 clauses (a)–(c), compression/speed-limit sentence; L0 wording; L1 metrics list (false-claim rate, challenger success, signer interventions, concentration deltas), red-test/weaken-the-suite sentences; L2 red-team cadence, "openly accepted" without deadline; Limits (no authority over others' systems, not a legal instrument, adharma line, publication is the human's call). MUST/DOIT force preserved everywhere; A1–A5 / L0–L2 / outcome_check / tools/bondattest.py unchanged.

## Untranslatable-term notes

- **Cross-cultural lexicon** (dharma, ṛta, Ma'at, asha, druj, 天理, ubuntu, svadharma, adharma, nomos/ius): transliterated/kept as in the source; French has no native equivalents by definition. Handled by keeping the terms and adding short explanatory glosses at first use (findings 3, 4, 11).
- **personhood**: no compact native French noun; rendered "la personne" (finding 10).
- **informed assent**: French lacks a live assent/consent distinction; rendered with the standard "consentement éclairé" (finding 8).
- **bond / bonding**: native equivalent exists — "caution" / "cautionnement" (legal-financial term) — correctly used.
- **append-only / tamper-evident / replayable / red-team**: "en ajout uniquement", "à détection de falsification", "rejouable" are accepted native/calqued equivalents; "red-team" borrowed as-is, standard in French security usage.
- **load-bearing (metaphor)**: "porteuse" without complement (finding 2).

## VERDICT

VERDICT: faithful-with-notes


## Day-12 addendum (2026-10-26, DHARMA-13 Day-12 audit)
Source bumped to v0.1+rev2. This translation's A1(c), A2, and L1 sections still mirror
rev1 text (visible drift, disclosed in the rev2 notice atop CHARTER.fr.md); full
re-verification of those three sections is a Day-13 task. Header count/date refreshed:
19/19 tests green 2026-10-26.
- fr fixes applied: `Projet`→`Brouillon` (draft status); `révélation`→`divulgation` (A4 disclosure); L2 heading `Revue contradictoire`→`Revue hostile (red-team)` (closer to adversarial security review).


## Day-13 addendum (2026-10-27, DHARMA-13 Day-13 satya consolidation)
A1(c), A2, L1, and the Status block re-translated to the English v0.1+rev2 text; rev2
notice atop `../CHARTER.fr.md` updated. Verification: independent leg — cold
back-translation via agent-bridge ask_kimi of the four sections, then clause-by-clause
diff vs the rev2 source. Full evidence: `roundtrip/fr.rev2-check.md`.
- Status → rev2 lineage: recovered (job IDs, legs, Cloudflare pending). resolved
- A1(c) binding-level scope ({condition, verifier_ref, deadline}; full_validate via
  certify; operator-duty execution): all clauses recovered. resolved
- A2 extended honesty note (evidence_ref enforced; no fetch/hash verification;
  forfeit_split = arithmétique de répartition; assumption-bound verdict, both refs):
  all elements recovered. resolved
- L1 scoped per-article enforcement + not-enforced lists + outcome-trend metrics +
  denominators/thresholds clause: recovered. resolved
- Verifier [amb] notes (dispositions; découvertes simplifiées; cautionnement) are
  judgment calls, none action-changing.

VERDICT: **PASS** (independent leg). No material drift.
