# Recorded experimental evidence

This report is generated from the three downloaded run archives. Values are measured outputs, not newly generated training results. All original JSON, CSV, corpus, checkpoints and model files are preserved in the result ZIPs.

## starter

Full archive: [starter-results.zip](starter-results.zip). Extract it to obtain `results/starter/`.

### Full fixed-panel loss history

| Step | Training loss | Validation loss |
| --- | --- | --- |
| 0 | 4.926252365112305 | 4.927547931671143 |
| 1500 | 0.6821389198303223 | 0.7182432413101196 |
| 3000 | 0.6783125996589661 | 0.7061358094215393 |

### Sample timeline

#### Step 0

```text
pear professor bond doctor course harvest team physician journey checking buyer delivery traffic report the lecturer item offering and system <UNK> taste recommended mentioned bus question customer at mortgage nurse in instructor
kitchen purchase journey product question discussion journey service . nurse local
compared and purchase update mortgage question loan taste in market treatment learned another item bicycle product bicycle focused data and dentist recommended mango apple taxi bicycle delivery peach quality update student lesson
important hospital juice patient return recommended deposit tutor returned understand kitchen student design ordered hospital treatment important package traffic with yesterday investment important of mentioned store ordered mortgage nurse shopper the station
```

#### Step 1500

```text
our school has a question about the new educator and lesson .
a review of risk helped us understand the different deposit .
we learned about the important website during a discussion of data .
our school has a question about the different instructor and course .
```

#### Step 3000

```text
our school has a question about the new educator and lesson .
a review of risk helped us understand the different deposit .
the report about the nurse explains the health in detail .
the consumer compared the offering after checking the price .
```

### Before/after evaluation summaries

#### untrained

| Group/category | Correct / all | Scorable | All-case success | Scorable accuracy | Coverage |
| --- | --- | --- | --- | --- | --- |
| overall | 9/48 | 24 | 18.8% | 37.5% | 50.0% |
| extend_corpus | 0/24 | 0 | 0.0% | N/A | 0.0% |
| starter_patterns | 6/16 | 16 | 37.5% | 37.5% | 100.0% |
| starter_transfer | 3/8 | 8 | 37.5% | 37.5% | 100.0% |
| categories_and_analogies | 0/3 | 0 | 0.0% | N/A | 0.0% |
| domain_context | 3/8 | 8 | 37.5% | 37.5% | 100.0% |
| domain_place | 3/8 | 8 | 37.5% | 37.5% | 100.0% |
| everyday_knowledge | 0/3 | 0 | 0.0% | N/A | 0.0% |
| grammar | 0/3 | 0 | 0.0% | N/A | 0.0% |
| negation | 0/3 | 0 | 0.0% | N/A | 0.0% |
| new_wording | 3/8 | 8 | 37.5% | 37.5% | 100.0% |
| opposites | 0/3 | 0 | 0.0% | N/A | 0.0% |
| reference | 0/3 | 0 | 0.0% | N/A | 0.0% |
| sequence | 0/3 | 0 | 0.0% | N/A | 0.0% |
| spatial_relations | 0/3 | 0 | 0.0% | N/A | 0.0% |

#### final

| Group/category | Correct / all | Scorable | All-case success | Scorable accuracy | Coverage |
| --- | --- | --- | --- | --- | --- |
| overall | 20/48 | 24 | 41.7% | 83.3% | 50.0% |
| extend_corpus | 0/24 | 0 | 0.0% | N/A | 0.0% |
| starter_patterns | 16/16 | 16 | 100.0% | 100.0% | 100.0% |
| starter_transfer | 4/8 | 8 | 50.0% | 50.0% | 100.0% |
| categories_and_analogies | 0/3 | 0 | 0.0% | N/A | 0.0% |
| domain_context | 8/8 | 8 | 100.0% | 100.0% | 100.0% |
| domain_place | 8/8 | 8 | 100.0% | 100.0% | 100.0% |
| everyday_knowledge | 0/3 | 0 | 0.0% | N/A | 0.0% |
| grammar | 0/3 | 0 | 0.0% | N/A | 0.0% |
| negation | 0/3 | 0 | 0.0% | N/A | 0.0% |
| new_wording | 4/8 | 8 | 50.0% | 50.0% | 100.0% |
| opposites | 0/3 | 0 | 0.0% | N/A | 0.0% |
| reference | 0/3 | 0 | 0.0% | N/A | 0.0% |
| sequence | 0/3 | 0 | 0.0% | N/A | 0.0% |
| spatial_relations | 0/3 | 0 | 0.0% | N/A | 0.0% |

