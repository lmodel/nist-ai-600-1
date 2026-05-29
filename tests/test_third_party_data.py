"""Third-party data tests.

Validates JSON fixtures supplied by external publishers (e.g., NIST)
that live under ``tests/data/third_party/<publisher>/``. Filename
convention mirrors the in-repo YAML fixtures:
``<TargetClass>-<short-description>.json`` so the target class is
derived from the filename stem.
"""

import glob
import os
from pathlib import Path

import pytest

import nist_ai_600_1.datamodel.nist_ai_600_1
from linkml_runtime.loaders import json_loader

DATA_DIR_THIRD_PARTY = Path(__file__).parent / "data" / "third_party" / "nist"

THIRD_PARTY_JSON_FILES = glob.glob(os.path.join(DATA_DIR_THIRD_PARTY, "*.json"))

# Per-fixture record counts, harvested by the `pytest_terminal_summary`
# hook in conftest.py to print a green per-source summary at the end of
# the (separate) third-party pytest run.
THIRD_PARTY_RECORD_COUNTS: dict[str, int] = {}


@pytest.mark.parametrize("filepath", THIRD_PARTY_JSON_FILES)
def test_third_party_nist_json(filepath):
    """Validate a third-party NIST JSON fixture against the schema."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        nist_ai_600_1.datamodel.nist_ai_600_1,
        target_class_name,
    )
    obj = json_loader.load(filepath, target_class=tgt_class)
    assert obj
    count = 1
    for attr in ("entries", "items", "records"):
        value = getattr(obj, attr, None)
        if isinstance(value, list):
            count = len(value)
            break
    THIRD_PARTY_RECORD_COUNTS[Path(filepath).name] = count
