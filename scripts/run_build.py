#!/usr/bin/env python3
"""Compatibility runner for e-Stat year-specific column labels.

The Local Public Finance Survey labels the current-year fund balance with the
literal fiscal year (e.g. `006:令和4年度末現在高`) instead of a stable
`当年度末現在高` label. Patch only that schema lookup, then execute the
canonical builder.
"""
from __future__ import annotations

import re
import build_dataset as b

_original_col_by = b.col_by


def _patched_col_by(headers, required, forbidden=()):
    result = _original_col_by(headers, required, forbidden)
    if result is not None:
        return result

    req_norm = [b.norm(x) for x in required]
    if any("当年度末現在高" in x for x in req_norm):
        candidates = [
            h for h in headers
            if "年度末現在高" in b.norm(h) and "管理状況" not in b.norm(h)
        ]
        if candidates:
            def key(h):
                m = re.match(r"(\d+):", h)
                return int(m.group(1)) if m else -1
            # Previous-year and current-year balances can both exist; the
            # current-year balance is the later numbered source column.
            return max(candidates, key=key)
    return None


b.col_by = _patched_col_by

if __name__ == "__main__":
    raise SystemExit(b.main())