### Token, vector, gradient and prediction

Selected token: `customer`; ID: **28**. IDs are vocabulary indices, not meanings.

<details><summary>embedding_before (complete saved values)</summary>

```json
[
  -0.057591915130615234,
  -0.004809952806681395,
  0.04263188689947128,
  0.019338956102728844,
  0.015643136575818062,
  -0.02882436476647854,
  0.025609055534005165,
  5.246092769084498e-05,
  0.02470681630074978,
  0.0206917654722929,
  0.0073690167628228664,
  -0.033089615404605865,
  -0.05354786291718483,
  -0.0057429298758506775,
  -0.024166762828826904,
  -0.014716118574142456,
  0.004685705993324518,
  -0.01045426819473505,
  -0.008381075225770473,
  -0.018258560448884964,
  -0.020133700221776962,
  0.005098649766296148,
  -0.010916502214968204,
  -0.012633351609110832,
  0.028389625251293182,
  -0.002631223062053323,
  -0.004071928560733795,
  0.013641919940710068,
  -0.009891724213957787,
  -0.01671762391924858,
  0.0019060791237279773,
  -0.0014535071095451713,
  0.01602652110159397,
  -0.005674874875694513,
  -0.0006723481928929687,
  -0.001290727173909545,
  -0.0073194727301597595,
  -0.0009307070868089795,
  0.001507619977928698,
  -0.004976638592779636,
  -0.028987020254135132,
  0.018092988058924675,
  -0.007348013576120138,
  -0.005440254230052233,
  0.01564120501279831,
  -0.004543505609035492,
  0.04156793653964996,
  0.052355434745550156,
  0.02264268510043621,
  -0.015414278954267502,
  -0.025121202692389488,
  -0.006797463167458773,
  0.02935275062918663,
  -0.0025336795952171087,
  0.029801232740283012,
  -0.022797005251049995,
  -0.030237913131713867,
  0.006436783354729414,
  0.050490811467170715,
  0.007490998134016991,
  -0.01072286069393158,
  0.02473733201622963,
  -0.014468724839389324,
  0.013235910795629025
]
```

</details>

<details><summary>embedding_after (complete saved values)</summary>

```json
[
  0.03662968426942825,
  -0.01821804977953434,
  0.13302753865718842,
  0.10595157742500305,
  0.06301464885473251,
  0.018913576379418373,
  0.15230250358581543,
  0.09290938824415207,
  -0.06321955472230911,
  -0.017256855964660645,
  0.03409649431705475,
  -0.04738563299179077,
  -0.06455359607934952,
  -0.08658706396818161,
  -0.1449921429157257,
  -0.03588370978832245,
  -0.15690958499908447,
  -0.1502740979194641,
  -0.007622718811035156,
  -0.07074500620365143,
  -0.09301486611366272,
  0.009106839075684547,
  -0.06480730324983597,
  0.017523247748613358,
  0.003923745825886726,
  -0.062454286962747574,
  0.11252037435770035,
  -0.06432817131280899,
  0.052046604454517365,
  -0.15667366981506348,
  -0.07061680406332016,
  0.06167813390493393,
  -0.03177092596888542,
  0.14139509201049805,
  0.09131097793579102,
  0.056472133845090866,
  0.01960933208465576,
  -0.1348366141319275,
  0.12228488177061081,
  -0.033832427114248276,
  0.1187402606010437,
  0.004576496779918671,
  -0.13443273305892944,
  0.05294271558523178,
  -0.03759584575891495,
  -0.10312052071094513,
  0.020272448658943176,
  0.03811731934547424,
  -0.01984069123864174,
  -0.1507372260093689,
  0.03028012625873089,
  -0.12055385857820511,
  0.016617776826024055,
  0.07775366306304932,
  0.11808909475803375,
  0.0557357557117939,
  0.09336108714342117,
  0.002622203202918172,
  0.03705667704343796,
  0.07563258707523346,
  0.11851995438337326,
  0.014375481754541397,
  0.0912889838218689,
  -0.07461018860340118
]
```

