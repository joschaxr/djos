from dataclasses import dataclass


@dataclass
class SearchQuery:
    artist: str | None
    title: str
    album: str | None = None


@dataclass
class MatchCandidate:
    spotify_id: str

    artist: str
    title: str
    album: str | None

    duration_ms: int | None

    popularity: int | None

    score: float = 0.0