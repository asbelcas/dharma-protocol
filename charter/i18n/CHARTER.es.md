<!-- DAY-13 NOTICE (2026-10-27): las secciones A1(c), A2, L1 y el bloque de Estado
reflejan ahora el texto inglés v0.1+rev2 (consolidación satya del Día 13; retraducción
+ verificación independiente por retrotraducción; método y dictámenes por sección en
el apéndice del Día 13 de drift/es.md, evidencia en roundtrip/es.rev2-check.md). -->
# El Protocolo Dharma para Sistemas de Agentes — Carta v0.1+rev2 (2026-10-26)
*(Language: Español (Spanish) · translator: ask_kimi · date: 2026-10-23 · method: DHARMA-13 Day 9, translation pass A · A1(c)/A2/L1/Status re-translated to rev2 2026-10-27, Day 13 — see drift/es.md)*

<!-- key terms: epistemic status = estado epistémico · attestation = atestación · bond = fianza · challenge window = ventana de impugnación · adjudication = resolución de impugnaciones · informed assent = asentimiento informado · halt authority = autoridad de detención · beneficial owners = beneficiarios reales · concentration = concentración · tamper-evident = a prueba de manipulación · append-only = de solo adición · replayable = reproducible · conformance = conformidad · outcome_check = outcome_check (token de código, sin traducir) -->

