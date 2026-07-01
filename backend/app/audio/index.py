from dataclasses import dataclass
from pathlib import Path


@dataclass
class AudioFile:
    path: Path
    filename: str
    extension: str

    artist: str | None = None
    title: str | None = None
    album: str | None = None

    duration_ms: int | None = None

    spotify_track_id: int | None = None

    match_score: float = 0.0