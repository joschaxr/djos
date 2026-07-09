import re


NOISE_PATTERNS = [
    r"\(official video\)",
    r"\(official audio\)",
    r"\(official visualizer\)",
    r"\(official music video\)",
    r"\(offizielles musikvideo\)",
    r"\(lyrics?\)",
    r"\(lyric video\)",
    r"\(audio\)",
    r"\(video\)",
    r"\(hd\)",
    r"\(hq\)",
    r"\(prod\.? by [^)]+\)",
    r"\(prod\.? [^)]+\)",
    r"\(produced by [^)]+\)",
    r"official music video",
    r"offizielles musikvideo",
]


def clean_title(title: str) -> str:
    cleaned = title

    for pattern in NOISE_PATTERNS:
        cleaned = re.sub(
            pattern,
            "",
            cleaned,
            flags=re.IGNORECASE,
        )

    cleaned = cleaned.replace("_", " ")

    cleaned = re.sub(
        r"\s+",
        " ",
        cleaned,
    )

    return cleaned.strip(" -_")