"""Task 3 (medium): factorial of a number."""


def factorial(n: int) -> int:
    """Return ``n!`` computed with an iterative loop.

    Args:
        n: non-negative integer.

    Returns:
        Product of all integers from 1 to ``n``; ``0!`` is 1.

    Raises:
        ValueError: if ``n`` is negative.
    """
    if n < 0:
        raise ValueError("factorial is undefined for negatives")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result
