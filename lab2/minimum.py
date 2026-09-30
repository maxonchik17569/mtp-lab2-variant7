"""Task 9 (medium): minimum element of a sequence."""


def min_element(items: list):
    """Return the smallest element of ``items``.

    Args:
        items: non-empty sequence of mutually comparable elements.

    Returns:
        The minimum value.

    Raises:
        ValueError: if the sequence is empty.
    """
    if not items:
        raise ValueError("sequence must not be empty")
    smallest = items[0]
    for item in items[1:]:
        if item < smallest:
            smallest = item
    return smallest