</details>

<details><summary>first_update (complete saved values)</summary>

```json
{
  "token": "customer",
  "coordinate": 0,
  "before": -0.057591915130615234,
  "gradient": 0.0006925872294232249,
  "learning_rate": 1e-05,
  "after": -0.05760190635919571
}
```

</details>

Top next-token probabilities for `the customer`:

| Stage | Token | Probability |
| --- | --- | --- |
| before | customer | 0.016007 |
| before | bus | 0.010685 |
| before | educator | 0.010398 |
| before | us | 0.010329 |
| before | application | 0.010121 |
| after | reviewed | 0.178249 |
| after | recommended | 0.171205 |
| after | ordered | 0.168474 |
| after | selected | 0.163443 |
| after | compared | 0.159659 |

| State | Nearest customer neighbors (64-dimensional cosine) |
| --- | --- |
| initial | bus (0.2133), educator (0.2033), helped (0.2022) |
| final | shopper (0.9781), client (0.9769), buyer (0.9766) |

Saved attention rows (causal lower-triangular matrix):

```json
[
  [
    1.0,
    0.0,
    0.0
  ],
  [
    0.6059795022010803,
    0.3940204977989197,
    0.0
  ],
  [
    0.48513180017471313,
    0.42299577593803406,
    0.09187241643667221
  ]
]
```

### Temperature samples

#### Temperature 0.3

```text
our school has a question about the new educator and lesson .
a review of risk helped us understand the different investment .
the report about the nurse explains the health in detail .
the local consumer was mentioned in the purchase report yesterday .
```

#### Temperature 0.8

```text
our school has a question about the new educator and lesson .
a review of risk helped us understand the different deposit .
the report about the nurse explains the health in detail .
the consumer compared the offering after checking the price .
```

#### Temperature 1.2

```text
our school has a question about the new educator and lesson .
a review of risk helped us understand the different deposit .
the report about the nurse explains the health in detail .
the consumer compared the offering after checking the price .
```

### Actual chat transcript

Model SHA-256: `a0fb06406d96c728860c40960c8d849779f3531b29b210e1c75f3f02f692d7af`; completed steps: 3000. Each prompt starts with fresh context.

| Prompt | Response | Unknown prompt words |
| --- | --- | --- |
| the customer | selected the item after checking the price . |  |
| the professor | selected the merchandise after checking the price . |  |
| the student | reviewed the product instructor during a discussion of delivery . |  |
| the idol | the important peach with another banana at the kitchen . | idol |
| Yujin | the new professor helped us understand the different apple . | yujin |
| class | [empty response] | class |
| student | report about the therapist explains the patient in detail . |  |
| family | the bank focused on risk and the local bond . | family |
| family | the hospital focused on care and the new therapist . | family |

## expanded

Full archive: [expanded-results.zip](expanded-results.zip). Extract it to obtain `results/expanded/`.

### Full fixed-panel loss history

| Step | Training loss | Validation loss |
| --- | --- | --- |
| 0 | 5.895987510681152 | 5.831655502319336 |
| 1500 | 0.6977213621139526 | 0.711374819278717 |
| 3000 | 0.6876829266548157 | 0.7038069367408752 |

### Sample timeline

#### Step 0

```text
question firmness class rope buy finishes bank hall tutor dirty less artist application same not package deposit focused to arrived driver have plate risk fruit hospital accepted car brand rather no our
water order drank task tools review seat service accepted they discussion prefers access became apart credit room borrow long data us discussion received reviewed breeze way select hard station has customers light
lift take prefers apple apart nothing was is scale therapist system chose route offering store physician hard final merchandise instructor application empty instructor bread us window brand interest reviewed a until take
sell nothing tools not choose same exchanged is focused missing dark shop dentist care customers loan learning from seat bicycle focused describe reviewed came explains use an use and brand noisy than
```

#### Step 1500

