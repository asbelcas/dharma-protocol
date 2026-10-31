# Drift Report — CHARTER.es.md (Spanish)

- Language: es (Spanish)
- Date: 2026-10-23
- Method: back-translated from translation alone, then diffed against source.
- Back-translation: `i18n/roundtrip/CHARTER.es.back-en.md`

## Findings

| Section | Source meaning (quote) | Back-translated rendering | Severity | Cause |
|---|---|---|---|---|
| Title/Status/Derivation | "Charter v0.1+rev1"; "ChatGPT advisory leg blocked by Cloudflare challenge"; "justice-as-cosmic-order" | Identical structure and content; "vía asesora" = advisory leg/track | none | faithful |
| Preamble | "one engine"; "no price on being wrong"; "duty-appropriate conduct that keeps the web of dependences legible" | "un mismo motor" (slightly more emphatic); "sin coste alguno por el error"; "conducta propia del deber … trama de las dependencias" | none | faithful |
| A1 head | "Truthful claims (satya)" | "Afirmaciones veraces (satya)" | none | faithful |
| A1(a) | "attested output" | "resultado atestado" | minor | ambiguity-in-target |
| A1(c) | "the stronger check already implemented" | "la comprobación más exigente ya implementada" | minor | translator-error |
| A1 close | "ineligible for bonding, ranking, or payment" | "no es apto para fianza, clasificación ni pago" | minor | ambiguity-in-target |
| A2 head | "Bonded outputs" | "Resultados bajo fianza" | minor | ambiguity-in-target |
| A2 body | "adjudication, custody, and payout enforcement"; "bond market live" | "resolución de impugnaciones … ejecución de los pagos"; "mercado de fianzas en funcionamiento" | none | faithful (translator's key-terms header explicitly maps adjudication → resolución de impugnaciones) |
| A3 | "named accountable human"; "live authority to halt"; "strongest declined alternative" | "humano responsable nombrado"; "autoridad de detención en vigor"; "alternativa descartada más sólida" | none | faithful |
| A4 | "what is enforced is the disclosure" | "lo que se exige es la divulgación" (require/demand, not enforce) | none | faithful (nuance softened but same obligation in context) |
| A5 | "deal log"; "human-legible"; "replayable … from the log alone" | "registro de acuerdo"; "legibles para los humanos"; "a partir del solo registro" | none | faithful |
| Conformance L0 | "Costless by design — a starting line, not a claim" | "Sin coste por diseño — una línea de salida, no una afirmación" (race-start metaphor correctly preserved) | none | faithful |
| Conformance L1 | "enforced by tooling in the loop"; "concentration deltas"; "may not be weakened to go green" | "exigidas por herramientas en el circuito"; "variaciones de la concentración"; "no puede debilitarse para quedar en verde" | none | faithful |
| Conformance L2 | "has attempted to break each article"; "remediation or acceptance deadline" | "ha intentado vulnerar cada artículo"; "plazo de corrección o de aceptación" | none | faithful |
| Limits | "not a legal instrument"; "adharma wearing dharma's clothes"; "what ships" | "no es un instrumento jurídico"; "adharma vistiendo las ropas de dharma"; "qué se publica" | none | faithful |

### Explanations for non-"none" findings

1. **A1(a) "attested output" → "resultado atestado"** (minor, ambiguity-in-target): Spanish "resultado" means result/outcome, not "output" (deliverable/product). The computing sense of "output" is normally "salida". On its own this is harmless, but combined with finding 3 it collapses two source distinctions.
2. **A1(c) "the stronger check" → "la comprobación más exigente"** (minor, translator-error): English "stronger" is a comparative (stronger than the (a)/(b) checks); with the definite article, Spanish "la más exigente" reads as an absolute superlative ("the most demanding check there is"). Spanish comparative would more safely be "una comprobación más exigente". A reader could over-read the stringency claim, but no concrete action changes.
3. **A1 close "ranking" → "clasificación"** (minor, ambiguity-in-target): "clasificación" primarily means classification/categorization; "ranking/standing" is a secondary sense (common in sports). Most Spanish readers will read "no apto para clasificación" as "not eligible for classification". The bonding/ranking/payment triad's "ranking" (scoring/ordering) nuance is partially lost. Could arguably be fixed with "ranking" (borrowed) or "ordenación por puntuación".
4. **A2 head "Bonded outputs" → "Resultados bajo fianza"** (minor, ambiguity-in-target): same output→resultado collapse as finding 1. Net effect of findings 1+4: the source's deliberate distinction between "outputs" (A2 — what agents produce and attest) and "outcomes" (A1(c) — later real-world results checked post-hoc) is flattened, since both surface as "resultado". This is the most substantive drift found and it is still not material: A1(c) keeps "resultado" tied to "se materialice con posterioridad" and A2 keeps "producción material", so context disambiguates.

## Untranslatable-term notes

- `outcome_check`: kept as untranslated code token per the translator's own key-terms header ("token de código, sin traducir") — correct handling.
- Cross-cultural lexicon (dharma, ṛta, asha, druj, svadharma, Ma'at, ubuntu, nomos/ius, 天理): kept as-is or with short native glosses; Spanish has no native equivalents and these are intentionally preserved. Glosses ("el deber propio", "la justicia cósmica", "norma y derecho") are additive and accurate.
- "append-only / tamper-evident": rendered as "de solo adición / a prueba de manipulación" — established calques in Spanish technical writing; acceptable.
- "red team": "equipo rojo" — standard calque in Spanish security usage; acceptable.
- No other genuinely untranslatable terms found.

## What was checked

Full pass over all 99 lines of the translation against all 89 lines of the source: title/status/dates/job IDs/file names, Preamble (engine metaphor, day-02/day-07 references, all six cross-cultural terms), A1–A5 article bodies including the (a)/(b)/(c) enumerations and parenthetical pillar citations, Conformance L0/L1/L2 including the "outcome trends" metric list and red-test rule, and Limits. Structure, numbering, bold/italic shapes, and MUST-capitalization (→ DEBE) all preserved. Code tokens (`outcome_check`, `tools/bondattest.py`, `day-04-attestation-spec.md`, `2610.08144`, job ID) intact.

## VERDICT

VERDICT: faithful-with-notes

Minor findings: 4 (none material). Optional translator polish, not required for correctness: (1) "salida" or "producto" for "output" in A1(a)/A2 title to restore the output/outcome distinction; (2) "una comprobación más exigente" for the comparative in A1(c); (3) "ranking" or "ordenación por puntuación" for "ranking" in A1 close.


## Day-12 addendum (2026-10-26, DHARMA-13 Day-12 audit)
Source bumped to v0.1+rev2. This translation's A1(c), A2, and L1 sections still mirror
rev1 text (visible drift, disclosed in the rev2 notice atop CHARTER.es.md); full
re-verification of those three sections is a Day-13 task. Header count/date refreshed:
19/19 tests green 2026-10-26.
- es fix applied: A4 broken syntax repaired (governing verb `quiénes son ... y cómo se les compensa`). Accepted-open (Day-13): `resultado` still covers both output and outcome (A1/A2 distinction); a full disambiguation pass is queued.


## Day-13 addendum (2026-10-27, DHARMA-13 Day-13 satya consolidation)
Secciones A1(c), A2, L1 y bloque de Estado retraducidas al texto inglés v0.1+rev2;
aviso de rev2 en cabecera de `../CHARTER.es.md` actualizado. **Ítem aceptado-abierto
despejado** (ver abajo). Verificación: **pata independiente no ejecutada** — el presupuesto
de búsquedas externas del día se consumió con el probe + las patas fr/zh + los
tiempos-agotados de hi/ar (véase day-13-synthesis.md, registro de límites), por lo que no
se reintentó. Verificación de operador único (pasos separados en sesión): cada cláusula
de la fuente rev2 comprobada por su contrapartida en español (cobertura). Evidencia
completa: `roundtrip/es.rev2-check.md`.
- Ítem aceptado-abierto despejado — disambigüación de `resultado`:
  - A1(a) "attested output": ~~resultado atestado~~ → **"salida atestada"**.
  - A2 título "Bonded outputs": ~~Resultados bajo fianza~~ → **"Salidas bajo fianza"**;
    el cuerpo de A2 ya usaba "salida material".
  - Los sentidos de OUTCOME conservan intencionadamente *resultado*: A1(c) "cuando un
    resultado se materialice", A2 "ganchos de … resultado", A4 "resultados que ningún
    instrumento puede verificar", A5 "resultados del mundo real", L1 "tendencias de
    resultados". Verificado por grep: ningún `resultado` restante en sentido de output.
    resolved
- Estado → linaje rev2: recuperado (ambos job IDs, vías, Cloudflare pendiente). resolved
- A1(c) nivel del vínculo ({condition, verifier_ref, deadline}; full_validate aplicado
  por certify; deber del operador): completo. resolved
- A2 nota de honestidad ampliada (evidence_ref campo obligatorio; nada recupera artefactos
  ni verifica hashes; forfeit_split = aritmética de asignación; veredicto condicionado a
  sus supuestos, ambas referencias): completo. resolved
- L1 cumplimiento por artículo + listas "no exigido" + métricas de tendencias +
  cláusula de denominadores/umbrales: completo. resolved
- Residuo: "clasificación" por "ranking" (ítem de pulido opcional del Día 9) queda sin
  cambio — no formaba parte de la lista de aceptados-abiertos.

VERDICT: **PASS WITH NOTES** — ítem aceptado-abierto despejado, cobertura completa
frente a rev2; nota = sin pata independiente (presupuesto externo agotado).
