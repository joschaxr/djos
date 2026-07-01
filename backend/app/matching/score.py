from difflib import SequenceMatcher

from app.matching.normalize import normalize


def similarity_score(left: str, right: str) -> float:
    """
    Berechnet eine einfache Textähnlichkeit zwischen 0 und 1.
    """

    left_normalized = normalize(left)
    right_normalized = normalize(right)

    return SequenceMatcher(
        None,
        left_normalized,
        right_normalized,
    ).ratio()