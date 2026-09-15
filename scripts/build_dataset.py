#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a 47-prefecture fund investment dataset from e-Stat primary data.

Target fiscal years:
- FY2022 (Reiwa 4) <- e-Stat survey year 2023
- FY2023 (Reiwa 5) <- e-Stat survey year 2024
- FY2024 (Reiwa 6) <- e-Stat survey year 2025

Primary source: MIC Local Public Finance Survey (prefecture tables), e-Stat.
Tables used: 01 (profile), 02 (settlement balance), 31 (fund status).
"""
from __future__ import annotations

import csv
import json
import math
import os
import re
import statistics
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import parse_qs, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
PROCESSED = ROOT / "processed"
CHARTS = ROOT / "charts"
for d in (RAW, PROCESSED, CHARTS):
    d.mkdir(parents=True, exist_ok=True)

ESTAT_BASE = "https://www.e-stat.go.jp"
LISTING_URL = (
    "https://www.e-stat.go.jp/stat-search/files?cycle=7&layout=datalist&month=0"
    "&result_back=1&tclass1=000001078091&tclass2=000001078092"
    "&tclass3val=0&toukei=00200251&tstat=000001077755&year={year}0"
)

SURVEY_TO_FY = {2023: 2022, 2024: 2023, 2025: 2024}
FY_LABEL = {2022: "R4", 2023: "R5", 2024: "R6"}

PREFS = [
    "北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県","茨城県","栃木県","群馬県",
    "埼玉県","千葉県","東京都","神奈川県","新潟県","富山県","石川県","福井県","山梨県","長野県",
    "岐阜県","静岡県","愛知県","三重県","滋賀県","京都府","大阪府","兵庫県","奈良県","和歌山県",
    "鳥取県","島根県","岡山県","広島県","山口県","徳島県","香川県","愛媛県","高知県","福岡県",
    "佐賀県","長崎県","熊本県","大分県","宮崎県","鹿児島県","沖縄県"
]
PREF_SET = set(PREFS)

TABLE_TITLES = {
    "01": "団体の概況",
    "02": "決算収支の状況",
    "31": "基金の状況",
}

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (compatible; saiken-prefecture-fund-research/1.0; +https://github.com/ryotamatsuki/saiken)",
    "Accept-Language": "ja,en-US;q=0.8,en;q=0.6",
})


def norm(s: object) -> str:
    if s is None:
        return ""
    return re.sub(r"[\s\u3000]+", "", str(s)).replace("（", "(").replace("）", ")")


def nfloat(v: object) -> Optional[float]:
    if v is None:
        return None
    s = str(v).strip().replace(",", "")
    if s in ("", "-", "－", "…", "...", "NA", "N/A"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def thousand_yen_to_million(v: object) -> Optional[float]:
    x = nfloat(v)
    return None if x is None else x / 1000.0


def get(url: str, *, binary: bool = False, retries: int = 5):
    last = None
    for i in range(retries):
        try:
            r = SESSION.get(url, timeout=60)
            r.raise_for_status()
            return r.content if binary else r.text
        except Exception as e:
            last = e
            time.sleep(2 ** i)
    raise RuntimeError(f"GET failed after {retries} tries: {url}: {last}")


def discover_statinf_ids(survey_year: int) -> Dict[str, str]:
    """Discover table 01/02/31 statInfId values from the official e-Stat listing."""
    url = LISTING_URL.format(year=survey_year)
    html = get(url)
    soup = BeautifulSoup(html, "html.parser")
    found: Dict[str, str] = {}

    # Primary path: title links include stat_infid in href.
    for a in soup.find_all("a", href=True):
        text = norm(a.get_text(" ", strip=True))
        href = a.get("href", "")
        if "stat_infid=" not in href:
            continue
        q = parse_qs(urlparse(href).query)
        sid = (q.get("stat_infid") or [None])[0]
        if not sid:
            continue
        for table_no, title_key in TABLE_TITLES.items():
            if title_key in text:
                found.setdefault(table_no, sid)

    # Fallback: inspect anchors whose text matches the title, then follow detail page.
    if len(found) < 3:
        for a in soup.find_all("a", href=True):
            text = norm(a.get_text(" ", strip=True))
            table_no = None
            for no, key in TABLE_TITLES.items():
                if key in text:
                    table_no = no
                    break
            if not table_no or table_no in found:
                continue
            href = urljoin(ESTAT_BASE, a["href"])
            detail = get(href)
            m = re.search(r"stat_infid=(\d+)", href)
            if not m:
                m = re.search(r"stat_infid(?:=|%3D)(\d+)", detail)
            if m:
                found[table_no] = m.group(1)

    if set(found) != {"01", "02", "31"}:
        raise RuntimeError(f"Could not discover all required table IDs for survey year {survey_year}: {found}")
    return found


def download_csv(statinf_id: str, out_path: Path) -> str:
    url = f"{ESTAT_BASE}/stat-search/file-download?fileKind=1&statInfId={statinf_id}"
    data = get(url, binary=True)
    out_path.write_bytes(data)
    return url


def decode_csv(path: Path) -> Tuple[str, str]:
    data = path.read_bytes()
    for enc in ("utf-8-sig", "cp932", "shift_jis", "utf-8"):
        try:
            return data.decode(enc), enc
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("unknown", data, 0, 1, f"Cannot decode {path}")


def read_csv(path: Path) -> Tuple[List[dict], List[str], str]:
    text, enc = decode_csv(path)
    rows = list(csv.DictReader(text.splitlines()))
    headers = list(rows[0].keys()) if rows else []
    return rows, headers, enc


def col_by(headers: Iterable[str], required: Iterable[str], forbidden: Iterable[str] = ()) -> Optional[str]:
    req = [norm(x) for x in required]
    forb = [norm(x) for x in forbidden]
    candidates = []
    for h in headers:
        nh = norm(h)
        if all(x in nh for x in req) and not any(x in nh for x in forb):
            candidates.append(h)
    if not candidates:
        return None
    candidates.sort(key=lambda h: (len(norm(h)), h))
    return candidates[0]


def detect_common_cols(headers: List[str]) -> Dict[str, Optional[str]]:
    return {
        "fiscal_year": col_by(headers, ["決算年度"]),
        "code": col_by(headers, ["団体コード"]),
        "pref": col_by(headers, ["県名"]) or col_by(headers, ["都道府県名"]),
        "entity": col_by(headers, ["団体名"]),
        "row_name": col_by(headers, ["行名称"]),
        "row_no": col_by(headers, ["行番号"]),
    }


def pick_pref(row: dict, common: Dict[str, Optional[str]]) -> Optional[str]:
    for key in (common.get("pref"), common.get("entity")):
        if key:
            val = str(row.get(key, "")).strip()
            if val in PREF_SET:
                return val
    # Some files may put prefecture directly in a generic column.
    for v in row.values():
        s = str(v).strip()
        if s in PREF_SET:
            return s
    return None


def select_pref_rows(rows: List[dict], common: Dict[str, Optional[str]]) -> Dict[str, List[dict]]:
    out: Dict[str, List[dict]] = defaultdict(list)
    for r in rows:
        p = pick_pref(r, common)
        if p:
            out[p].append(r)
    return out


def rowname(r: dict, common: Dict[str, Optional[str]]) -> str:
    c = common.get("row_name")
    return norm(r.get(c, "")) if c else ""


def find_row(rows: List[dict], common: Dict[str, Optional[str]], patterns: List[List[str]]) -> Optional[dict]:
    for r in rows:
        rn = rowname(r, common)
        for terms in patterns:
            if all(norm(t) in rn for t in terms):
                return r
    # Some table files are one-row-per-prefecture and the row name is generic/blank.
    if len(rows) == 1:
        return rows[0]
    return None


def parse_table31(path: Path, fy: int) -> Tuple[Dict[str, dict], dict]:
    rows, headers, enc = read_csv(path)
    common = detect_common_cols(headers)
    by_pref = select_pref_rows(rows, common)

    c_total = col_by(headers, ["当年度末現在高", "F"], ["管理状況"])
    if c_total is None:
        c_total = col_by(headers, ["当年度末現在高"], ["管理状況"])
    c_cash = col_by(headers, ["管理状況", "現金・預金"])
    c_trust = col_by(headers, ["管理状況", "信託"])
    c_securities = col_by(headers, ["管理状況", "有価証券"], ["うち地方債"])
    c_local_bonds = col_by(headers, ["管理状況", "有価証券", "地方債"])
    c_equity = col_by(headers, ["管理状況", "出資金"])
    c_other = col_by(headers, ["管理状況", "その他"])

    required_cols = [c_total, c_cash, c_trust, c_securities, c_local_bonds, c_equity, c_other]
    if any(c is None for c in required_cols):
        raise RuntimeError(f"FY{fy}: table31 columns not found. headers={headers}; mapped={required_cols}")

    result: Dict[str, dict] = {}
    for p in PREFS:
        prs = by_pref.get(p, [])
        total_row = find_row(prs, common, [["積立基金", "合計"], ["積立基金_合計"], ["合計(1～3)"]])
        fa_row = find_row(prs, common, [["財政調整基金"]])
        dr_row = find_row(prs, common, [["減債基金"]])
        os_row = find_row(prs, common, [["その他特定目的基金"]])
        if total_row is None:
            raise RuntimeError(f"FY{fy}: no accumulated-fund total row for {p}; row names={[rowname(x, common) for x in prs]}")

        def my(r: Optional[dict], col: str) -> Optional[float]:
            return None if r is None else thousand_yen_to_million(r.get(col))

        cash = my(total_row, c_cash)
        trust = my(total_row, c_trust)
        sec = my(total_row, c_securities)
        equity = my(total_row, c_equity)
        oth = my(total_row, c_other)
        # "other_assets" is explicitly the sum of source categories 4 (出資金) and 5 (その他),
        # not a residual plug.
        other_assets = None if equity is None or oth is None else equity + oth
        result[p] = {
            "fund_total_million_yen": my(total_row, c_total),
            "fiscal_adjustment_fund_million_yen": my(fa_row, c_total),
            "debt_reduction_fund_million_yen": my(dr_row, c_total),
            "other_specific_funds_million_yen": my(os_row, c_total),
            "cash_deposit_million_yen": cash,
            "trust_million_yen": trust,
            "securities_million_yen": sec,
            "local_bonds_million_yen": my(total_row, c_local_bonds),
            "equity_contributions_million_yen": equity,
            "source_other_million_yen": oth,
            "other_assets_million_yen": other_assets,
        }

    meta = {
        "encoding": enc,
        "headers": headers,
        "source_columns": {
            "fund_total_million_yen": c_total,
            "fiscal_adjustment_fund_million_yen": c_total,
            "debt_reduction_fund_million_yen": c_total,
            "other_specific_funds_million_yen": c_total,
            "cash_deposit_million_yen": c_cash,
            "trust_million_yen": c_trust,
            "securities_million_yen": c_securities,
            "local_bonds_million_yen": c_local_bonds,
            "equity_contributions_million_yen": c_equity,
            "source_other_million_yen": c_other,
            "other_assets_million_yen": f"{c_equity} + {c_other}",
        },
    }
    return result, meta


def parse_table01(path: Path, fy: int) -> Tuple[Dict[str, dict], dict]:
    rows, headers, enc = read_csv(path)
    common = detect_common_cols(headers)
    by_pref = select_pref_rows(rows, common)
    c_sfs = col_by(headers, ["標準財政規模"])
    if c_sfs is None:
        raise RuntimeError(f"FY{fy}: standard financial scale column not found: {headers}")
    out = {}
    for p in PREFS:
        prs = by_pref.get(p, [])
        if not prs:
            raise RuntimeError(f"FY{fy}: table01 no row for {p}")
        r = prs[0]
        code = str(r.get(common.get("code"), "")).strip() if common.get("code") else ""
        out[p] = {
            "prefecture_code": code,
            "standard_financial_scale_million_yen": thousand_yen_to_million(r.get(c_sfs)),
        }
    return out, {"encoding": enc, "headers": headers, "source_columns": {"standard_financial_scale_million_yen": c_sfs}}


def parse_table02(path: Path, fy: int) -> Tuple[Dict[str, dict], dict]:
    rows, headers, enc = read_csv(path)
    common = detect_common_cols(headers)
    by_pref = select_pref_rows(rows, common)
    c_rev = col_by(headers, ["歳入総額"])
    c_exp = col_by(headers, ["歳出総額"])
    if c_rev is None or c_exp is None:
        raise RuntimeError(f"FY{fy}: revenue/expenditure columns not found: {headers}")
    out = {}
    for p in PREFS:
        prs = by_pref.get(p, [])
        if not prs:
            raise RuntimeError(f"FY{fy}: table02 no row for {p}")
        r = prs[0]
        out[p] = {
            "revenue_total_million_yen": thousand_yen_to_million(r.get(c_rev)),
            "expenditure_total_million_yen": thousand_yen_to_million(r.get(c_exp)),
        }
    return out, {"encoding": enc, "headers": headers, "source_columns": {"revenue_total_million_yen": c_rev, "expenditure_total_million_yen": c_exp}}


def safe_div(a: Optional[float], b: Optional[float], mult: float = 100.0) -> Optional[float]:
    if a is None or b is None or b == 0:
        return None
    return a / b * mult


def fmt(v: Optional[float], n: int = 2) -> str:
    return "NA" if v is None or (isinstance(v, float) and math.isnan(v)) else f"{v:.{n}f}"


def mean(xs: List[float]) -> Optional[float]:
    return statistics.fmean(xs) if xs else None


def quantile(xs: List[float], q: float) -> Optional[float]:
    if not xs:
        return None
    ys = sorted(xs)
    if len(ys) == 1:
        return ys[0]
    pos = (len(ys) - 1) * q
    lo = int(math.floor(pos)); hi = int(math.ceil(pos))
    if lo == hi:
        return ys[lo]
    return ys[lo] + (ys[hi] - ys[lo]) * (pos - lo)


def rank_desc(records: List[dict], key: str) -> Dict[str, int]:
    valid = [(r["prefecture"], r.get(key)) for r in records if r.get(key) is not None]
    valid.sort(key=lambda x: x[1], reverse=True)
    return {p: i + 1 for i, (p, _) in enumerate(valid)}


def write_csv(path: Path, rows: List[dict], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def build_charts(long_rows: List[dict], wide_rows: List[dict]) -> None:
    import matplotlib.pyplot as plt

    r6 = [r for r in long_rows if r["fiscal_year"] == 2024]
    r6_sorted = sorted(r6, key=lambda r: r.get("securities_ratio_pct") if r.get("securities_ratio_pct") is not None else -1)
    plt.figure(figsize=(9, 12))
    y = list(range(len(r6_sorted)))
    vals = [r.get("securities_ratio_pct") or 0 for r in r6_sorted]
    labels = [r["prefecture"] for r in r6_sorted]
    plt.barh(y, vals)
    plt.yticks(y, labels, fontsize=7)
    plt.xlabel("有価証券比率（%）")
    plt.title("47都道府県 令和6年度 基金有価証券比率")
    for i, p in enumerate(labels):
        if p == "愛媛県":
            plt.text(vals[i], i, "  ← 愛媛県", va="center", fontsize=9, fontweight="bold")
    plt.tight_layout(); plt.savefig(CHARTS / "01_R6_securities_ratio_ranking.png", dpi=180); plt.close()

    wr_sorted = sorted(wide_rows, key=lambda r: r.get("R4_R6_securities_ratio_change_pt") if r.get("R4_R6_securities_ratio_change_pt") is not None else -999)
    plt.figure(figsize=(9, 12))
    y = list(range(len(wr_sorted)))
    vals = [r.get("R4_R6_securities_ratio_change_pt") or 0 for r in wr_sorted]
    labels = [r["prefecture"] for r in wr_sorted]
    plt.barh(y, vals)
    plt.yticks(y, labels, fontsize=7)
    plt.xlabel("R4→R6 有価証券比率変化（pt）")
    plt.title("47都道府県 有価証券比率の変化")
    for i, p in enumerate(labels):
        if p == "愛媛県":
            plt.text(vals[i], i, "  ← 愛媛県", va="center", fontsize=9, fontweight="bold")
    plt.tight_layout(); plt.savefig(CHARTS / "02_R4_R6_securities_ratio_change.png", dpi=180); plt.close()

    plt.figure(figsize=(10, 8))
    xs = [r["R6_securities_ratio_pct"] for r in wide_rows if r.get("R6_securities_ratio_pct") is not None and r.get("R4_R6_securities_ratio_change_pt") is not None]
    ys = [r["R4_R6_securities_ratio_change_pt"] for r in wide_rows if r.get("R6_securities_ratio_pct") is not None and r.get("R4_R6_securities_ratio_change_pt") is not None]
    ps = [r["prefecture"] for r in wide_rows if r.get("R6_securities_ratio_pct") is not None and r.get("R4_R6_securities_ratio_change_pt") is not None]
    plt.scatter(xs, ys)
    for x, yv, p in zip(xs, ys, ps):
        plt.annotate(p, (x, yv), fontsize=6, xytext=(3, 2), textcoords="offset points", fontweight="bold" if p == "愛媛県" else "normal")
    if xs and ys:
        plt.axvline(statistics.median(xs), linestyle="--", linewidth=1)
        plt.axhline(statistics.median(ys), linestyle="--", linewidth=1)
    plt.xlabel("R6 有価証券比率（%）"); plt.ylabel("R4→R6 変化（pt）")
    plt.title("基金運用の類型化：有価証券比率 × R4→R6変化")
    plt.tight_layout(); plt.savefig(CHARTS / "03_typology_scatter.png", dpi=180); plt.close()

    eh = sorted([r for r in long_rows if r["prefecture"] == "愛媛県"], key=lambda r: r["fiscal_year"])
    med_by_fy = {}
    for fy in (2022, 2023, 2024):
        fyrows = [r for r in long_rows if r["fiscal_year"] == fy]
        med_by_fy[fy] = {
            "sec": statistics.median([r["securities_ratio_pct"] for r in fyrows if r.get("securities_ratio_pct") is not None]),
            "cash": statistics.median([r["cash_deposit_ratio_pct"] for r in fyrows if r.get("cash_deposit_ratio_pct") is not None]),
        }
    years = [r["fiscal_year"] for r in eh]
    plt.figure(figsize=(8, 5))
    plt.plot(years, [r["securities_ratio_pct"] for r in eh], marker="o", label="愛媛県 有価証券")
    plt.plot(years, [med_by_fy[y]["sec"] for y in years], marker="o", label="全国中央値 有価証券")
    plt.plot(years, [r["cash_deposit_ratio_pct"] for r in eh], marker="o", label="愛媛県 現金・預金")
    plt.plot(years, [med_by_fy[y]["cash"] for y in years], marker="o", label="全国中央値 現金・預金")
    plt.xticks(years, [FY_LABEL[y] for y in years]); plt.ylabel("比率（%）")
    plt.title("愛媛県と全国中央値の推移"); plt.legend(fontsize=8)
    plt.tight_layout(); plt.savefig(CHARTS / "04_ehime_vs_median_trend.png", dpi=180); plt.close()


def main() -> int:
    source_records = []
    parsed_by_fy: Dict[int, Dict[str, dict]] = {}
    metadata = {}

    for survey_year, fy in SURVEY_TO_FY.items():
        ids = discover_statinf_ids(survey_year)
        year_meta = {}
        for table_no in ("01", "02", "31"):
            out = RAW / f"FY{fy}_survey{survey_year}_table{table_no}.csv"
            dl = download_csv(ids[table_no], out)
            year_meta[table_no] = {
                "statinf_id": ids[table_no],
                "dataset_page": f"https://www.e-stat.go.jp/stat-search/files?stat_infid={ids[table_no]}",
                "download_url": dl,
                "listing_url": LISTING_URL.format(year=survey_year),
            }

        t31, m31 = parse_table31(RAW / f"FY{fy}_survey{survey_year}_table31.csv", fy)
        t01, m01 = parse_table01(RAW / f"FY{fy}_survey{survey_year}_table01.csv", fy)
        t02, m02 = parse_table02(RAW / f"FY{fy}_survey{survey_year}_table02.csv", fy)
        year_meta["31"].update(m31); year_meta["01"].update(m01); year_meta["02"].update(m02)
        metadata[fy] = year_meta

        combined = {}
        for p in PREFS:
            combined[p] = {**t31[p], **t01[p], **t02[p]}
        parsed_by_fy[fy] = combined

        for var, source_col in m31["source_columns"].items():
            source_records.append({
                "fiscal_year": fy, "variable_name": var,
                "source_document": "総務省 地方財政状況調査（都道府県分）",
                "source_table": "31 基金の状況 その1 積立基金現在高の状況",
                "source_column_name": source_col, "source_unit": "千円（処理時に百万円へ換算）",
                "estat_url": year_meta["31"]["dataset_page"], "download_url": year_meta["31"]["download_url"],
                "notes": "other_assets_million_yen は出資金＋その他の明示的合算。残差ではない。" if var == "other_assets_million_yen" else "",
            })
        for table_no, mm in (("01", m01), ("02", m02)):
            for var, source_col in mm["source_columns"].items():
                source_records.append({
                    "fiscal_year": fy, "variable_name": var,
                    "source_document": "総務省 地方財政状況調査（都道府県分）",
                    "source_table": f"{table_no} {TABLE_TITLES[table_no]}",
                    "source_column_name": source_col, "source_unit": "千円（処理時に百万円へ換算）",
                    "estat_url": year_meta[table_no]["dataset_page"], "download_url": year_meta[table_no]["download_url"],
                    "notes": "",
                })

    # Long dataset and Python-calculated indicators.
    long_rows: List[dict] = []
    for fy in (2022, 2023, 2024):
        for p in PREFS:
            r = {"prefecture": p, "prefecture_code": parsed_by_fy[fy][p].get("prefecture_code", ""), "fiscal_year": fy}
            r.update(parsed_by_fy[fy][p])
            ft = r.get("fund_total_million_yen")
            sec = r.get("securities_million_yen")
            cash = r.get("cash_deposit_million_yen")
            lb = r.get("local_bonds_million_yen")
            sfs = r.get("standard_financial_scale_million_yen")
            r["securities_ratio_pct"] = safe_div(sec, ft)
            r["cash_deposit_ratio_pct"] = safe_div(cash, ft)
            r["local_bond_ratio_pct"] = safe_div(lb, ft)
            r["local_bond_share_of_securities_pct"] = safe_div(lb, sec)
            r["fund_to_standard_scale_pct"] = safe_div(ft, sfs)
            r["securities_to_standard_scale_pct"] = safe_div(sec, sfs)
            long_rows.append(r)

    # Year-over-year percentage-point change.
    idx = {(r["prefecture"], r["fiscal_year"]): r for r in long_rows}
    for r in long_rows:
        prev = idx.get((r["prefecture"], r["fiscal_year"] - 1))
        r["securities_ratio_yoy_change_pt"] = None if not prev or r.get("securities_ratio_pct") is None or prev.get("securities_ratio_pct") is None else r["securities_ratio_pct"] - prev["securities_ratio_pct"]

    # QA.
    qa_rows = []
    severe = []
    for fy in (2022, 2023, 2024):
        rows_fy = [r for r in long_rows if r["fiscal_year"] == fy]
        qa_rows.append({"fiscal_year": fy, "check": "prefecture_count", "status": "PASS" if len(rows_fy) == 47 else "FAIL", "value": len(rows_fy), "details": "47 prefectures expected"})
        if len(rows_fy) != 47: severe.append(f"FY{fy} prefecture count {len(rows_fy)}")
        uniq = len({(r["prefecture"], r["fiscal_year"]) for r in rows_fy})
        qa_rows.append({"fiscal_year": fy, "check": "unique_prefecture_year", "status": "PASS" if uniq == 47 else "FAIL", "value": uniq, "details": "prefecture × fiscal_year must be unique"})
        for r in rows_fy:
            vals = [r.get("cash_deposit_million_yen"), r.get("trust_million_yen"), r.get("securities_million_yen"), r.get("equity_contributions_million_yen"), r.get("source_other_million_yen")]
            if all(v is not None for v in vals) and r.get("fund_total_million_yen") is not None:
                residual = sum(vals) - r["fund_total_million_yen"]
                if abs(residual) > 0.001:
                    qa_rows.append({"fiscal_year": fy, "check": "asset_reconciliation", "status": "WARN", "value": residual, "details": f"{r['prefecture']}: management assets - fund total (million yen)"})
            if r.get("local_bonds_million_yen") is not None and r.get("securities_million_yen") is not None and r["local_bonds_million_yen"] > r["securities_million_yen"] + 1e-9:
                qa_rows.append({"fiscal_year": fy, "check": "local_bonds_within_securities", "status": "FAIL", "value": r["local_bonds_million_yen"] - r["securities_million_yen"], "details": r["prefecture"]})
                severe.append(f"FY{fy} {r['prefecture']} local bonds > securities")
            for k in ("securities_ratio_pct", "cash_deposit_ratio_pct", "local_bond_ratio_pct"):
                v = r.get(k)
                if v is not None and (v < -1e-9 or v > 100.0001):
                    qa_rows.append({"fiscal_year": fy, "check": "ratio_range", "status": "FAIL", "value": v, "details": f"{r['prefecture']} {k}"})
                    severe.append(f"FY{fy} {r['prefecture']} invalid {k}={v}")

    # Wide dataset.
    wide_rows: List[dict] = []
    for p in PREFS:
        r4, r5, r6 = idx[(p, 2022)], idx[(p, 2023)], idx[(p, 2024)]
        w = {"prefecture": p, "prefecture_code": r6.get("prefecture_code") or r5.get("prefecture_code") or r4.get("prefecture_code")}
        for label, rr in (("R4", r4), ("R5", r5), ("R6", r6)):
            w[f"{label}_fund_total_million_yen"] = rr.get("fund_total_million_yen")
            w[f"{label}_cash_deposit_million_yen"] = rr.get("cash_deposit_million_yen")
            w[f"{label}_securities_million_yen"] = rr.get("securities_million_yen")
            w[f"{label}_securities_ratio_pct"] = rr.get("securities_ratio_pct")
            w[f"{label}_cash_deposit_ratio_pct"] = rr.get("cash_deposit_ratio_pct")
            w[f"{label}_local_bond_ratio_pct"] = rr.get("local_bond_ratio_pct")
            w[f"{label}_standard_financial_scale_million_yen"] = rr.get("standard_financial_scale_million_yen")
            w[f"{label}_securities_to_standard_scale_pct"] = rr.get("securities_to_standard_scale_pct")
        w["R4_R6_securities_ratio_change_pt"] = None if r4.get("securities_ratio_pct") is None or r6.get("securities_ratio_pct") is None else r6["securities_ratio_pct"] - r4["securities_ratio_pct"]
        w["R4_R6_securities_change_million_yen"] = None if r4.get("securities_million_yen") is None or r6.get("securities_million_yen") is None else r6["securities_million_yen"] - r4["securities_million_yen"]
        w["R4_R6_securities_growth_pct"] = safe_div(w["R4_R6_securities_change_million_yen"], r4.get("securities_million_yen")) if r4.get("securities_million_yen") not in (None, 0) else None
        w["R4_R6_cash_deposit_decline_million_yen"] = None if r4.get("cash_deposit_million_yen") is None or r6.get("cash_deposit_million_yen") is None else r4["cash_deposit_million_yen"] - r6["cash_deposit_million_yen"]
        wide_rows.append(w)

    # Typology based on nationwide medians.
    med_r6_sec = statistics.median([w["R6_securities_ratio_pct"] for w in wide_rows if w.get("R6_securities_ratio_pct") is not None])
    med_change = statistics.median([w["R4_R6_securities_ratio_change_pt"] for w in wide_rows if w.get("R4_R6_securities_ratio_change_pt") is not None])
    for w in wide_rows:
        x = w.get("R6_securities_ratio_pct"); y = w.get("R4_R6_securities_ratio_change_pt")
        if x is None or y is None:
            w["typology"] = "NA"
        elif x >= med_r6_sec and y >= med_change:
            w["typology"] = "A: 有価証券比率が高く、さらに増加"
        elif x < med_r6_sec and y >= med_change:
            w["typology"] = "B: 低位から相対的にシフト"
        elif x >= med_r6_sec and y < med_change:
            w["typology"] = "C: 高比率だが増加は小さい/低下"
        else:
            w["typology"] = "D: 現預金中心・シフト小"

    # Ranking table for six metrics.
    r6_rows = [r for r in long_rows if r["fiscal_year"] == 2024]
    wide_by_pref = {w["prefecture"]: w for w in wide_rows}
    rank_specs = [
        ("R6有価証券比率", "securities_ratio_pct", r6_rows),
        ("R6有価証券残高", "securities_million_yen", r6_rows),
        ("R6有価証券/標準財政規模", "securities_to_standard_scale_pct", r6_rows),
        ("R4→R6有価証券比率上昇幅", "R4_R6_securities_ratio_change_pt", wide_rows),
        ("R4→R6有価証券残高増加額", "R4_R6_securities_change_million_yen", wide_rows),
        ("R6現金・預金比率", "cash_deposit_ratio_pct", r6_rows),
    ]
    ranking_rows = []
    for metric, key, source in rank_specs:
        ordered = sorted([r for r in source if r.get(key) is not None], key=lambda r: r[key], reverse=True)
        for i, r in enumerate(ordered, 1):
            p = r["prefecture"]
            w = wide_by_pref[p]
            ranking_rows.append({
                "metric": metric, "rank": i, "prefecture": "★愛媛県" if p == "愛媛県" else p,
                "value": r[key],
                "R4": w.get("R4_securities_ratio_pct") if "比率" in metric and "現金" not in metric else w.get("R4_securities_million_yen"),
                "R5": w.get("R5_securities_ratio_pct") if "比率" in metric and "現金" not in metric else w.get("R5_securities_million_yen"),
                "R6": w.get("R6_securities_ratio_pct") if "比率" in metric and "現金" not in metric else w.get("R6_securities_million_yen"),
                "R4_R6_change": w.get("R4_R6_securities_ratio_change_pt") if "比率" in metric else w.get("R4_R6_securities_change_million_yen"),
            })

    # Ehime summary: rank, mean, median, quartiles for requested variables.
    metric_map = {
        "fund_total_million_yen": "基金総額",
        "securities_million_yen": "有価証券残高",
        "cash_deposit_million_yen": "現金・預金残高",
        "securities_ratio_pct": "有価証券比率",
        "cash_deposit_ratio_pct": "現金・預金比率",
        "local_bond_ratio_pct": "地方債比率",
        "fund_to_standard_scale_pct": "基金/標準財政規模",
        "securities_to_standard_scale_pct": "有価証券/標準財政規模",
    }
    ehime_summary = []
    for key, label in metric_map.items():
        vals = [r[key] for r in r6_rows if r.get(key) is not None]
        ranks = rank_desc(r6_rows, key)
        eh = idx[("愛媛県", 2024)].get(key)
        ehime_summary.append({"metric": label, "ehime_value": eh, "rank_desc": ranks.get("愛媛県"), "n": len(vals), "mean": mean(vals), "median": statistics.median(vals) if vals else None, "q1": quantile(vals, .25), "q3": quantile(vals, .75)})
    w_eh = wide_by_pref["愛媛県"]
    change_vals = [w["R4_R6_securities_ratio_change_pt"] for w in wide_rows if w.get("R4_R6_securities_ratio_change_pt") is not None]
    change_ranks = rank_desc(wide_rows, "R4_R6_securities_ratio_change_pt")
    ehime_summary.append({"metric": "R4→R6有価証券比率変化(pt)", "ehime_value": w_eh.get("R4_R6_securities_ratio_change_pt"), "rank_desc": change_ranks.get("愛媛県"), "n": len(change_vals), "mean": mean(change_vals), "median": statistics.median(change_vals), "q1": quantile(change_vals, .25), "q3": quantile(change_vals, .75)})

    # Neighbors around Ehime in R6 securities ratio.
    ordered_sec = sorted(r6_rows, key=lambda r: r.get("securities_ratio_pct") if r.get("securities_ratio_pct") is not None else -1, reverse=True)
    eh_pos = next(i for i, r in enumerate(ordered_sec) if r["prefecture"] == "愛媛県")
    neighbors = ordered_sec[max(0, eh_pos-3):min(len(ordered_sec), eh_pos+4)]

    # Second-stage candidates: top ratio, top shift, similar SFS, plus Tokyo as disclosure/scale contrast.
    candidates = []
    def add_candidate(p: str, reason: str):
        if p not in [x["prefecture"] for x in candidates] and p != "愛媛県":
            candidates.append({"prefecture": p, "reason": reason})
    for r in sorted(r6_rows, key=lambda x: x.get("securities_ratio_pct") or -1, reverse=True)[:4]:
        add_candidate(r["prefecture"], "R6有価証券比率が全国上位。資産構成・年限管理の詳細確認価値が高い。")
    for w in sorted(wide_rows, key=lambda x: x.get("R4_R6_securities_ratio_change_pt") or -999, reverse=True)[:4]:
        add_candidate(w["prefecture"], "R4→R6の有価証券比率上昇幅が全国上位。金利正常化局面での運用方針変更を確認したい。")
    eh_sfs = idx[("愛媛県", 2024)].get("standard_financial_scale_million_yen")
    if eh_sfs:
        similar = sorted([r for r in r6_rows if r["prefecture"] != "愛媛県" and r.get("standard_financial_scale_million_yen")], key=lambda r: abs(r["standard_financial_scale_million_yen"] - eh_sfs))[:4]
        for r in similar:
            add_candidate(r["prefecture"], "標準財政規模が愛媛県に近く、同規模県の運用ベンチマークとして有用。")
    add_candidate("東京都", "絶対額・財政規模が突出する対照群。公金運用の開示・ALMの先進事例確認に有用。")
    candidates = candidates[:12]

    # Write datasets.
    long_fields = [
        "prefecture","prefecture_code","fiscal_year","fund_total_million_yen","fiscal_adjustment_fund_million_yen","debt_reduction_fund_million_yen","other_specific_funds_million_yen",
        "cash_deposit_million_yen","trust_million_yen","securities_million_yen","local_bonds_million_yen","equity_contributions_million_yen","source_other_million_yen","other_assets_million_yen",
        "standard_financial_scale_million_yen","revenue_total_million_yen","expenditure_total_million_yen","securities_ratio_pct","cash_deposit_ratio_pct","local_bond_ratio_pct",
        "local_bond_share_of_securities_pct","fund_to_standard_scale_pct","securities_to_standard_scale_pct","securities_ratio_yoy_change_pt"
    ]
    write_csv(PROCESSED / "prefecture_fund_investment_R4_R6.csv", long_rows, long_fields)
    wide_fields = list(wide_rows[0].keys())
    write_csv(PROCESSED / "wide_data.csv", wide_rows, wide_fields)
    write_csv(PROCESSED / "R6_rankings.csv", ranking_rows, ["metric","rank","prefecture","value","R4","R5","R6","R4_R6_change"])
    write_csv(PROCESSED / "ehime_analysis.csv", ehime_summary, ["metric","ehime_value","rank_desc","n","mean","median","q1","q3"])
    write_csv(PROCESSED / "source_dictionary.csv", source_records, ["fiscal_year","variable_name","source_document","source_table","source_column_name","source_unit","estat_url","download_url","notes"])
    write_csv(PROCESSED / "QA.csv", qa_rows, ["fiscal_year","check","status","value","details"])
    write_csv(PROCESSED / "stage2_candidates.csv", candidates, ["prefecture","reason"])

    # Save machine-readable metadata / source IDs.
    (PROCESSED / "source_metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    # Charts.
    build_charts(long_rows, wide_rows)

    # Analysis markdown.
    eh = idx[("愛媛県", 2024)]
    rank_sec = rank_desc(r6_rows, "securities_ratio_pct").get("愛媛県")
    rank_sec_amt = rank_desc(r6_rows, "securities_million_yen").get("愛媛県")
    rank_shift = rank_desc(wide_rows, "R4_R6_securities_ratio_change_pt").get("愛媛県")
    med_r6 = statistics.median([r["securities_ratio_pct"] for r in r6_rows if r.get("securities_ratio_pct") is not None])
    mean_r6 = statistics.fmean([r["securities_ratio_pct"] for r in r6_rows if r.get("securities_ratio_pct") is not None])
    top5 = sorted(r6_rows, key=lambda r: r.get("securities_ratio_pct") or -1, reverse=True)[:5]
    top_shift = sorted(wide_rows, key=lambda r: r.get("R4_R6_securities_ratio_change_pt") or -999, reverse=True)[:5]

    status = "DATASET COMPLETE" if not severe else "DATASET INCOMPLETE"
    analysis = f"""# 都道府県基金運用 第1段階分析（R4～R6）

