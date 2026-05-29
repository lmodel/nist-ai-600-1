"""Pytest hooks for the nist-ai-600-1 test suite.

The only hook here is ``pytest_terminal_summary``, which prints a
green summary of third-party fixtures whose records were validated.
The hook is a no-op for the default pytest run (third-party tests are
ignored via ``addopts`` in ``pyproject.toml``); it only produces
output when ``just test-third-party`` runs the dedicated suite.
"""

from __future__ import annotations

import os
import sys

_GREEN = "\033[32m"
_BOLD = "\033[1m"
_RESET = "\033[0m"


def _colour(text: str, code: str) -> str:
    if sys.stdout.isatty() or os.environ.get("FORCE_COLOR"):
        return f"{code}{text}{_RESET}"
    return text


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    try:
        from tests.test_third_party_data import THIRD_PARTY_RECORD_COUNTS
    except Exception:  # pragma: no cover - third-party module not loaded
        return

    if not THIRD_PARTY_RECORD_COUNTS:
        return

    tr = terminalreporter
    tr.write_sep("=", "third-party records validated", bold=True)
    total = 0
    for name, count in sorted(THIRD_PARTY_RECORD_COUNTS.items()):
        line = f"  {name:50s} {count:>6d} record(s)"
        tr.write_line(_colour(line, _GREEN))
        total += count
    tr.write_line(_colour(f"  {'TOTAL':50s} {total:>6d} record(s)", _BOLD + _GREEN))
