#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check upstream/ against the publication NIST serves.

upstream/NIST.AI.600-1.pdf can change at NIST without any change in this repository. NIST
publishes it in no repository and with no release to ask about, so the script downloads
the file and compares its SHA-256 with the pin. NIST may also publish a revision under a
new identifier. That cannot be predicted from the pinned one, so the publication's AI RMF
site is the place a person looks when this script fires or a reader reports one.

It prints a Markdown report and exits 1 when the file differs or the check could not
finish. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "upstream"
USER_AGENT = "lmodel-nist-ai-600-1-upstream-check"

# The edition the schema renders, as its digital object identifier. The schema header's
# `source` carries the same address, and tests/test_upstream.py holds the two equal.
PINNED_DOI = "10.6028/NIST.AI.600-1"

# The file, the address it is read from, and its SHA-256 on the date of the last
# comparison, 2026-11-05. doi.org redirects to this address over plain http, so the file
# is read here instead.
PINNED_DOWNLOADS = {
    "NIST.AI.600-1.pdf": (
        "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
        "6e73620ab6b64e90ef2c04bf0e0d6246185a2f4b1b13cab0df494496cff89b6a",
    ),
}


# The hosts a download may reach, and the most it reads. The pinned files are far smaller.
ALLOWED_HOSTS = {"nvlpubs.nist.gov"}
MAX_BYTES = 20 * 1024 * 1024


class _HttpsOnly(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only over https, and only to a host the script reads from."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
            raise urllib.error.URLError(f"refused a redirect to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _download(url: str) -> bytes:
    """A public file from NIST. It carries no token."""
    opener = urllib.request.build_opener(_HttpsOnly)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with opener.open(req, timeout=120) as resp:
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise urllib.error.URLError(f"{url} answered with more than {MAX_BYTES} bytes")
    return data


def check_downloads() -> tuple[list[str], bool]:
    """Report whether the publication is the pinned bytes."""
    report, attention = [f"- Pinned edition: https://doi.org/{PINNED_DOI}."], False
    for name, (url, pinned) in sorted(PINNED_DOWNLOADS.items()):
        if hashlib.sha256((UPSTREAM / name).read_bytes()).hexdigest() != pinned:
            attention = True
            report.append(
                f"- **`upstream/{name}` is not the pinned file.** Restore it."
            )
        if hashlib.sha256(_download(url)).hexdigest() == pinned:
            report.append(f"- `upstream/{name}` matches {url} byte for byte.")
        else:
            attention = True
            report.append(
                f"- **{url} now serves other bytes than `upstream/{name}`.** Read the change, "
                "replace the file, move the pin, rebuild the catalogue and run `just test`."
            )
    return report, attention


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    try:
        lines, attention = check_downloads()
    except (urllib.error.URLError, TimeoutError, OSError) as err:
        lines, attention = [f"- **The download could not finish: {err}.**"], True
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
