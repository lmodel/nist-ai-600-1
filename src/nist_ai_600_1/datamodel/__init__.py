"""Data model package for nist-ai-600-1."""

from pathlib import Path
from .nist_ai_600_1 import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "nist_ai_600_1.yaml"
