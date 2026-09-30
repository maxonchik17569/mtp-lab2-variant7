"""Tests for the factorial task."""

import unittest

from lab2.factorial import factorial


class FactorialTests(unittest.TestCase):
    """Checks for :func:`factorial`."""

    def test_zero(self) -> None:
        """Zero factorial equals one."""
        self.assertEqual(factorial(0), 1)

    def test_regular_value(self) -> None:
        """A regular value multiplies all integers up to it."""
        self.assertEqual(factorial(6), 720)

    def test_negative_value(self) -> None:
        """Negative values are rejected."""
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