```text
today the market focused on delivery and the different item .
the local car was mentioned in the travel report yesterday .
a review of health helped us understand the important doctor .
the report about the educator explains the lesson in detail .
```

#### Step 3000

```text
today the market focused on delivery and the different item .
the local orange was mentioned in the juice report yesterday .
a review of health helped us understand the important doctor .
the report about the educator explains the student in detail .
```

### Before/after evaluation summaries

#### untrained

| Group/category | Correct / all | Scorable | All-case success | Scorable accuracy | Coverage |
| --- | --- | --- | --- | --- | --- |
| overall | 6/48 | 26 | 12.5% | 23.1% | 54.2% |
| extend_corpus | 0/24 | 2 | 0.0% | 0.0% | 8.3% |
| starter_patterns | 3/16 | 16 | 18.8% | 18.8% | 100.0% |
| starter_transfer | 3/8 | 8 | 37.5% | 37.5% | 100.0% |
| categories_and_analogies | 0/3 | 0 | 0.0% | N/A | 0.0% |
| domain_context | 1/8 | 8 | 12.5% | 12.5% | 100.0% |
| domain_place | 2/8 | 8 | 25.0% | 25.0% | 100.0% |
| everyday_knowledge | 0/3 | 0 | 0.0% | N/A | 0.0% |
| grammar | 0/3 | 0 | 0.0% | N/A | 0.0% |
| negation | 0/3 | 0 | 0.0% | N/A | 0.0% |
| new_wording | 3/8 | 8 | 37.5% | 37.5% | 100.0% |
| opposites | 0/3 | 2 | 0.0% | 0.0% | 66.7% |
| reference | 0/3 | 0 | 0.0% | N/A | 0.0% |
| sequence | 0/3 | 0 | 0.0% | N/A | 0.0% |
| spatial_relations | 0/3 | 0 | 0.0% | N/A | 0.0% |

#### final

| Group/category | Correct / all | Scorable | All-case success | Scorable accuracy | Coverage |
| --- | --- | --- | --- | --- | --- |
| overall | 23/48 | 26 | 47.9% | 88.5% | 54.2% |
| extend_corpus | 1/24 | 2 | 4.2% | 50.0% | 8.3% |
| starter_patterns | 16/16 | 16 | 100.0% | 100.0% | 100.0% |
| starter_transfer | 6/8 | 8 | 75.0% | 75.0% | 100.0% |
| categories_and_analogies | 0/3 | 0 | 0.0% | N/A | 0.0% |
| domain_context | 8/8 | 8 | 100.0% | 100.0% | 100.0% |
| domain_place | 8/8 | 8 | 100.0% | 100.0% | 100.0% |
| everyday_knowledge | 0/3 | 0 | 0.0% | N/A | 0.0% |
| grammar | 0/3 | 0 | 0.0% | N/A | 0.0% |
| negation | 0/3 | 0 | 0.0% | N/A | 0.0% |
| new_wording | 6/8 | 8 | 75.0% | 75.0% | 100.0% |
| opposites | 1/3 | 2 | 33.3% | 50.0% | 66.7% |
| reference | 0/3 | 0 | 0.0% | N/A | 0.0% |
| sequence | 0/3 | 0 | 0.0% | N/A | 0.0% |
| spatial_relations | 0/3 | 0 | 0.0% | N/A | 0.0% |

### Token, vector, gradient and prediction

Selected token: `customer`; ID: **74**. IDs are vocabulary indices, not meanings.

<details><summary>embedding_before (complete saved values)</summary>

