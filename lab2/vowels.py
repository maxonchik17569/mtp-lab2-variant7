"""Task 7 (medium): count vowels in a string."""

VOWELS = "аеёиоуыэюяaeiouy"


def count_vowels(text: str) -> int:
    """Return how many vowel characters ``text`` contains.

    Latin and Russian vowels are recognised in any letter case.

    Args:
        text: source string, may be empty.

    Returns:
        Number of vowel characters.
    """
    total = 0
    for char in text.lower():
        if char in VOWELS:
            total += 1
    return total