## 判定

**{status}**

## 調査目的

日経新聞「自治体の国債購入 急増」の問題意識を踏まえ、47都道府県について基金の運用資産が現金・預金から有価証券へどの程度シフトしているかを、全国統一の総務省「地方財政状況調査（都道府県分）」で比較した。

対象決算年度は令和4年度（FY2022）、令和5年度（FY2023）、令和6年度（FY2024）。e-Stat上の調査年月はそれぞれ2023年、2024年、2025年であり、ファイル内の「決算年度」で対応関係を確認している。

## 使用した一次資料

- 表01「団体の概況」：標準財政規模
- 表02「決算収支の状況」：歳入総額、歳出総額
- 表31「基金の状況 その1 積立基金現在高の状況」：基金残高、管理状況（現金・預金、信託、有価証券、うち地方債、出資金、その他）

出典URL・statInfId・実ダウンロードURLは `processed/source_dictionary.csv` と `processed/source_metadata.json` に保存した。

## 指標定義

- 有価証券比率 = 有価証券 ÷ 積立基金合計 × 100
- 現金・預金比率 = 現金・預金 ÷ 積立基金合計 × 100
- 地方債比率 = 有価証券のうち地方債 ÷ 積立基金合計 × 100
- 有価証券内地方債比率 = 地方債 ÷ 有価証券 × 100
- 基金/標準財政規模 = 積立基金合計 ÷ 標準財政規模 × 100
- 有価証券/標準財政規模 = 有価証券 ÷ 標準財政規模 × 100