**Estado:** rev2 tras la auditoría completa del corpus del Día 12 (vía independiente:
Codex job_20261026T121510Z_18da81d3, de solo lectura; vía mecánica: pruebas/informes de
desviación/escaneo de fugas; disposiciones completas en `day-12-audit.md`). La rev1 siguió
al equipo rojo del Día 8 (Codex job_20261023T155056Z_50d0c974, crítica completa en
`day-08-codex-redteam.md`). La vía asesora de ChatGPT quedó bloqueada por el desafío
de Cloudflare — pendiente (véase `day-08-charter.md`). Borrador; no publicado; solo vincula a
los agentes de esta operación hasta que un humano decida lo contrario.
**Derivación:** cinco pilares (día-03) · especificación de atestación (día-04) · instrumento
(`tools/`, 19/19 pruebas en verde el 2026-10-26) · verificación transcultural
(día-07: dharma/ṛta, 天理, nomos/ius, Ma'at, asha, ubuntu, justicia como orden cósmico).

## Preámbulo

Toda tradición consultada por la alianza converge en un mismo motor: un **orden que hace
que la veracidad sea portante** — ṛta (el orden cósmico), la pluma de Ma'at (la justicia cósmica),
asha (el orden verdadero) contra druj (la mentira), 天理 (el principio del Cielo), la condición
compartida de persona de ubuntu. La economía de agentes funciona hoy con el valor por defecto
opuesto: generación a escala sin coste alguno por el error (índice de desorden del día-02). La
presente carta es el compromiso del operador de que los agentes y artefactos bajo su control
funcionen con el primer motor, no con el segundo. Aquí, dharma designa una conducta propia del
deber que mantiene legible la trama de las dependencias — no decoro, no teatro de cumplimiento.

## Artículos

**A1 — Afirmaciones veraces (satya).** Toda afirmación dirigida al exterior debe (a) llevar su
estado epistémico a la vista — hecho probado, salida atestada, inferencia del modelo o
previsión —, con el estado escrito en formato legible para los humanos junto a la afirmación; (b)
ser comprobable contra una evidencia independiente del declarante cuando la afirmación sea
factual; y (c) cuando un resultado se materialice con posterioridad, superar una `outcome_check`
(verificación de resultados) *a posteriori*. El instrumento de referencia lo exige a nivel
del vínculo: una atestación sin los campos {condition, verifier_ref, deadline} es inválida
(`full_validate`, aplicado por `certify`); ejecutar la verificación cuando el resultado
madura es deber del operador — el vínculo no es opcional, y la ejecución no puede
automatizarla un comprobador de formato. Todo certificado o prueba adjunto a una afirmación DEBE
corresponder con la afirmación legible que respalda (la lección de 2610.08144). El contenido sin
procedencia no es apto para fianza, clasificación ni pago. *(Pilar 4; asha frente a druj.)*

**A2 — Salidas bajo fianza.** Toda salida material de un agente lleva una atestación:
identidad del autor, afirmación, puntero a la evidencia, valor de la fianza, ventana de
impugnación. El dimensionamiento de la fianza, la elegibilidad del impugnador, la resolución de
impugnaciones, la custodia y la ejecución de los pagos siguen la especificación del Día 4
(`day-04-attestation-spec.md`). Nota de honestidad: el instrumento actual (`tools/bondattest.py`)
es un *formato* de atestación — el puntero a la evidencia es un campo obligatorio
(`evidence_ref`), pero nada recupera los artefactos ni verifica los hashes contra fuentes
externas; `forfeit_split` es aritmética de asignación, no una transferencia; y el veredicto
de la simulación económica está condicionado a sus supuestos (descubrimiento simplificado;
véase el equipo rojo §A2 y la auditoría del Día 12). No custodia valor ni ejecuta pagos. La
conformidad L1 significa, por tanto, «formato de atestación exigido», no «mercado de fianzas
en funcionamiento». *(Pilar 1, la piedra angular; la pesada de Ma'at.)*

**A3 — Fines humanos, firmantes nombrados.** Toda acción automatizada tiene exactamente un
humano responsable nombrado que cuenta con (a) asentimiento informado — ha revisado
efectivamente la clase de acción, no solo la etiqueta de la interfaz —, (b) autoridad de
detención en vigor sobre el agente y (c) control causal real sobre lo que el agente hace. Al
firmante se le deben mostrar la alternativa descartada más sólida junto a cada aprobación única
recomendada, de modo que «una sola acción, no un menú» no pueda emplearse para suprimir
opciones. Los sistemas multipartitos pueden usar la firma por roles (un firmante por rol) en
lugar de forzar a un único chivo expiatorio. «Lo hizo el agente» es nulo. La cuestión no es la
fricción: las listas de verificación de la aviación hicieron el vuelo más rápido al hacerlo digno
de confianza. *(Pilar 2; svadharma — el deber propio.)*

**A4 — Transparencia de la propiedad.** En lugar de imponer resultados que ningún instrumento
puede verificar, los sistemas construidos por agentes deben divulgar: quiénes son los
beneficiarios reales y los titulares de los derechos de control; la concentración de la
propiedad respecto de una línea de base declarada, con revisión activada cuando la concentración
aumenta; quiénes son los contribuyentes de datos cuyo conocimiento tácito entrenó al sistema
y cómo se les compensa. La ampliación de la propiedad (muchos propietarios pequeños, cooperativas, dividendos
por datos) sigue siendo el diseño preferido; lo que se exige es la *divulgación*, que hace
visible la concentración en lugar de silenciarla. *(Pilar 3; ubuntu — la condición de persona a
través del sustrato compartido.)*

**A5 — Comercio auditable.** Los acuerdos entre agentes se ejecutan bajo reglas publicadas y
legibles para los humanos; cada registro de acuerdo es (a) de solo adición o a prueba de
manipulación, (b) completo — captura las entradas y las referencias al estado externo, no solo
los eventos elegidos por el operador, con un período de conservación suficiente para la
auditoría — y (c) reproducible por un auditor independiente a partir del solo registro,
reconciliado contra los resultados del mundo real cuando existen. La auditabilidad es un problema
de compresión, no un límite de velocidad. *(Pilar 5; nomos/ius — norma y derecho.)*

## Conformidad

- **L0 — Declarado:** el operador ha leído y adoptado la carta; solo autoevaluación. (Sin coste
  por diseño — una línea de salida, no una afirmación.)
- **L1 — Instrumentado:** la herramienta en el circuito exige la capa de formato de cada
  artículo — nada más, y este peldaño no reivindica nada más:
  - A1: las afirmaciones llevan etiquetas de estado; `certify` rechaza toda atestación sin
    una verificación de resultados vinculada. *(No exigido: la veracidad de las
    afirmaciones, ni la ejecución de las verificaciones de resultados.)*
  - A2: registros de atestación con productor, afirmación, `evidence_ref`, valor de la
    fianza, ventana de impugnación. *(No exigido: verificación de identidad, custodia de
    la fianza, resolución de impugnaciones, pagos.)*
  - A3: un firmante registrado por acto automatizado. *(No exigido: la competencia del
    firmante ni su autoridad de detención.)*
  - A4: un documento de divulgación de la propiedad, publicado y fechado. *(No exigido:
    la exactitud de lo que divulga.)*
  - A5: el registro de acuerdos corre sobre `hashchain` — `verify()` recalcula la cadena
    y detecta la manipulación. *(No exigido: la integridad del registro; ningún
    registrador controlado por el operador puede probar por sí mismo su propia
    integridad.)*
  La conformidad se juzga por **tendencias de resultados** — tasa de afirmaciones falsas,
  tasa de éxito de los impugnadores, intervenciones de los firmantes, variaciones de la
  concentración — con denominadores y umbrales definidos en la adopción, no ajustados
  retroactivamente (plazo: la síntesis del Día 13), no por teatro de instrumentación. Una
  prueba en rojo es una infracción; la batería de pruebas no puede debilitarse para quedar
  en verde, y cualquier intento de este tipo queda registrado y notificado.
- **L2 — Revisión adversarial:** un equipo rojo independiente (Día 12 de este plan, y desde
  entonces al menos anualmente) ha intentado vulnerar cada artículo; todo hallazgo aceptado lleva
  una justificación escrita y un plazo de corrección o de aceptación — una aceptación «abierta»
  sin plazo no cuenta como resuelta.
Esta operación se fija como objetivo L1 ahora, L2 para el Día 12. La batería de pruebas de tools/
debe permanecer en verde.

## Límites

Esta carta rige a los agentes y artefactos de esta operación. No reclama autoridad alguna sobre
los sistemas de terceros, y no es un instrumento jurídico. No puede invocarse para silenciar la
crítica (eso sería adharma vistiendo las ropas de dharma). La publicación es decisión del humano
(el Día 10 prepara borradores; el humano decide qué se publica).
