"""Demo entry point: run ``python -m lab2``."""

import os
import tempfile

from lab2.factorial import factorial
from lab2.guess_number import play_guess_number
from lab2.minimum import min_element
from lab2.vowels import count_vowels
from lab2.wordfreq import word_frequency


def main() -> None:
    """Print results of every variant task."""
    print("Medium tasks")
    print('count_vowels("Привет, world") ->', count_vowels("Привет, world"))
    print("min_element([4, 2, 9, 1]) ->", min_element([4, 2, 9, 1]))
    print("factorial(6) ->", factorial(6))
    with tempfile.NamedTemporaryFile(
        "w", suffix=".txt", delete=False, encoding="utf-8"
    ) as handle:
        handle.write("Cat cat dog. Cat!")
        sample = handle.name
    try:
        print("word_frequency ->", word_frequency(sample))
    finally:
        os.unlink(sample)
    won = play_guess_number(secret=42, reader=lambda _: "42")
    print("play_guess_number(secret=42) ->", won)


if __name__ == "__main__":
    main()
