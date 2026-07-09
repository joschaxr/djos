from dataclasses import dataclass
from pathlib import Path

from mutagen import File


@dataclass
class AudioMetadata:
    path: Path

    filename: str
    extension: str

    artist: str | None
    title: str | None
    album: str | None

    duration_ms: int | None


def extract_metadata(
    file_path: Path,
) -> AudioMetadata:

    audio = File(file_path, easy=True)

    duration_ms = None

    if audio is not None and audio.info is not None:
        duration_ms = int(audio.info.length * 1000)

    def tag(name: str):
        if audio is None:
            return None

        value = audio.get(name)

        if value:
            return value[0]

        return None

    return AudioMetadata(
        path=file_path,
        filename=file_path.stem,
        extension=file_path.suffix.lower(),

        artist=tag("artist"),
        title=tag("title"),
        album=tag("album"),

        duration_ms=duration_ms,
    )