from difflib import SequenceMatcher

from app.intelligence.matching.normalizer import normalize


def text_score(left: str | None, right: str | None) -> float:
    left_normalized = normalize(left)
    right_normalized = normalize(right)

    if not left_normalized or not right_normalized:
        return 0.0

    return SequenceMatcher(
        None,
        left_normalized,
        right_normalized,
    ).ratio()


def duration_score(
    left_duration_ms: int | None,
    right_duration_ms: int | None,
) -> float:
    if not left_duration_ms or not right_duration_ms:
        return 0.0

    difference = abs(left_duration_ms - right_duration_ms)

    if difference <= 2000:
        return 1.0

    if difference <= 5000:
        return 0.8

    if difference <= 10000:
        return 0.5

    return 0.0