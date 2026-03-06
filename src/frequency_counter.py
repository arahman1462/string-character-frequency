"""
Character Frequency Counter

Counts occurrences of characters in a string while preserving
the order of first appearance.
"""


def char_frequency(text: str) -> dict:
    """
    Count character frequency.

    Args:
        text (str): input string

    Returns:
        dict: ordered character frequency
    """

    if not text:
        return {}

    frequency = {}

    for char in text:
        if char.isspace():
            continue

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


def format_output(freq: dict) -> str:
    return ", ".join(f"{k}:{v}" for k, v in freq.items())