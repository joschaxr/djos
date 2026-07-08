import re


NOISE_PATTERNS = [
    r"\(official video\)",
    r"\(official audio\)",
    r"\(official lyric video\)",
    r"\(offizielles musikvideo\)",
    r"\(lyrics?\)",
    r"\(visualizer\)",
    r"\(audio\)",
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


def split_artist_title(
    artist: str | None,
    title: str | None,
) -> tuple[str | None, str | None]:
    """
    Entfernt doppelte Artistnamen aus dem Titel.

    Beispiel:

    Artist:
        Ikkimel

    Title:
        Ikkimel - ASZENDENT BITCH

    →

    Artist:
        Ikkimel

    Title:
        ASZENDENT BITCH
    """

    if not artist or not title:
        return artist, title

    prefix = artist.lower() + " - "

    if title.lower().startswith(prefix):
        title = title[len(prefix):]

    return artist, title