金額の元単位は千円で、Python処理時に百万円へ統一した。

## 令和6年度 全国の主な特徴

47都道府県の有価証券比率は、単純平均 **{mean_r6:.2f}%**、中央値 **{med_r6:.2f}%**。

有価証券比率上位5団体：
"""
    for i, r in enumerate(top5, 1):
        analysis += f"\n{i}. {r['prefecture']}：{r['securities_ratio_pct']:.2f}%"
    analysis += "\n\nR4→R6の有価証券比率上昇幅 上位5団体：\n"
    for i, w in enumerate(top_shift, 1):
        analysis += f"\n{i}. {w['prefecture']}：{w['R4_R6_securities_ratio_change_pt']:.2f}pt"

    analysis += f"""

## 愛媛県の位置

令和6年度の愛媛県は、

- 積立基金合計：{fmt(eh.get('fund_total_million_yen')/100 if eh.get('fund_total_million_yen') is not None else None,1)}億円
- 有価証券残高：{fmt(eh.get('securities_million_yen')/100 if eh.get('securities_million_yen') is not None else None,1)}億円（全国{rank_sec_amt}位）
- 有価証券比率：{fmt(eh.get('securities_ratio_pct'))}%（全国{rank_sec}位）
- 現金・預金比率：{fmt(eh.get('cash_deposit_ratio_pct'))}%
- 地方債比率：{fmt(eh.get('local_bond_ratio_pct'))}%
- 基金/標準財政規模：{fmt(eh.get('fund_to_standard_scale_pct'))}%
- R4→R6有価証券比率変化：{fmt(w_eh.get('R4_R6_securities_ratio_change_pt'))}pt（全国{rank_shift}位）
- 類型：{w_eh.get('typology')}

