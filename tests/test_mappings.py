"""Verify that LinkML schemas reflect the SSSOM mapping TSV files.

Wraps ``scripts/verify_mappings.py`` so it runs as part of the
default ``just test`` pytest invocation.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "verify_mappings.py"
_spec = importlib.util.spec_from_file_location("verify_mappings", _SCRIPT)
verify_mappings = importlib.util.module_from_spec(_spec)
sys.modules["verify_mappings"] = verify_mappings
_spec.loader.exec_module(verify_mappings)


def test_sssom_mappings_match_schema():
    assert verify_mappings.main([]) == 0
