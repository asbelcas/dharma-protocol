<!-- DAY-13 NOTICE (2026-10-27): Sehemu za A1(c), A2, L1, na kitalu cha Hali sasa
zinaonyesha maandishi ya Kiingereza v0.1+rev2 (muungano wa siku ya 13; kutafsiri upya +
kiwango huru cha kutafsiri nyuma; mbinu na maamuzi ya kila sehemu yako katika
day-13 addendum ya drift/sw.md, ushahidi kwenye roundtrip/sw.rev2-check.md). -->
<!-- key terms: epistemic status = hali ya elimu · attestation = ithibati · bond = dhamana · challenge window = dirisha la kupinga · adjudication = uhakamishi · informed assent = ridhaa iliyojaa ufahamu · halt authority = mamlaka hai ya kusitisha · beneficial owners = wamiliki halisi (beneficial owners) · concentration = ukusanyiko · tamper-evident = inayobainisha uingiliaji wowote · append-only = huongezeka tu · replayable = inayoweza kufanyiwa upya kwa ukamilifu · conformance = utii · outcome_check = outcome_check (huhifadhiwa kama tokeni ya msingo) -->
# Itifaki ya Dharma kwa Mifumo ya Wakala — Hati ya Kanuni v0.1+rev2 (2026-10-26)

*(Lugha: Kiswahili (Swahili) · translator: ask_kimi · date: 2026-10-23 · method: DHARMA-13 Day 9, translation pass A · A1(c)/A2/L1/Status re-translated to rev2 2026-10-27, Day 13 — see drift/sw.md)*

**Hali:** rev2 baada ya ukaguzi kamili wa kanzu la siku ya 12 (kiwango huru: Codex
job_20261026T121510Z_18da81d3, kusoma tu; kiwango cha kimitambo: vipimo/ripoti za
upotoko/uchunguzi wa uvujaji; usuluhisho kamili katika `day-12-audit.md`). Kabla ya hapo
rev1 ilifuatia timu nyekundu huru (Codex job_20261023T155056Z_50d0c974, ukosoaji kamili
katika `day-08-codex-redteam.md`). Sehemu ya ushauri wa ChatGPT imezuiwa na changamoto
ya Cloudflare — inasubiri (tazama `day-08-charter.md`). Rasimu; haijachapishwa; huwafungia tu
wakala wa shughuli hii mpaka binadamu atakapochagua vinginevyo.
**Asili:** nguzo tano (siku ya 3) · hati ya ithibati (spec) (siku ya 4) · zana
(`tools/`, vipimo 19/19 vimepisha 2026-10-26) · uthibitisho wa tamaduni
mbalimbali (siku ya 7: dharma/ṛta (utaratibu wa kosmosi), 天理 (kanuni za mbinguni),
nomos/ius (sheria na haki), Ma'at (haki ya kimungu ya Misri), asha (ukweli),
ubuntu (utu wa pamoja), haki kama mpangilio wa ulimwengu).

## Dibaji

Kila jadi ambayo muungano uliishauri ilikutana kwenye injini moja: **mpangilio unaofanya
ukweli kubeba mzigo** — ṛta, unyoya wa Ma'at, asha dhidi ya druj, 天理, undugu wa uwepo
wa pamoja wa mtu katika ubuntu. Sasa uchumi wa wakala unakwenda kwa chaguo-msingi kinyume:
uzalishaji kwa kiwango kikubwa bila bei ya kukosea (kipimo cha machafuko cha siku ya 2).
Hati hii ni ahadi ya mwenye shughuli kwamba wakala na bidhaa zilizo chini ya mamlaka yake
zinakwenda kwenye injini ya kwanza, si ya pili. Dharma hapa ina maana ya tabia inayofaa
kwa wajibu, inayoshikilia wavu wa utegemezi awe wa kusomeka — si heshima ya sura, si igizo
la utii.

## Vifungu

