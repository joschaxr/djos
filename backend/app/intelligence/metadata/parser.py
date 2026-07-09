from dataclasses import dataclass


@dataclass
class ParsedMetadata:
    artist: str | None
    title: str


def parse_artist_title(
    text: str,
) -> ParsedMetadata:
    cleaned = text.strip()

    separators = [
        " - ",
        " – ",
        " — ",
    ]

    for separator in separators:
        if separator in cleaned:
            artist, title = cleaned.split(separator, 1)

            return ParsedMetadata(
                artist=artist.strip(),
                title=title.strip(),
            )

    return ParsedMetadata(
        artist=None,
        title=cleaned,
    )