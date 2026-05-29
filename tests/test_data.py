"""Data tests for the NIST AI 600-1 LinkML datamodel.

Each fixture under ``tests/data/valid/`` and ``tests/data/invalid/``
is named ``<ClassName>-<descriptor>.yaml`` per the test corpus
convention; the class name (the part before the first ``-``) is
resolved against the generated Python datamodel and used as the
``target_class`` for ``yaml_loader.load``.

* Valid fixtures must load without raising.
* Invalid fixtures must raise ``TypeError`` (unknown slot) or
  ``ValueError`` (unknown enum value) - the two failure modes the
  linkml_runtime YAML loader catches at construction time. Pattern
  / cardinality / structural-rule violations are not enforced by
  the loader; those belong in ``linkml-validate`` based tests.
"""

import glob
import os
from pathlib import Path

import pytest

import nist_ai_600_1.datamodel.nist_ai_600_1
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml")))
INVALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml")))


def _target_class(filepath):
    """Resolve the datamodel class for a fixture filename."""
    target_class_name = Path(filepath).stem.split("-")[0]
    return getattr(nist_ai_600_1.datamodel.nist_ai_600_1, target_class_name)


@pytest.mark.parametrize(
    "filepath",
    VALID_EXAMPLE_FILES,
    ids=[Path(p).name for p in VALID_EXAMPLE_FILES],
)
def test_valid_data_files(filepath):
    """Every valid fixture loads as an instance of its target class."""
    tgt_class = _target_class(filepath)
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj is not None
    assert isinstance(obj, tgt_class)


@pytest.mark.parametrize(
    "filepath",
    INVALID_EXAMPLE_FILES,
    ids=[Path(p).name for p in INVALID_EXAMPLE_FILES],
)
def test_invalid_data_files(filepath):
    """Every invalid fixture must be rejected by the YAML loader."""
    tgt_class = _target_class(filepath)
    with pytest.raises((TypeError, ValueError)):
        yaml_loader.load(filepath, target_class=tgt_class)