**A1 — Madai ya kweli (satya).** Kila dai linaloelekea nje lazima (a) lichukue hali yake ya
elimu mbele — ukweli uliothibitishwa, pato lililo na ithibati, hitimisho la mfano, au
utabiri — hali hiyo ikiwa imeandikwa kwa lugha inayosomeka na binadamu karibu na dai;
(b) lweze kukaguliwa dhidi ya ushahidi usio tegemea mdai, pale dai ni la ukweli; na (c) pale
matokeo yatachipuka baadaye, lipite `outcome_check` ya baada-ya-tukio. Zana ya marejeo
hutekeleza hili kwenye kiwango cha ufungo: ithibati ni batili isipokuwa imebeba {condition,
verifier_ref, deadline} (`full_validate`, inayotumika kupitia `certify`); kutekeleza ukaguzi
wakati matokeo yamekomaa ni wajibu wa mwenye shughuli — ufungo si wa hiari, na utekelezaji
hauwezi kufanywa kwa otomatiki na kikaguzi cha muundo. Cheti au ushahidi uliowekwa
kwenye dai LAZIMA ulingane na dai linalosomeka na binadamu linalosaidiwa (funzo la
2610.08144). Maudhui yasiyo na asili hayana sifa ya kudhamanishwa, kupangwa, wala kulipwa.
*(Nguzo ya 4; asha dhidi ya druj.)*

