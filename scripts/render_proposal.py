#!/usr/bin/env python3
"""Render a Niagara Visual Diff proposal JSON into a standalone HTML page."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


MARKER = "/*__NIAGARA_PROPOSAL__*/ null"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("proposal", type=Path, help="Input proposal JSON file")
    parser.add_argument("--output", type=Path, required=True, help="Output HTML file")
    args = parser.parse_args()

    proposal = json.loads(args.proposal.read_text(encoding="utf-8"))
    if not isinstance(proposal, dict) or not isinstance(proposal.get("changes", []), list):
        parser.error("proposal must be a JSON object with a changes array")

    template = Path(__file__).resolve().parents[1] / "assets" / "proposal-template.html"
    html = template.read_text(encoding="utf-8")
    if html.count(MARKER) != 1:
        parser.error("HTML template must contain exactly one proposal marker")

    payload = json.dumps(proposal, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html.replace(MARKER, payload), encoding="utf-8")
    print(f"Rendered {len(proposal.get('changes', []))} change(s) to {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
