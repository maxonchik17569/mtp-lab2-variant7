"""Task 5 (advanced): the "guess the number" game."""

import random


def play_guess_number(
    secret=None,
    max_attempts: int = 7,
    reader=input,
    writer=print,
) -> bool:
    """Play the guessing game until the number is found or tries run out.

    Args:
        secret: predefined number in 1..100; random when omitted.
        max_attempts: how many guesses the player may make.
        reader: callable asking for the next guess.
        writer: callable printing feedback lines.

    Returns:
        ``True`` if the number was guessed, ``False`` otherwise.
    """
    if secret is None:
        secret = random.randint(1, 100)
    writer("Guess the integer from 1 to 100.")
    for _ in range(max_attempts):
        line = reader("Your guess: ")
        try:
            guess = int(line)
        except ValueError:
            writer("Please enter an integer.")
            continue
        if guess < secret:
            writer("Too small.")
        elif guess > secret:
            writer("Too large.")
        else:
            writer("Correct!")
            return True
    writer(f"The number was {secret}.")
    return False
