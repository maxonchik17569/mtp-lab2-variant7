"""Tests for the word frequency task."""

import os
import tempfile
import unittest

from lab2.wordfreq import word_frequency


class WordFrequencyTests(unittest.TestCase):
    """Checks for :func:`word_frequency`."""

    def setUp(self) -> None:
        """Write a sample text file."""
        handle = tempfile.NamedTemporaryFile(
            "w", suffix=".txt", delete=False, encoding="utf-8"
        )
        with handle:
            handle.write("Cat cat dog. CAT!\nbird, cat")
        self.path = handle.name

    def tearDown(self) -> None:
        """Remove the sample file."""
        os.unlink(self.path)

    def test_counts_ignore_case_and_punctuation(self) -> None:
        """Words are normalised before counting."""
        self.assertEqual(
            word_frequency(self.path),
            {"cat": 4, "dog": 1, "bird": 1},
        )


if __name__ == "__main__":
    unittest.main()