有価証券比率で愛媛県の前後3団体程度：
"""
    for r in neighbors:
        mark = " **←愛媛県**" if r["prefecture"] == "愛媛県" else ""
        analysis += f"\n- {r['prefecture']}：{r['securities_ratio_pct']:.2f}%{mark}"

    analysis += "\n\n## 第2段階で追加調査すべき都道府県\n"
    for c in candidates:
        analysis += f"\n- **{c['prefecture']}**：{c['reason']}"

    analysis += """

## 解釈上の留意点

1. 本分析の「有価証券」は「国債」と同義ではない。表31では有価証券全体と、その内数として地方債までは全国統一で把握できるが、国債、政府保証債、財投機関債等への完全な分解はできない。
2. 有価証券比率が高いこと自体を運用の優劣とは評価しない。基金の取崩し予定、流動性、デュレーション、金利リスク、ALM等の検討が必要である。
3. 表31は年度末現在高であり、年度中平均残高や年間運用額とは異なる。
4. 東京都は絶対額が突出するため、残高比較に加え比率・中央値を併用する。
5. `other_assets_million_yen` は、表31の「4.出資金」と「5.その他」を明示的に合算したものであり、残差で補完したものではない。

## QA

完全性、重複、資産内訳整合、地方債内数、比率範囲の検査結果は `processed/QA.csv` を参照。重大な不整合がある場合は `DATASET INCOMPLETE` とする。
"""
    (ROOT / "prefecture_fund_investment_analysis.md").write_text(analysis, encoding="utf-8")

    # Root README.
    readme = f"""# saiken — 都道府県基金・債券運用分析

