# Client-Ready Review Checklist

このチェックリストは、`ehime_fund_bond_management_consulting_report_R7_R8.md` の次版をSenior Manager Reviewからclient-readyへ移す際に使用する。

## A. Executive Summary

- [ ] 中心的なmanagement questionが1文で明示されている。
- [ ] 主要結論が5分以内で把握できる。
- [ ] 全国比較、愛媛県の流動性、運用余地、実装条件が一つのストーリーになっている。
- [ ] 151.27 / 435.32 / 574.70億円が「実額推計」ではなくscenario envelopeであることが明確。
- [ ] 435.32億円を採る条件と、採らない条件が分かる。
- [ ] R7/R8基金別現金残高が未反映であることの意味が明確。

## B. Evidence integrity

- [ ] 主要数字に一次資料又は明確な出典がある。
- [ ] R6 / R7 / R8の時点が混同されていない。
- [ ] 年間平均 / 年度末 / 予算額 / 決算額を区別している。
- [ ] 基金 / 歳計現金 / 公金全体の範囲を区別している。
- [ ] 報道値は原統計と区別している。
- [ ] 愛媛県の非公表実運用を推定していない。
- [ ] 計算式、入力値、丸めが再現可能。
- [ ] 比較不能なデータを同列ランキングしていない。

## C. Benchmarking

- [ ] 全国47都道府県の統一比較とR7個別開示を区別している。
- [ ] 公式類似団体と運用実務peerを区別している。
- [ ] 代表4～6県についてmini case studyがある。
- [ ] 各caseに `What Ehime can learn / What does not transfer` がある。
- [ ] 高い債券比率を自動的にbest practiceとみなしていない。

## D. Liquidity analysis — Chapter 9

- [ ] 16期間の基金繰替分布の意味を本文で説明している。
- [ ] median / P75 / P90 / maxを使い分ける理由がある。
- [ ] 季節性をcash managementへ接続している。
- [ ] peak liquidityとannual average liquidityを区別している。
- [ ] 西日本豪雨等のstressと通常資金需要の重複を確認している。
- [ ] 400億円の財源対策用基金目標を単純加算していない。
- [ ] 即時現金、near-cash、1年以内満期債を別の機能として定義している。

## E. Investable amount — Chapter 10

- [ ] 151.27億円の設計原則が説明されている。
- [ ] 435.32億円の設計原則が説明されている。
- [ ] 574.70億円の設計原則が説明されている。
- [ ] 各ケースのcash forecast能力要件が書かれている。
- [ ] 各ケースのstress coverageが書かれている。
- [ ] 各ケースの不適用条件が書かれている。
- [ ] 435.32億円を変更すべきtriggerが明示されている。
- [ ] bottom-up式が基金別cash balanceから始まっている。
- [ ] R7/R8データ取得後のupdate手順が明確。

## F. Portfolio and maturity ladder — Chapter 11

- [ ] liquidity bucketの役割が明確。
- [ ] 1～3年 / 3～5年 / 5年以上のliability-side rationaleがある。
- [ ] 1年以内の満期を月・四半期に分散する考え方がある。
- [ ] equal ladder以外の代替案を検討している。
- [ ] 10年超を当初抑制する理由がある。
- [ ] 商品構成例を最適比率と誤読させない。
- [ ] eligible instrumentsと県規程確認の必要性を明記。
- [ ] issuer / product / maturity / timingの4種類の集中を区別。
- [ ] 途中売却を必要としない構造が原則になっている。

## G. Economics — Chapter 12

- [ ] 追加収益は代替預金対比で計算している。
- [ ] 年限の異なる利回りを単純比較していない。
- [ ] 0.1～0.5pt sensitivityの意味を文章で解釈している。
- [ ] 運用事務・システム・人材等のimplementation costを定性的に扱う。
- [ ] 収益だけでなくcash visibility、governance、risk controlの便益を扱う。

## H. Risk — Chapter 13

- [ ] interest-rate / market-value risk
- [ ] liquidity risk
- [ ] reinvestment risk
- [ ] credit risk
- [ ] issuer/product concentration risk
- [ ] forecast error risk
- [ ] disaster / supplemental-budget risk
- [ ] operational risk
- [ ] governance / key-person risk
- [ ] 各riskにmonitoring metric又はcontrolが対応している。
- [ ] limit breach時の対応原則がある。

## I. Governance — Chapter 14

- [ ] annual investment policyの構成要素が定義されている。
- [ ] decision ownerとexecution ownerを区別している。
- [ ] independent review又は牽制機能を想定している。
- [ ] exception approvalがある。
- [ ] 13週 / 1年 / 3～5年forecastの更新頻度がある。
- [ ] investment rationaleと市場条件を記録する仕組みがある。
- [ ] 人事異動に耐える標準台帳がある。
- [ ] disclosure項目が定義されている。

## J. Roadmap — Chapter 15

- [ ] 0–90日deliverable
- [ ] 3–6か月deliverable
- [ ] 6–12か月deliverable
- [ ] annual review cycle
- [ ] Data Ready gate
- [ ] Liquidity Model Validated gate
- [ ] Policy Ready gate
- [ ] Pilot Ready gate
- [ ] Scale Decision gate
- [ ] 拡大だけでなく維持・縮小の選択肢がある。

## K. Exhibit review

各主要図表について確認する。

- [ ] titleが結論を述べている。
- [ ] source / definition / unitが分かる。
- [ ] 図の比較対象は定義が揃っている。
- [ ] 本文が数字を繰り返すだけでなく意味を説明する。
- [ ] 図を削除すると論証が弱くなる。
- [ ] 重要図表はExecutive Summaryでも参照可能。

## L. Writing review

- [ ] 各章冒頭に「この章で答える問い」がある。
- [ ] 各主要節がFactで止まっていない。
- [ ] `Fact → Interpretation → Ehime implication → Decision` が主要論点で成立している。
- [ ] 同じ注意書きを過剰に反復していない。
- [ ] 重要でない背景説明が長すぎない。
- [ ] 専門用語は初出で定義。
- [ ] 「可能性がある」「考えられる」を乱用せず、確度を区別。
- [ ] 見出しだけ追ってもストーリーが分かる。

## M. Final gates

### Evidence Integrity Gate

- [ ] PASS

### Decision Logic Gate

- [ ] PASS

### Implementation Gate

- [ ] PASS

### Communication Gate

- [ ] PASS

### Score

- [ ] 85点以上
- [ ] 90点以上を最終目標

**最終判定：**

- [ ] MAJOR REVISION
- [ ] SENIOR MANAGER REVIEW REQUIRED
- [ ] CONDITIONAL CLIENT-READY
- [ ] CLIENT-READY PASS
