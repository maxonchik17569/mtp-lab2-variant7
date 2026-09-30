"""Tests for the minimum element task."""

import unittest

from lab2.minimum import min_element


class MinElementTests(unittest.TestCase):
    """Checks for :func:`min_element`."""

    def test_regular_list(self) -> None:
        """The smallest value is returned."""
        self.assertEqual(min_element([4, 2, 9, 1]), 1)

    def test_negative_values(self) -> None:
        """Negative values work as well."""
        self.assertEqual(min_element([-3, -1, -7]), -7)

    def test_empty_list(self) -> None:
        """An empty sequence is rejected."""
        with self.assertRaises(ValueError):
            min_element([])


if __name__ == "__main__":
    unittest.main()