```json
[
  0.0052889566868543625,
  -0.01922529935836792,
  -0.002191513543948531,
  -0.02660312131047249,
  0.009699264541268349,
  0.028761766850948334,
  0.004346064757555723,
  -0.005226263776421547,
  0.044469427317380905,
  0.04580643028020859,
  0.019510235637426376,
  -0.009842897765338421,
  0.0004903938388451934,
  0.018352100625634193,
  0.011836141347885132,
  0.005269794259220362,
  0.052174024283885956,
  0.001419785083271563,
  -0.0038833420258015394,
  -0.007490877527743578,
  0.0065193031914532185,
  0.014301599934697151,
  0.0120931351557374,
  0.00030143538606353104,
  -0.01955217868089676,
  -0.00675915228202939,
  -0.01981429010629654,
  -0.011974649503827095,
  0.0011372334556654096,
  0.0055724321864545345,
  -0.00274399621412158,
  0.02053980343043804,
  0.021544329822063446,
  0.012342486530542374,
  0.03212741017341614,
  0.019040655344724655,
  -0.004900495987385511,
  -0.014178835786879063,
  -0.03586333617568016,
  0.036883555352687836,
  0.010738387703895569,
  0.011499566957354546,
  0.0062422375194728374,
  0.004677486605942249,
  0.013949977234005928,
  0.02688637189567089,
  0.015211954712867737,
  -0.01236721407622099,
  -0.042481083422899246,
  -0.01472429372370243,
  0.006743118166923523,
  -0.008922525681555271,
  -0.002851338591426611,
  0.02197604812681675,
  -0.01725718006491661,
  0.040033191442489624,
  -0.011744939722120762,
  0.010781319811940193,
  0.053442396223545074,
  -0.014106105081737041,
  0.02346823178231716,
  -0.006230342201888561,
  0.006206076592206955,
  -0.018828025087714195
]
```

</details>

<details><summary>embedding_after (complete saved values)</summary>

```json
[
  0.03110417164862156,
  -0.15498144924640656,
  -0.10790548473596573,
  0.022297076880931854,
  -0.047574348747730255,
  -0.07936540246009827,
  0.08099231123924255,
  -0.06219536066055298,
  0.156067356467247,
  0.1007544994354248,
  -0.03233882412314415,
  0.014146478846669197,
  -0.0150520671159029,
  0.0013508233241736889,
  -0.014122038148343563,
  0.03133075311779976,
  -0.0006979507743380964,
  -0.0412413664162159,
  -0.03613211214542389,
  -0.053706176578998566,
  -0.001951870508491993,
  -0.06947369873523712,
  0.10188696533441544,
  -0.02348577417433262,
  -0.12064960598945618,
  -0.003271035850048065,
  -0.09311480075120926,
  0.07320619374513626,
  0.13631083071231842,
  0.06605548411607742,
  -0.07938404381275177,
  0.15978476405143738,
  0.08271146565675735,
  -0.12170866131782532,
  0.0018449559574946761,
  -0.027771998196840286,
  0.0411088801920414,
  0.11971835792064667,
  -0.12096790969371796,
  0.14309121668338776,
  0.011185838840901852,
  -0.15102419257164001,
  0.05377643555402756,
  0.16261102259159088,
  0.05826175957918167,
  0.036135029047727585,
  -0.021881945431232452,
  -0.10853737592697144,
  -0.17631740868091583,
  -0.06331624835729599,
  -0.07834067195653915,
  -0.0551862008869648,
  -0.005897665861994028,
  0.08181869983673096,
  -0.03966684266924858,
  0.1726013869047165,
  -0.09122415632009506,
  0.06383497267961502,
  0.1426086127758026,
  0.09209833294153214,
  0.11910930275917053,
  -0.056614797562360764,
  0.03738471865653992,
  -0.015584162436425686
]
```

</details>

<details><summary>first_update (complete saved values)</summary>

```json
{
  "token": "customer",
  "coordinate": 0,
  "before": 0.0052889566868543625,
  "gradient": -0.0012052644742652774,
  "learning_rate": 1e-05,
  "after": 0.005298955831676722
}
```

</details>

Top next-token probabilities for `the customer`:

| Stage | Token | Probability |
| --- | --- | --- |
| before | customer | 0.006008 |
| before | doing | 0.004764 |
| before | class | 0.004480 |
| before | <BOS> | 0.004439 |
| before | afterward | 0.004399 |
| after | compared | 0.194991 |
| after | ordered | 0.176423 |
| after | selected | 0.167710 |
| after | returned | 0.141187 |
| after | recommended | 0.138341 |

| State | Nearest customer neighbors (64-dimensional cosine) |
| --- | --- |
| initial | support (0.3474), team (0.3019), doing (0.2909) |
| final | client (0.9604), subscriber (0.9577), consumer (0.9553) |

Saved attention rows (causal lower-triangular matrix):

