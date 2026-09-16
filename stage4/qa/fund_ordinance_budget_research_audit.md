# 愛媛県基金 条例・予算・決算調査 QA

調査基準日：2026-09-16

| check | result | detail |
|---|---|---|
| historical universe | PASS | H23包括外部監査の48基金・積立金を母集団として保持 |
| current working universe | PASS | R8予算・R6決算・個別公表資料から43基金の現存証拠をworking universe化。全基金43とは断定しない |
| R8 fund withdrawals | PASS | 一般会計基金繰入32基金、35,185,764千円＝351.85764億円 |
| fund-level ordinance/liquidity register | PASS | 主要30基金について目的・保持制約・推奨満期bucketを整理 |
| statutory/sunset hard rules | PASS | 災害救助基金、終了期限基金、非現金・回転基金等を別表化 |
| disaster relief statutory formula | PASS | 災害救助法23条の式「当該年度の前年度の前三年間における普通税（法定外普通税除外）決算平均×0.5%」を反映 |
| disaster relief R8 floor | PASS | R4-R6普通税総額から法定外普通税の核燃料税を控除し、R8概算法定最少額860,751.287千円＝8.607513億円を再計算 |
| disaster relief R8 budget | PASS | R8当初予算の災害救助基金積立金4,342千円と法定必要額への積立目的を確認 |
| disaster relief permitted assets | PASS | 法26条の預金・国債地方債等・救助物資事前購入を反映 |
| sunset funds | PASS | 公立学校情報機器整備基金R11-03-31廃止、安心こども基金R12-06解散見込み、県立高校等教育改革R8-R10を反映 |
| policy floor | PASS | 財源対策用基金400億円規模は法定最低額と区別して政策フロアとして扱う |
| non-cash principal | PASS | 美術品等取得基金、美術品等／現金を分離。医師確保奨学基金、貸付金／現金を分離。三浦保愛基金、寄附株式元本をbond-convertible cashから除外 |
| revolving assets | PASS | 土地開発・企業立地資金貸付等は基金総額全体を債券運用可能現金とみなさない |
| R6 vs R8 basis control | PASS | R8取崩351.86億円をR6基金総額から機械的に控除しない。基金別期首残高との接続が必要と明記 |
| unknown status handling | PASS | H23母集団のうち現行証拠未確認基金はneeds_status_checkとし、廃止と推定しない |
| abolished funds | PASS | 森林整備地域活動支援基金、森林そ生緊急対策基金のみ確認できた廃止条例根拠でabolishedとした |
| fact / interpretation separation | PASS | 公表事実、ALM解釈、推奨bucket、confidenceを別列に分離 |
| minimum-balance discipline | PASS | 条例の積立額・基金額を自動的に最低保持額へ読み替えない |
| top-down scenario preservation | PASS | 現行151.27 / 435.32 / 574.70億円はouter envelopeとして維持し、bottom-up test完了前に改変しない |
| bottom-up formula | PASS | cash balanceから法定・政策フロア、12か月支出、1-3年pipeline、stress、非現金・回転要件を控除する式を定義 |
| public-only | PASS | 愛媛県公式、e-Gov、既存Stage4公開資料のみ。内部資料不使用 |

## 判定

**FUND ORDINANCE/BUDGET RESEARCH QA PASS**

## 重要な限定

- `ehime_fund_current_universe_R8.csv` の43基金は、R8予算・R6決算・個別公表資料で現存証拠を確認したworking universeであり、愛媛県の法的な全基金数を断定するものではない。
- R8基金繰入351.85764億円は一般会計の予算上の取崩予定であり、実支出額・基金期首残高とは異なる。
- 災害救助基金のR8法定最少額8.607513億円は、県公表のR4～R6普通税収入済額から災害救助法上除外される法定外普通税（核燃料税）を控除して算出した再計算値であり、県が公表した「R8法定最少額」という表記値そのものではない。R8予算の積立金4,342千円とは整合的に参照するが、基金現在高の完全な再構成は別途必要である。
- 各基金の条例にある「最も確実かつ有利な方法」は、それだけで個別債券商品の購入権限を断定する根拠にしない。地方自治法、県の公金運用規程等との整合確認を残す。
- R7末又はR8期首の基金別現金残高が揃うまでは、bottom-upの総債券運用可能額を確定しない。
