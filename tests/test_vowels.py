"""Tests for the vowel counting task."""

import unittest

from lab2.vowels import count_vowels


class CountVowelsTests(unittest.TestCase):
    """Checks for :func:`count_vowels`."""

    def test_russian_word(self) -> None:
        """Russian vowels are recognised."""
        self.assertEqual(count_vowels("привет"), 2)

    def test_english_word(self) -> None:
        """English vowels are recognised in any case."""
        self.assertEqual(count_vowels("Hello"), 2)

    def test_empty_string(self) -> None:
        """An empty string contains no vowels."""
        self.assertEqual(count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
