from dataclasses import dataclass

from app.intelligence.metadata.cleaner import clean_title
from app.intelligence.metadata.parser import parse_artist_title
from app.services.library.metadata_extractor import AudioMetadata


@dataclass
class ResolvedMetadata:
    artist: str | None
    title: str
    album: str | None
    confidence: float
    source: str


def resolve_metadata(metadata: AudioMetadata) -> ResolvedMetadata:
    filename_cleaned = clean_title(metadata.filename)
    filename_parsed = parse_artist_title(filename_cleaned)

    tag_title_cleaned = clean_title(metadata.title or "")
    tag_title_parsed = parse_artist_title(tag_title_cleaned)

    if filename_parsed.artist and filename_parsed.title:
        return ResolvedMetadata(
            artist=filename_parsed.artist,
            title=filename_parsed.title,
            album=metadata.album,
            confidence=0.75,
            source="filename",
        )

    if metadata.artist and metadata.title:
        return ResolvedMetadata(
            artist=metadata.artist,
            title=tag_title_parsed.title or metadata.title,
            album=metadata.album,
            confidence=0.7,
            source="tags",
        )

    return ResolvedMetadata(
        artist=metadata.artist,
        title=metadata.title or metadata.filename,
        album=metadata.album,
        confidence=0.4,
        source="fallback",
    )