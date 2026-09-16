# Stage 4 — 愛媛県基金の債券運用余地・ALM分析

調査基準日：2026-09-15

Stage 4 は、Stage 3の全国比較をベンチマークとして、愛媛県のR3～R6基金繰替運用、R2～R6基金残高、基金別取崩構造、財源対策用基金、災害ストレスを統合し、必要流動性と債券運用可能レンジを推計する。

2026-09-16追補として、愛媛県「財政運営基本方針」（R5～R8）をALM制約へ明示的に統合した。財源対策用基金400億円規模、中期財政見通しR6～R8財源不足333億円、豪雨時183億円、地方交付税減少407億円、県有施設更新費平均180億円/年等は、役割を分けてモデルへ反映する。

さらに2026-09-16の基金別下調べとして、条例・法令・R8当初予算・R6決算・基金個別公表資料を調査し、基金ごとの用途、法定・政策上の保持制約、事業終期、予算上の取崩し、非現金資産を構造化した。これにより、全体キャッシュフローから求めるtop-down ALMに加えて、基金別用途から求めるbottom-up ALMで検証できる基礎を整備した。

## 最終レポート

- `reports/ehime_fund_bond_capacity_ALM_R7.md`
  - 「愛媛県基金の債券運用余地 ―必要流動性、基金繰替運用、ALM及び全国比較からみた適正ポートフォリオ―」
- `reports/fiscal_management_policy_integration_note.md`
  - 財政運営基本方針を流動性フロア・中期財政圧力・ストレステスト・予定負債へ分解した追補メモ
- `reports/fund_ordinance_budget_research_note.md`
  - 条例・予算・決算に基づく基金別用途・保持制約・終期・非現金資産とbottom-up ALMの調査メモ

## 主要成果物

- `processed/ehime_fund_substitution_R3_R6_long.csv` — R3～R6基金別・期間別繰替64行
- `processed/ehime_fund_substitution_period_totals.csv` — 16期間合計
- `processed/ehime_fund_substitution_stats.csv` — 年度別最大・最小・平均・中央値・期間加重平均
- `processed/ehime_fund_substitution_seasonal_stats.csv` — 4～5月・夏期・秋期・年度末の季節統計
- `processed/ehime_fund_balance_R2_R6.csv` — 基金総額・主要基金残高
- `processed/ehime_major_fund_5yr_long.csv` — 主要基金5年推移・確認できた積立取崩
- `processed/ehime_other_specific_fund_flows_R2_R6.csv` — その他特定目的基金の積立取崩
- `processed/ehime_fund_classification.csv` — 基金のALM類型
- `processed/ehime_liquidity_distribution.csv` — 16期間の分布統計
- `processed/ehime_liquidity_bond_scenarios.csv` — 保守・標準・積極3ケース
- `processed/ehime_income_sensitivity.csv` — 一般的な増収感応度
- `processed/ehime_scenario_income_sensitivity.csv` — 3ケース別増収感応度
- `processed/ehime_national_benchmark.csv` — R7直接比較県との外部妥当性チェック
- `processed/evidence_table.csv` — 学術・国際実務エビデンス
- `processed/ehime_fiscal_management_policy_constraints.csv` — 財政運営基本方針のALM制約一覧
- `processed/ehime_medium_term_fiscal_outlook_R6_R8.csv` — R6～R8財源不足122・113・98億円
- `processed/ehime_fiscal_buffer_policy_history.csv` — 財源対策用基金の実績・400億円目標・R7見込み
- `processed/ehime_policy_overlay_scenario_check.csv` — 3ケースと政策制約の整合確認
- `processed/ehime_fund_current_universe_R8.csv` — R8予算・R6決算等から現存証拠を確認したworking current universe
- `processed/ehime_R8_fund_withdrawals.csv` — R8一般会計の基金繰入32基金・計351.85764億円
- `processed/ehime_fund_ordinance_liquidity_register.csv` — 主要基金の用途・保持制約・推奨満期bucket
- `processed/ehime_fund_statutory_sunset_rules.csv` — 法定最少額・政策フロア・終期・国庫返還・非現金元本等のハード制約
- `processed/ehime_fund_historical_universe_H23_status_map.csv` — H23包括外部監査48基金と2026 working statusの対応
- `charts/fig1`～`fig9` — 指定9図
- `sources/source_dictionary.csv` — Source ID・一次資料
- `qa/final_audit.md` — Stage4最終監査
- `qa/fiscal_policy_integration_audit.md` — 財政運営基本方針統合監査
- `qa/fund_ordinance_budget_research_audit.md` — 条例・予算・基金別制約調査監査