```json
[
  [
    1.0,
    0.0,
    0.0
  ],
  [
    0.27842968702316284,
    0.7215702533721924,
    0.0
  ],
  [
    0.3573991358280182,
    0.29806262254714966,
    0.34453830122947693
  ]
]
```

### Temperature samples

#### Temperature 0.3

```text
today the market focused on delivery and the different item .
the local orange was mentioned in the juice report yesterday .
the new apple was mentioned in the juice report yesterday .
the report about the educator explains the student in detail .
```

#### Temperature 0.8

```text
today the market focused on delivery and the different item .
the local orange was mentioned in the juice report yesterday .
a review of health helped us understand the important doctor .
the report about the educator explains the student in detail .
```

#### Temperature 1.2

```text
today the market focused on delivery and the different item .
the local consumer was mentioned in the service report yesterday .
a review of health helped us understand the important doctor .
the report about the educator explains the student in detail .
```

### Actual chat transcript

Model SHA-256: `18d35daf64cd8551a2df487befb20490c86a6007b1c1d23cacb9e2df46d20abd`; completed steps: 3000. Each prompt starts with fresh context.

| Prompt | Response | Unknown prompt words |
| --- | --- | --- |
| family | important system was mentioned in the data report yesterday . | family |
| children | important deposit was mentioned in the payment report yesterday . | children |
| customer | and did not opposite levels of a discussion of service . |  |
| student | and lesson describe opposite levels of fruit . |  |
| the teacher | carried a green bag instead of a market . |  |

## expanded2

Full archive: [expanded2-results.zip](expanded2-results.zip). Extract it to obtain `results/expanded2/`.

### Full fixed-panel loss history

| Step | Training loss | Validation loss |
| --- | --- | --- |
| 0 | 6.156435489654541 | 6.163686275482178 |
| 1500 | 0.6997037529945374 | 0.7002544403076172 |
| 3000 | 0.6911444664001465 | 0.6987431049346924 |

### Sample timeline

#### Step 0

```text
library open red <BOS> hospital frame removed car afternoon week not expensive orange recommended relative mentioned insects pressure interest table helps together chair together system passed access report bowl an prefers understand
receive hospital different full plants starts plate product rejected platform artist solve brings cake shop served fresh green late space service food moves attract drank seeds exchanged
while teacher receive cold place drummer finished doctor system musicians cold road customer soil customer apples notebook deposit mixes classroom therapist paper delivery listens hospital at introduces educator late tools select soft
sell peach break important contained coat contained station caring shares round health seat shopper end in includes allows light service bowl regular discusses became carried with finish from pears cleanliness cashier writes
```

#### Step 1500

```text
the important mango was mentioned in the harvest report yesterday .
our school has a question about the local educator and learning .
we learned about the important physician during a discussion of treatment .
we learned about the new banana during a discussion of taste .
```

#### Step 3000

```text
the report about the subscriber explains the order in detail .
our school has a question about the local educator and learning .
we learned about the important physician during a discussion of treatment .
the report about the brand explains the delivery in detail .
```

### Before/after evaluation summaries

#### untrained

| Group/category | Correct / all | Scorable | All-case success | Scorable accuracy | Coverage |
| --- | --- | --- | --- | --- | --- |
| overall | 5/48 | 26 | 10.4% | 19.2% | 54.2% |
| extend_corpus | 1/24 | 2 | 4.2% | 50.0% | 8.3% |
| starter_patterns | 2/16 | 16 | 12.5% | 12.5% | 100.0% |
| starter_transfer | 2/8 | 8 | 25.0% | 25.0% | 100.0% |
| categories_and_analogies | 0/3 | 0 | 0.0% | N/A | 0.0% |
| domain_context | 1/8 | 8 | 12.5% | 12.5% | 100.0% |
| domain_place | 1/8 | 8 | 12.5% | 12.5% | 100.0% |
| everyday_knowledge | 0/3 | 0 | 0.0% | N/A | 0.0% |
| grammar | 0/3 | 0 | 0.0% | N/A | 0.0% |
| negation | 0/3 | 0 | 0.0% | N/A | 0.0% |
| new_wording | 2/8 | 8 | 25.0% | 25.0% | 100.0% |
| opposites | 1/3 | 2 | 33.3% | 50.0% | 66.7% |
| reference | 0/3 | 0 | 0.0% | N/A | 0.0% |
| sequence | 0/3 | 0 | 0.0% | N/A | 0.0% |
| spatial_relations | 0/3 | 0 | 0.0% | N/A | 0.0% |