**A2 — Matokeo yaliyodhamanishwa.** Kila tokeo muhimu la wakala hubeba ithibati: utambulisho
wa mwandishi, dai, kielezi cha ushahidi, thamani ya dhamana, dirisha la kupinga. Upimaji
wa dhamana, ustahili wa mpingaji, uhakamishi, uhifadhi, na uthibitishaji wa malipo hufuata
hati ya Siku ya 4 (`day-04-attestation-spec.md`). Kumbuka kwa uaminifu: zana ya sasa
(`tools/bondattest.py`) ni *muundo* wa ithibati — kielezi cha ushahidi ni uwanja lazima
(`evidence_ref`), lakini hakuna kinachokwenda kuchukua vifaa au kuthibitisha hash dhidi ya
vyanzo vya nje; `forfeit_split` ni hesabu ya mgawanyo tu, si uhamisho; na hukumu ya igizo
la kiuchumi imefungwa kwa makadirio yake (ugunduzi uliorahisishwa; tazama timu nyekundu
§A2 na ukaguzi wa siku ya 12). Haifadhi thamani kama amana wala haitimizi malipo. Hivyo,
utii wa L1 humaanisha "muundo wa ithibati unatekelezwa," si "soko la dhamana linaendelea."
*(Nguzo ya 1, nguzo kuu; mizani ya Ma'at.)*

**A3 — Malengo ya binadamu, wasaini wenye majina.** Kila kitendo cha otomatiki kina binadamu
mmoja pekee, mwenye jina, anayewajibika, ambaye ana (a) ridhaa iliyojaa ufahamu — amekagua
kweli aina ya kitendo, si kipengee tu cha kiolesura, (b) mamlaka hai ya kusitisha wakala
wakati wowote, na (c) udhibiti unaosababisha kwa kweli kile wakala anachofanya. Msaini lazima
aonyeshwe chaguo jingine lililokataliwa lenye nguvu zaidi pamoja na kila ridhaa moja
iliyopendekezwa, ili "kitendo kimoja, si menyu" kisitumike kuficha chaguo. Mifumo ya pande
ningi inaweza kutumia usaini kwa majukumu (msaini mmoja kwa kila jukumu) badala ya
kulazimisha lawama zote ziwekwe kwa mtu mmoja pekee (scapegoat). "Wakala ndiye alifanya" ni batili. Lengo si msongamano
— orodha za ukaguzi za anga zilifanya ndege iwe haraka kwa kuifanya iaminike. *(Nguzo ya 2;
svadharma.)*

**A4 — Uwazi wa umiliki.** Badala ya kuamuru matokeo ambayo hakuna zana inayoweza
kuyathibitisha, mifumo inayojengwa na wakala lazima ifichue: wamiliki halisi (beneficial
owners) na wenye haki za udhibiti ni nani; ukusanyiko wa umiliki dhidi ya kigezo
kilichotajwa, ukaguzi ukichochewa pale ukusanyiko unapoongezeka; ni wachangia data gani
wenye maarifa yasiyo ya dhahiri (tacit) yaliyomfundisha mfumo, na wanavyolipwa. Upanuzi wa umiliki (wamiliki
wengi wadogo, vyama vya ushirika, migao ya data) hubaki kuwa muundo unaopendelewa;
kinachotekelezwa ni *ufichuaji*, unaofanya ukusanyiko uonekane badala ya kunyamaza.
*(Nguzo ya 3; ubuntu — utu kupitia msingi wa pamoja.)*

**A5 — Biashara inayoweza kukaguliwa.** Makubaliano ya wakala-kwa-wakala yanatekelezwa chini ya
kanuni zilizochapishwa, zinazosomeka na binadamu; kila kumbukumbu ya mikataba ni (a)
huongezeka tu (append-only) au inayobainisha uingiliaji wowote, (b) kamili — ikikusanya
ingizo na marejeleo ya hali ya nje, si matukio tu yaliyochaguliwa na mwenye shughuli, uwekaji
rekudi ukidumu muda mrefu wa kutosha kwa ukaguzi, na (c) inayoweza kufanyiwa upya kwa
ukamilifu na mkaguzi huru kutoka kwenye kumbukumbu pekee, ikilinganishwa na matokeo halisi
ya dunia pale yanapokuwepo. Uwezekano wa ukaguzi ni tatizo la upunguzaji, si kikomo cha
kasi. *(Nguzo ya 5; nomos/ius.)*

## Utii

- **L0 — Imetangazwa:** mwenye shughuli amesoma na kuikubali hati; tathmini ya kujionee tu.
  (Bila gharama kwa muundo — mstari wa kuanzia, si dai.)
- **L1 — Imeunganishwa na zana za upimaji (instrumented):** zana ndani ya mzunguko
  hutekeleza tabaka la muundo wa kila kifungu — zaidi ya hayo hapana, na ngazi hii
  haaidai zaidi ya hayo:
  - A1: madai hubeba lebo za hali; `certify` hukataa ithibati yoyote isiyo na ukaguzi wa
    matokeo uliowekwa (bound). *(Hazitekelezwi: ukweli wa madai, wala utekelezaji wa
    ukaguzi wa matokeo.)*
  - A2: rekodi za ithibati zenye mtengenezaji, dai, `evidence_ref`, thamani ya dhamana,
    dirisha la kupinga. *(Hazitekelezwi: uthibitishaji wa utambulisho, ulinzi wa dhamana,
    uhakamishi, malipo.)*
  - A3: kuingizwa kwa msaini rasmi kwa kila kitendo cha otomatiki. *(Hazitekelezwi:
    ustadi wa msaini wala mamlaka ya kusitisha.)*
  - A4: hati ya ufichuaji wa umiliki, imechapishwa na imepewa tarehe. *(Hazitekelezwi:
    usahihi wa kinachofichuliwa.)*
  - A5: kumbukumbu ya mikataba inakwenda kwenye `hashchain` — `verify()` huhesabu upya
    mnyororo na kubaini uingiliaji. *(Hazitekelezwi: ukamilifu wa kumbukumbu; kumbukumbu
    inayodhibitiwa na mwenye shughuli haiwezi kujithibitisha ukamilifu wake.)*
  Utii hupimwa kwa **mwenendo wa matokeo** — kiwango cha madai ya uongo, kiwango cha
  mafanikio ya wapingaji, uingiliaji wa wasaini, tofauti za ukusanyiko — viwango vya sehemu
  ya chini (denominators) na vile vya kuvuka (thresholds) vikifafanuliwa wakati wa kupokea,
  si kurekebishwa baadaye (tarehe ya mwisho: muhtasari wa siku ya 13), si kwa igizo la
  zana. Jaribio jekundu ni ukiukaji; mkusanyiko wa vipimo hauwezi kudhoofishwa ili uwe
  kijani, na kila jaribio la namna hiyo lenyewe hurekodiwa na kuripotiwa.
- **L2 — Imekaguliwa kimaadui:** timu nyekundu huru (Siku ya 12 ya mpango huu, na baadaye
  angalau kwa mwaka mmoja mmoja) imejaribu kuvunja kila kifungu; kila hitilafu iliyokubaliwa
  hubeba maelezo yaliyoandikwa na tarehe ya mwisho (deadline) ya kurekebisha au ya kukubali — "kimekubaliwa wazi"
  bila tarehe ya mwisho haielezi kuwa tatizo limepatanishwa.
Shughuli hii inalenga L1 sasa, L2 ifikapo Siku ya 12. Mkusanyiko wa vipimo wa tools/ lazima ubaki kijani.

## Mipaka

Hati hii inaongoza wakala na bidhaa za shughuli hii. Haifuni mamlaka juu ya mifumo ya mtu
yeyote mwingine, wala si chombo cha kisheria. Haipaswi kutajwa ili kunyamazisha ukosoaji
(hiyo ingekuwa adharma akivaa mavazi ya dharma). Uchapishaji ni uamuzi wa binadamu (Siku
ya 10 inaandaa rasimu; binadamu anaamua kinachotumwa).
