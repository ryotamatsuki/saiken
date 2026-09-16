# Public Source Collection QA — 2026-09-16

## Scope completion

| Requested group | Status | Result |
|---|---|---|
| 1. R7決算関係資料 | PARTIAL BY PUBLICATION STATUS | 認定議案、企業会計決算提出、健全化判断比率提出、主要施策成果説明書、事後評価、R8年5月財政事情、R7最終補正関連まで登録。詳細決算5点は未公表確認。 |
| 2. 財政事情5月・11月時系列 | PASS | H14年5月～R8年5月の49件を公式URLでカタログ化。R3～R7の基金繰替借入・返済月パターンを検証。 |
| 3. 現行公金管理方針・関連規程 | PARTIAL BY DISCLOSURE | R8予算編成で現行方針が参照されること、H23監査中の歴史的本文、上位法・基金条例・監査/所管資料を登録。最新版本文は公開検索で未確認。 |
| 4. 主要10～15基金1～5年cash-flow資料 | PASS WITH GAPS EXPLICIT | R8取崩上位15基金（336.78819億円、全32基金取崩の95.717%）について、公開資料・horizon・復元可能性・残存gapを登録。 |

## Integrity checks

- R7決算を「認定済み」と誤記していない。2026-09-16時点では議会提出・審議中として扱う。
- R6詳細決算資料をR7資料として代用していない。
- H23時点の公金管理方針本文を現行最新版と断定していない。
- 将来の基金cash-flowが政策・災害・企業立地等で未確定の場合、推定値を確定支出として作っていない。
- 公開PDFを「公開=再配布可」と解釈せず、原則として公式URLと構造化した派生情報を保存した。
- R8取崩上位15基金の合計・カバレッジはPythonで検算した。

## Immediate usability for rewrite

### Ch.9 Required liquidity

- R7まで延長した基金繰替の年度内タイミング evidence を利用可能。
- 既存Stage4のamount distributionと組み合わせ、size × timeで説明可能。

### Ch.10 Investable amount

- 上位15基金をscheduled / rolling / contingent / fiscal bufferへ分類可能。
- R7末基金別cash balanceだけがなお最大のbottom-up gap。

### Ch.11 Portfolio / ladder

- 学校・県有施設・動物園等の複数年度支出horizonをmaturity matchingの実例へ使用可能。
- 現行公金管理方針の最新eligible assets / limitsは未公表確認のためモデル案として扱う。

### Ch.13–15 Risk / Governance / Roadmap

- 現行方針の存在、H23方針原則、基金条例、運営委員会等を制度面のevidenceとして使用可能。
- 現行具体limit・権限表は確認事項として残す。

## Update triggers

次のいずれかが公表された場合はStage6を更新する。

1. R7歳入歳出決算書
2. R7決算附属書
3. R7財産に関する調書
4. R7決算概要説明書
5. R7部局別一般会計歳入歳出決算額調書
6. 愛媛県公金管理方針の現行最新版本文
7. R9当初予算資料（主要基金の翌年度cash-flow更新）

## QA result

**PUBLIC SOURCE EXPANSION PASS — WITH TWO DISCLOSURE-DEPENDENT GAPS**

The two gaps are:

- R7 detailed settlement package not yet publicly confirmed.
- Current full text of the Ehime Public Funds Management Policy not publicly confirmed.