#### final

| Group/category | Correct / all | Scorable | All-case success | Scorable accuracy | Coverage |
| --- | --- | --- | --- | --- | --- |
| overall | 21/48 | 26 | 43.8% | 80.8% | 54.2% |
| extend_corpus | 1/24 | 2 | 4.2% | 50.0% | 8.3% |
| starter_patterns | 16/16 | 16 | 100.0% | 100.0% | 100.0% |
| starter_transfer | 4/8 | 8 | 50.0% | 50.0% | 100.0% |
| categories_and_analogies | 0/3 | 0 | 0.0% | N/A | 0.0% |
| domain_context | 8/8 | 8 | 100.0% | 100.0% | 100.0% |
| domain_place | 8/8 | 8 | 100.0% | 100.0% | 100.0% |
| everyday_knowledge | 0/3 | 0 | 0.0% | N/A | 0.0% |
| grammar | 0/3 | 0 | 0.0% | N/A | 0.0% |
| negation | 0/3 | 0 | 0.0% | N/A | 0.0% |
| new_wording | 4/8 | 8 | 50.0% | 50.0% | 100.0% |
| opposites | 1/3 | 2 | 33.3% | 50.0% | 66.7% |
| reference | 0/3 | 0 | 0.0% | N/A | 0.0% |
| sequence | 0/3 | 0 | 0.0% | N/A | 0.0% |
| spatial_relations | 0/3 | 0 | 0.0% | N/A | 0.0% |

### Token, vector, gradient and prediction

Selected token: `customer`; ID: **104**. IDs are vocabulary indices, not meanings.

<details><summary>embedding_before (complete saved values)</summary>

```json
[
  0.012136144563555717,
  -0.013438301160931587,
  0.009346249513328075,
  -0.01820254884660244,
  -0.014388476498425007,
  -0.013512828387320042,
  -0.03370789811015129,
  0.024410486221313477,
  0.014209813438355923,
  -0.016482962295413017,
  -0.0030740138608962297,
  0.028340546414256096,
  -0.0009952017571777105,
  0.017754916101694107,
  -0.013089197687804699,
  0.022344158962368965,
  -0.02192390337586403,
  -0.022103190422058105,
  -0.022930869832634926,
  -0.013906726613640785,
  -0.005534253548830748,
  0.010830925777554512,
  0.02680004946887493,
  0.01061221957206726,
  -0.004430655390024185,
  -0.0009022040176205337,
  -0.0032649103086441755,
  -0.04055742546916008,
  0.008429880253970623,
  0.029586659744381905,
  -0.009710470214486122,
  0.016865024343132973,
  -0.046258941292762756,
  0.001067587872967124,
  0.004579158965498209,
  0.00867931917309761,
  -0.009240204468369484,
  -0.024300269782543182,
  0.022370247170329094,
  0.010527879931032658,
  -0.009157350286841393,
  -0.03255215659737587,
  0.026552600786089897,
  -0.0053620897233486176,
  7.923333760118112e-05,
  0.009855299256742,
  -0.018335552886128426,
  0.004089649301022291,
  0.01000931952148676,
  0.015491344965994358,
  0.012221661396324635,
  0.013599958270788193,
  0.011145121417939663,
  0.022066783159971237,
  -0.002619159175083041,
  0.03515245020389557,
  0.03532024845480919,
  -0.011196709237992764,
  -0.0033055441454052925,
  -0.01141366921365261,
  0.027751177549362183,
  -0.00010383060725871474,
  0.002418159507215023,
  -0.01545810978859663
]
```

</details>

<details><summary>embedding_after (complete saved values)</summary>

