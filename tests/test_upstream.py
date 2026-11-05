"""Checks that upstream/ holds the edition the schema renders, and that the vendored
modules of lmodel/nist-ai-100-1 are the pinned ones."""

import hashlib
import importlib.util
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
UPSTREAM = ROOT / "upstream"
SCHEMA = ROOT / "src" / "nist_ai_600_1" / "schema" / "nist_ai_600_1.yaml"
WATCH = ROOT / "scripts" / "check_upstream_release.py"
VENDORED = SCHEMA.parent / "nist_ai_100_1"

# Each module of lmodel/nist-ai-100-1 this schema imports, as of its commit
# 64b373eb797f85d3ceaa56ec9a879b316ab91278. Vendor from its release, then move the pins.
VENDORED_PINS = {
    "nist_ai_100_1_base.yaml": "6334c56f4481dfa531aa16d2b166410fc5e23103504c3c56dea36e8ac992f86b",
    "nist_ai_100_1_profiles.yaml": "7a9844bcbe191ee309296bb2c2936b9831152bb7d36b90a367708ba93d3b3e65",
}


@lru_cache(maxsize=1)
def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _header():
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


def test_upstream_holds_only_the_pinned_file():
    """The publication is in upstream/, and nothing else is there."""
    assert {p.name for p in UPSTREAM.iterdir()} == set(_watch().PINNED_DOWNLOADS)


def test_download_matches_its_pin():
    """The publication has the SHA-256 the watch pins."""
    watch = _watch()
    for name, (_url, sha256) in watch.PINNED_DOWNLOADS.items():
        assert hashlib.sha256((UPSTREAM / name).read_bytes()).hexdigest() == sha256


def test_header_names_the_pinned_edition():
    """The header's source is the identifier the watch names."""
    assert _header()["source"] == f"https://doi.org/{_watch().PINNED_DOI}"


def test_every_module_carries_the_header():
    """Each module carries the version, the source and the licence of the umbrella."""
    header = _header()
    for path in SCHEMA.parent.glob("*.yaml"):
        module = yaml.safe_load(path.read_text(encoding="utf-8"))
        for key in ("version", "source", "license"):
            assert module[key] == header[key], (path.name, key)


def test_vendored_modules_are_the_pinned_ones():
    """The vendored modules are byte for byte the pinned files, and no others."""
    assert {p.name for p in VENDORED.iterdir()} == set(VENDORED_PINS)
    for name, sha256 in VENDORED_PINS.items():
        assert hashlib.sha256((VENDORED / name).read_bytes()).hexdigest() == sha256, (
            name
        )
