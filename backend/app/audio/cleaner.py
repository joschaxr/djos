import re


NOISE_PATTERNS = [
    r"\(official video\)",
    r"\(official audio\)",
    r"\(offizielles musikvideo\)",
    r"\(lyrics?\)",
    r"\(visualizer\)",
    r"\[official video\]",
    r"\[official audio\]",
    r"\[lyrics?\]",
    r"\bhd\b",
    r"\b4k\b",
]


def clean_text(value: str | None) -> str | None:
    if not value:
        return value

    cleaned = value

    for pattern in NOISE_PATTERNS:
        cleaned = re.sub(
            pattern,
            "",
            cleaned,
            flags=re.IGNORECASE,
        )

    cleaned = cleaned.replace("_", " ")
    cleaned = re.sub(r"\s+", " ", cleaned)

    return cleaned.strip()