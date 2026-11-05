"""Checks the upstream watch's decisions against stubbed downloads.

scripts/check_upstream_release.py downloads the publication from NIST. These tests replace
its one network call, `_download`, so they run offline.
"""

import importlib.util
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"


@pytest.fixture
def watch():
    """A fresh copy of the script."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """The same bytes at the pinned address exit 0."""
    watch._download = lambda url: (watch.UPSTREAM / "NIST.AI.600-1.pdf").read_bytes()
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "`upstream/NIST.AI.600-1.pdf` matches" in text


def test_nist_changes_the_publication(watch, tmp_path):
    """Other bytes at the pinned address set attention and name the file."""
    watch._download = lambda url: b"another edition"
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "now serves other bytes than `upstream/NIST.AI.600-1.pdf`" in text


def test_a_failed_download_still_writes_a_report(watch, tmp_path):
    """A download that fails is reported as unfinished."""

    def fail(url):
        raise urllib.error.URLError("Connection refused")

    watch._download = fail
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The download could not finish" in text


def test_a_redirect_to_plain_http_is_refused(watch):
    """A file is followed only over https."""
    handler = watch._HttpsOnly()
    with pytest.raises(urllib.error.URLError):
        handler.redirect_request(None, None, 302, "Found", {}, "http://example.org/x")