```json
[
  -0.13022392988204956,
  0.04242035746574402,
  0.04547746852040291,
  0.10472310334444046,
  0.12127148360013962,
  -0.02287750504910946,
  -0.09221542626619339,
  0.05985840782523155,
  -0.05384890362620354,
  -0.014815590344369411,
  0.05624639242887497,
  0.15636813640594482,
  -0.12001851946115494,
  -0.01519425306469202,
  0.08190760016441345,
  0.07640288770198822,
  -0.05251486971974373,
  0.04909425228834152,
  -0.03615744784474373,
  -0.08841478079557419,
  0.04138965532183647,
  -0.03631668910384178,
  0.048537857830524445,
  0.06841209530830383,
  -0.0750206932425499,
  -0.10163146257400513,
  0.059995751827955246,
  -0.07463603466749191,
  0.1119358092546463,
  0.042443715035915375,
  0.05722876638174057,
  -0.016934260725975037,
  -0.13040007650852203,
  0.020825203508138657,
  0.03825107216835022,
  -0.005698233377188444,
  0.08426791429519653,
  0.023774435743689537,
  0.01244563888758421,
  0.034960076212882996,
  -0.17709092795848846,
  -0.07212865352630615,
  -0.10408126562833786,
  -0.09633173793554306,
  -0.081254743039608,
  0.12622931599617004,
  -0.11508285254240036,
  0.059354569762945175,
  -0.0009328076266683638,
  0.04287277162075043,
  -0.04531710967421532,
  -0.12223870307207108,
  0.051368460059165955,
  0.12353742122650146,
  -0.030148914083838463,
  -0.09463749080896378,
  0.12125258147716522,
  0.07197859138250351,
  -0.1199963241815567,
  0.10971798002719879,
  0.13030627369880676,
  -0.055321335792541504,
  -0.1042962446808815,
  -0.002484417287632823
]
```

</details>

<details><summary>first_update (complete saved values)</summary>

```json
{
  "token": "customer",
  "coordinate": 0,
  "before": 0.012136144563555717,
  "gradient": 6.299065717030317e-05,
  "learning_rate": 1e-05,
  "after": 0.012126147747039795
}
```

</details>

Top next-token probabilities for `the customer`:

| Stage | Token | Probability |
| --- | --- | --- |
| before | customer | 0.004411 |
| before | drank | 0.003410 |
| before | more | 0.003218 |
| before | speeds | 0.003190 |
| before | milk | 0.003134 |
| after | returned | 0.191359 |
| after | selected | 0.173791 |
| after | recommended | 0.151831 |
| after | ordered | 0.150725 |
| after | compared | 0.136191 |

| State | Nearest customer neighbors (64-dimensional cosine) |
| --- | --- |
| initial | speeds (0.3362), morning (0.3226), drank (0.3028) |
| final | subscriber (0.9637), shopper (0.9537), consumer (0.9510) |

Saved attention rows (causal lower-triangular matrix):

```json
[
  [
    1.0,
    0.0,
    0.0
  ],
  [
    0.48423510789871216,
    0.5157648921012878,
    0.0
  ],
  [
    0.2986118197441101,
    0.3304429352283478,
    0.3709453344345093
  ]
]
```

### Temperature samples

#### Temperature 0.3

```text
the important mango was mentioned in the harvest report yesterday .
our school has a question about the local educator and learning .
we learned about the important physician during a discussion of treatment .
the report about the brand explains the delivery in detail .
```

#### Temperature 0.8

```text
the report about the subscriber explains the order in detail .
our school has a question about the local educator and learning .
we learned about the important physician during a discussion of treatment .
the report about the brand explains the delivery in detail .
```

#### Temperature 1.2

```text
the open during feel assignment frame and did not in not expensive was the relative choice .
they compared the local instructor with another professor at the school .
the customer selected the brand after checking the price .
today the hospital focused on treatment and the important physician .
```

### Actual chat transcript

Model SHA-256: `2092cd8c14fe3e73c3437aef1e47788ae770e6f86eb9cbe8f4d606794777a240`; completed steps: 3000. Each prompt starts with fresh context.

| Prompt | Response | Unknown prompt words |
| --- | --- | --- |
| the teacher | chose a bus and did not removed the station . |  |
| the customer | returned the merchandise after checking the price . |  |
| the student | consumer ordered the store drink . |  |
| the baby | about the hand than mentioned in the frame . | baby |
