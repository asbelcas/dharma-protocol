# Re-verification 2026-10-27 (Day 13) — es — A1(c)/A2/L1/Status to rev2 + accepted-open item

Method: Day-12 handoff task (incl. the es accepted-open item). Pass A (re-translation to
rev2 + disambiguation): driver session (kimi-cli Day 13), glossary-bound per the file's
key-terms header. Pass B (independent back-translation leg): **not run** — external-lookup
budget for the day was consumed by the probe + the fr/zh verification legs + the hi/ar
timeouts (see day-13-synthesis.md, boundary record). Pass B′ (single-operator
verification, this file): the driver re-read the final Spanish text cold and checked every
rev2 source clause for a Spanish counterpart (coverage check), passes separated within the
session. Weaker than an independent leg — recorded, not hidden.

## Accepted-open item from the Day-12 addendum — cleared

1. **`resultado` covering both output and outcome** → disambiguation pass applied:
   - A1(a) "attested output": ~~resultado atestado~~ → **"salida atestada"** (computing
     sense of output, standard in Spanish technical register).
   - A2 title "Bonded outputs": ~~Resultados bajo fianza~~ → **"Salidas bajo fianza"**;
     A2 body already used "salida material".
   - Outcome senses intentionally keep *resultado*: A1(c) "cuando un resultado se
     materialice", A2 "ganchos de … resultado", A4 "resultados que ningún instrumento
     puede verificar", A5 "resultados del mundo real", L1 "tendencias de resultados" /
     "verificación de resultados". Verified by grep: no remaining *resultado* in an
     output sense. **resolved**

## Clause-coverage check vs rev2 source (Spanish counterpart → verdict)

STATUS: rev2 lineage + independent/mechanical legs + `day-12-audit.md` + rev1/day-8
lineage + Cloudflare pending + draft scope → **present** (rev2 tras la auditoría completa
del corpus del Día 12… vía independiente… de solo lectura; vía mecánica… / La rev1 siguió
al equipo rojo del Día 8… / pendiente / Borrador; no publicado).

A1(c): post-hoc `outcome_check` ✓ ("superar una `outcome_check` (verificación de
resultados) *a posteriori*"); binding level → "a nivel del vínculo" ✓; invalid unless
{condition, verifier_ref, deadline} → "una atestación sin los campos {condition,
verifier_ref, deadline} es inválida" ✓; full_validate applied by certify → "(`full_validate`,
aplicado por `certify`)" ✓; execution at maturity = operator's duty → "ejecutar la
verificación cuando el resultado madura es deber del operador" ✓; not optional → "el
vínculo no es opcional" ✓; not automatable by a format checker → "la ejecución no puede
automatizarla un comprobador de formato" ✓. **complete**

A2: five attestation fields ✓; day-4 spec reference (now in code backticks, matching the
EN source) ✓; format-only claim ✓ ("es un *formato* de atestación"); evidence_ref
mandatory field ✓ ("es un campo obligatorio (`evidence_ref`)"); no artifact fetch / no
external hash verification ✓ ("nada recupera los artefactos ni verifica los hashes contra
fuentes externas"); forfeit_split allocation arithmetic, not transfer ✓ ("es aritmética
de asignación, no una transferencia"); assumption-bound verdict with red-team §A2 +
Día-12 audit refs ✓; no escrow/no payouts ✓; L1-meaning sentence ✓. **complete**

L1: "la capa de formato de cada artículo — nada más, y este peldaño no reivindica nada
más" ✓; A1 labels + certify rejection + not-enforced truth/execution ✓; A2 records +
not-enforced identity/custody/adjudication/payments ✓; A3 signer-of-record +
not-enforced competence/halt authority ✓; A4 published dated disclosure + not-enforced
accuracy ✓; A5 hashchain verify() recalcula/detects + completeness + operator-logger
sentence ✓; four metrics ✓; denominators/umbrales at adoption, not retroactive, Día-13
deadline ✓; not instrumentation theater ✓; red-test rule ✓. **complete**

## Notes / residues

- A1 close "ranking → clasificación" (Day-9 optional polish item) left unchanged — it was
  not part of the accepted-open list; noted for any future polish pass.
- Code tokens verbatim: {condition, verifier_ref, deadline}, full_validate, certify,
  evidence_ref, forfeit_split, hashchain, verify().

VERDICT: **PASS WITH NOTES** — accepted-open item cleared, coverage complete against
rev2; single-operator verification only (no external leg remaining in budget).
