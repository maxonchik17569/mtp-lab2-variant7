"""Task 7 (advanced): word frequency of a text file."""

import string


def word_frequency(path: str) -> dict:
    """Read a text file and count occurrences of every word.

    Punctuation around a word is stripped and letters are folded to
    lower case, so ``"Cat,"`` and ``"cat"`` share one counter.

    Args:
        path: path to a UTF-8 text file.

    Returns:
        Mapping of each word to the number of its occurrences.
    """
    counts = {}
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            for raw_word in line.split():
                word = raw_word.strip(string.punctuation).lower()
                if not word:
                    continue
                counts[word] = counts.get(word, 0) + 1
    return counts
