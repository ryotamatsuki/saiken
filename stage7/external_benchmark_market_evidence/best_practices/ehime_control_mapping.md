# Ehime Control Mapping — Public Treasury Best Practices

本表はGFOA等の外部best practiceを愛媛県向けの**候補control / metric**へ翻訳したものであり、愛媛県の現行規程・limitを記述するものではない。数値limitは現行規程と実cash-flowを確認するまで設定しない。

| Risk | Best-practice control | Possible Ehime metric | Primary evidence | Implementation note |
|---|---|---|---|---|
| Liquidity | minimum liquidity + maturity matching | 13-week coverage ratio / minimum liquidity compliance | GFOA Cash Forecasts; GFOA Performance | Stage6の基金繰替季節性・P90/peakと接続 |
| Forecast | rolling forecast + actual-vs-forecast | weekly/monthly forecast error | GFOA Cash Forecasts; WB | 13週、12か月、3～5年を別精度で管理 |
| Interest-rate | maturity distribution + WAM/duration monitoring | WAM / duration proxy / maturity concentration | GFOA Market Risk | 初期はmaturity-based proxyから開始可能 |
| Reinvestment | ladder / staggered maturities | annual maturity share / largest maturity-year share | 熊本・東京・兵庫; GFOA | 特定年度への償還集中を避ける |
| Credit | eligible list + issuer qualification | issuer exposure / rating compliance | GFOA Investment Policy; 熊本 | 国債以外を採用する場合に明文化 |
| Concentration | issuer/sector/category diversification | max issuer share / category share | GFOA Diversification | 数値上限はillustrativeに留める |
| Market value | independent mark-to-market | book vs market value / unrealized gain-loss | GFOA Mark-to-Market | 四半期report候補; 満期保有でも時価を把握 |
| Forced sale | cash-flow matched maturities | pre-maturity sale count / realized loss from forced sales | GFOA Performance; Market Risk | 0件を目標とするかは現行policy確認後に決定 |
| Operational | documented trade/settlement/reconciliation process | exception count / unreconciled items | GFOA Investment Policy | segregation of dutiesとcustodyを文書化 |
| Governance | annual policy + periodic performance review | policy review completed / quarterly report timeliness | GFOA Investment Policy; Performance | 年度運用計画と四半期reviewを接続 |
| Counterparty | approved financial institutions / due diligence | approved-list compliance | GFOA Investment Policy; 新潟 | 預金先健全性評価の更新頻度を設定 |
| Long maturity | specific liability match for long terms | amount >5y matched to documented cash need | GFOA Market Risk; 東京 | 5年超は自動的に禁止せず、liability matchをgateとする |

## Recommended control hierarchy

1. **Policy layer** — objectives, eligible assets, authority, custody, reporting.
2. **Liquidity layer** — minimum cash / near-cash, 13-week coverage, 12-month maturities.
3. **Portfolio layer** — maturity buckets, issuer/category concentration, ladder.
4. **Monitoring layer** — forecast error, WAM/duration proxy, mark-to-market, exceptions.
5. **Governance layer** — quarterly review, annual policy/benchmark review, escalation.

## Important boundary

熊本の21年・1,000億円、東京の10年、兵庫の30年といったpeer limitはbenchmark factsであって愛媛の推奨limitではない。愛媛の数値limitは、R7末/R8期首基金別cash balance、1～5年支出pipeline、現行公金管理方針本文が確認された後に設定する。
