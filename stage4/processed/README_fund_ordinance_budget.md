# 基金条例・予算・決算 bottom-up ALM データセット

調査基準日：2026-09-16

このディレクトリの基金別データは、Stage 4のトップダウン型ALM（基金繰替実績から必要流動性を推計）を、個々の基金の用途・条例・法定制約・予算上の取崩し・非現金資産からボトムアップで検証するための下調べデータである。

## 最新ファイル

- `ehime_fund_current_universe_R8.csv`
  - R8予算、R6決算、個別基金公表資料等から現存証拠を確認したworking universe。
  - 43基金を収録するが、「愛媛県の法的な全基金数＝43」とは断定しない。
- `ehime_R8_fund_withdrawals.csv`
  - R8一般会計基金繰入を基金別に構造化。
  - 32基金、合計35,185,764千円＝351.85764億円。
- `ehime_fund_ordinance_liquidity_register.csv`
  - 主要基金について、用途、法定・政策フロア、終期、R8取崩、ALM解釈、推奨満期bucketを整理。
- `ehime_fund_statutory_sunset_rules.csv`
  - 法定最少額、政策フロア、事業終期、国庫返還、非現金元本等のハード制約を抽出。
- `ehime_disaster_relief_statutory_minimum_R8.csv`
  - 災害救助基金のR8法定最少額を公表税収実績から再計算。
  - R4～R6の普通税から法定外普通税（核燃料税）を控除した平均172,150,257.333千円×0.5%＝860,751.287千円、約8.607513億円。
  - これは県が「R8法定最少額」として直接公表した数値ではなく、災害救助法第23条と県税決算値による再計算値。
- `ehime_fund_historical_universe_H23_status_map.csv`
  - H23包括外部監査の48基金・積立金をhistorical universeとして、2026時点の現存証拠・改称・確認済み廃止・要確認を整理。
- `ehime_fund_additional_ordinance_findings.csv`
  - 中核産業人材確保支援、中山間ふるさと保全、社会福祉施設整備、漁業振興資金積立金等の追加条例・制度調査。

## 重要な計算原則

基金別の債券運用余地は、基金残高そのものではなく、原則として次式で評価する。

`Core investable_i = cash balance_i - statutory/policy floor_i - approved 12m withdrawals_i - committed 1-3y pipeline_i - stress reserve_i - revolving/non-cash requirements_i`

美術品、土地、貸付金、株式等の非現金資産は、最初から債券化可能現金の母数に含めない。

## 重要な区別

- **法定最少額**：災害救助基金など。ハード制約。
- **政策フロア**：財源対策用基金400億円規模など。県の政策目標であり法定最低額とは異なる。
- **設置時積立額・基金額**：企業立地促進基金50億円、地域環境保全基金4億円等。条例上の金額を最低残高と自動的に解釈しない。
- **事業終期**：公立学校情報機器整備基金、安心こども基金等。終期を超える満期設定を避ける。
- **回転基金・非現金基金**：土地開発、企業立地資金貸付、美術品等取得、医師確保奨学、「三浦保」愛基金等。現金部分だけをALM対象とする。

## R8取崩額の扱い

R8一般会計の基金繰入351.85764億円は、近未来の用途制約を示す重要な情報だが、R6末基金総額1,302.28億円から機械的に一括控除しない。R6末からR8までの新設・追加積立基金が含まれ、時点・母集団が異なるためである。R7末又はR8期首の基金別現金残高へ接続して利用する。

## Stage 4への接続

現行の保守151.27億円、標準435.32億円、積極574.70億円は、全体の年度内資金繰りからみたouter envelopeとして維持する。最終的な債券運用可能額は、基金別bottom-up制約を適用したcore investableの合計と比較して検証する。

標準ケース435.32億円をbottom-upで支えられなければ、標準ケースは下方修正する。支えられれば、トップダウンの流動性制約と基金別の用途制約を同時に満たしたことになる。

## 関連資料

- `../reports/fund_ordinance_budget_research_note.md`
- `../reports/fund_ordinance_budget_research_addendum_20260916.md`
- `../qa/fund_ordinance_budget_research_audit.md`
- `../qa/fund_ordinance_budget_completion_gate.md`
- `../sources/source_dictionary.csv`
- `../sources/fund_ordinance_budget_source_dictionary.csv`
