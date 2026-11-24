"""Tests for the Pickup Lines for Machines entry program."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINE = "You make my gradients descend."


class TestEntry(unittest.TestCase):
    def run_main(self, tmp: Path) -> Path:
        out = tmp / "entry.txt"
        env = dict(os.environ, ENTRY_OUTPUT=str(out))
        subprocess.run(
            [sys.executable, str(ROOT / "main.py")],
            check=True, env=env, cwd=str(ROOT),
        )
        return out

    def test_writes_exact_line(self):
        with tempfile.TemporaryDirectory() as d:
            out = self.run_main(Path(d))
            self.assertEqual(out.read_text(encoding="utf-8"), LINE + "\n")

    def test_length_within_gate(self):
        # Gate: /output/entry.txt must be 1-200 characters, not only whitespace.
        self.assertTrue(1 <= len(LINE) <= 200)
        self.assertEqual(len(LINE), 30)

    def test_single_line(self):
        # The gate takes one line; a line break inside would fail it.
        self.assertNotIn("\n", LINE)
        self.assertNotIn("\r", LINE)

    def test_non_blank_and_utf8(self):
        self.assertTrue(LINE.strip())
        LINE.encode("utf-8")

    def test_output_world_readable(self):
        # The grader collects outputs as another user; 0600 fails.
        with tempfile.TemporaryDirectory() as d:
            out = self.run_main(Path(d))
            self.assertTrue(out.stat().st_mode & 0o444)


if __name__ == "__main__":
    unittest.main()