日経新聞「自治体の国債購入 急増」の問題意識を踏まえ、総務省・e-Statの全国統一統計だけで47都道府県の基金運用を比較するデータセットです。

## 第1段階

対象：令和4～6年度決算（FY2022～FY2024）

一次資料：総務省「地方財政状況調査（都道府県分）」表01、02、31。

主成果物：

- `processed/prefecture_fund_investment_R4_R6.csv` — long形式（47都道府県×3年度）
- `processed/wide_data.csv` — wide形式（47都道府県）
- `processed/R6_rankings.csv` — 主要6ランキング
- `processed/ehime_analysis.csv` — 愛媛県の全国ポジション
- `processed/source_dictionary.csv` — 変数別の一次資料・列名・URL
- `processed/QA.csv` — データ品質監査
- `processed/stage2_candidates.csv` — 第2段階候補県
- `prefecture_fund_investment_analysis.md` — 日本語分析レポート
- `charts/` — 図表
- `raw/` — e-Statから取得した原CSV

注意：第1段階で比較するのは「基金に占める有価証券運用」であり、「国債購入額ランキング」ではありません。

現在の判定：**{status}**
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")

    summary = {"status": status, "severe_issues": severe, "rows_long": len(long_rows), "rows_wide": len(wide_rows), "ehime": {"R6_securities_ratio_pct": eh.get("securities_ratio_pct"), "rank": rank_sec, "R4_R6_change_pt": w_eh.get("R4_R6_securities_ratio_change_pt"), "change_rank": rank_shift}}
    (PROCESSED / "run_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not severe else 2


if __name__ == "__main__":
    raise SystemExit(main())
