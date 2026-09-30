"""Tests for the guessing game task."""

import unittest

from lab2.guess_number import play_guess_number


class GuessNumberTests(unittest.TestCase):
    """Checks for :func:`play_guess_number`."""

    def test_number_is_guessed(self) -> None:
        """A correct guess wins the game."""
        answers = iter(["50"])
        won = play_guess_number(
            secret=50,
            reader=lambda _: next(answers),
            writer=lambda _: None,
        )
        self.assertTrue(won)

    def test_attempts_run_out(self) -> None:
        """Wrong guesses exhaust the attempts."""
        answers = iter(["1", "2"])
        won = play_guess_number(
            secret=99,
            max_attempts=2,
            reader=lambda _: next(answers),
            writer=lambda _: None,
        )
        self.assertFalse(won)

    def test_invalid_input_is_skipped(self) -> None:
        """Non-integer input does not consume a try."""
        answers = iter(["abc", "7"])
        won = play_guess_number(
            secret=7,
            reader=lambda _: next(answers),
            writer=lambda _: None,
        )
        self.assertTrue(won)


if __name__ == "__main__":
    unittest.main()