## 財政運営基本方針を踏まえた追加ルール

財源対策用基金400億円規模は、普通預金だけに限定せずとも、cash・near-cash・需要時期までに満期償還する短期安全資産の範囲で常時ring-fenceする政策上の流動性フロアとして扱う。

西日本豪雨183億円、H16～18地方交付税減少407億円、R6～R8財源不足333億円は相互に重複する財政リスクであり、400億円へ単純加算しない。183・407億円はストレステスト、333億円は1～3年満期ラダー、県有施設更新費平均180億円/年は中長期予定負債の設計に利用する。

現行3ケースの1年以内流動性資産は、保守1,151.01億円、標準968.01億円、積極932.76億円であり、いずれも400億円政策フロアを上回る。このため、現時点では債券運用可能額の数値自体は変更しない。ただし、財源対策用基金400億円相当を普通の中長期コア運用へ回さないという基金別制約を追加する。

## 条例・予算・決算を踏まえたbottom-up ALM

基金別の債券運用余地は、基金残高そのものではなく、原則として次式で検証する。

`Core investable_i = cash balance_i - statutory/policy floor_i - approved 12m withdrawals_i - committed 1-3y pipeline_i - stress reserve_i - revolving/non-cash requirements_i`

R8一般会計では32基金から合計351.85764億円の基金繰入が予算化されている。ただし、R6末基金総額とR8予算は基準時点・母集団が異なり、新設基金も含むため、この351.86億円をR6基金総額から一括控除しない。基金別R7末又はR8期首現金残高と接続して使用する。

法定・制度上の制約が特に強い基金は別管理する。災害救助基金は災害救助法上の最少額、財源対策用基金は400億円規模の政策フロア、公立学校情報機器整備基金等は明示された事業終期・廃止日、国保・後期高齢者医療等の財政安定化基金は不足時の貸付・交付余力を優先する。

また、美術品等取得基金、医師確保奨学基金、「三浦保」愛基金、土地開発基金等は美術品・貸付金・株式・土地等の非現金資産を含むため、基金額全体を債券化可能現金とみなさない。

現行の保守・標準・積極3ケースは全体資金繰りからみたouter envelopeとして維持し、最終レポート改訂時には、この基金別bottom-up制約の合計が標準ケース435.32億円を支えられるかを再検証する。

## 中心結果

R6基金総額1,302.28億円を基準に、公表情報だけで構築した政策レンジは次のとおり。

- 保守：債券151.27億円、11.6％
- 標準：債券435.32億円、33.4％
- 積極：債券574.70億円、44.1％

標準ケースは、過去最大基金繰替968.01億円を、即時現金・near-cash・1年以内満期債で100％カバーする。これは統計的な最適比率ではなく、ALMの政策設計レンジである。

R3～R6の基金繰替は16期間で203.51～968.01億円。季節平均は4～5月775.72億円、夏期325.31億円、秋期614.24億円、年度末782.29億円であり、ピーク額を365日すべて即時現金で持つ必要性は確認できない。一方、基金が年度内資金繰りに大きく使われているため、全国の高債券比率県をそのまま模倣することもできない。

2026-09-15時点でR7基金全体の実際債券残高は公表資料から確定できないため、R6値で代替していない。R7財源対策用基金残高436億円見込みは補助事実としてのみ扱う。

Stage4最終判定：**FINAL EHIME ALM REPORT QA PASS**  
基金条例・予算調査判定：**FUND ORDINANCE/BUDGET RESEARCH QA PASS**
