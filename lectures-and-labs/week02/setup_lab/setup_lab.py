"""Prove the environment works before the first exercise.

    python setup_lab.py

Checks the Python version, that the lab's files and packages are present,
whether this is your own copy of the repo, and whether the GitHub CLI is
signed in. It cannot see the editor's assistant -- that is what steps 3
and 4 of DIY 1 are for. Prints one line per check and exits non-zero if
anything essential is missing. It never prints a token or a key.
"""
from __future__ import annotations

import importlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
MODULE_REPO = "danielcregg/ai-assisted-programming"
PACKAGES = ("numpy", "pandas")   # DIY 2 imports pandas; requirements.txt lists both


def line(ok: bool, label: str, detail: str = "") -> bool:
    print(f"  [{'ok' if ok else '  '}] {label}{'  — ' + detail if detail else ''}")
    return ok


def run(*cmd: str) -> str | None:
    """stdout of a command, or None if it is missing or fails."""
    exe = shutil.which(cmd[0])
    if not exe:
        return None
    try:
        r = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() if r.returncode == 0 else None


def main() -> int:
    print("AIAP setup check\n")
    good = True

    v = sys.version_info
    good &= line(v >= (3, 10), f"Python {v.major}.{v.minor}",
                 "" if v >= (3, 10) else "3.10 or newer required")

    present = all((HERE / f).is_file() for f in ("README.md", "requirements.txt"))
    good &= line(present, "Lab files present", "" if present else "missing README.md or requirements.txt")

    missing = []
    for name in PACKAGES:
        try:
            importlib.import_module(name)
        except ImportError:
            missing.append(name)
    good &= line(not missing, " and ".join(PACKAGES) + " installed",
                 "" if not missing else "pip install -r requirements.txt")

    # The rest is reported, not required: none of it stops the lab, and all
    # of it is handled for you inside a Codespace.
    line(bool(os.environ.get("CODESPACES")), "Running in a Codespace",
         "" if os.environ.get("CODESPACES") else "fine if you set up locally")

    line(run("gh", "auth", "status") is not None, "GitHub CLI signed in",
         "" if run("gh", "auth", "status") is not None else
         "run: gh auth login  (a Codespace signs in for you)")

    origin = run("git", "remote", "get-url", "origin") or ""
    if not origin:
        line(False, "Your own copy of the repo", "no git remote found")
    elif MODULE_REPO in origin:
        line(False, "Your own copy of the repo",
             "this is the module repo itself; students work in a copy made with Use this template")
    else:
        line(True, "Your own copy of the repo")

    print()
    print("Ready." if good else "Something above needs fixing before you start.")
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
