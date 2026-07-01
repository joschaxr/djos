from app.audio.index import AudioFile
from app.audio.local import scan_music_directory


def scan_library(directory: str) -> list[AudioFile]:
    """
    Scannt eine Musikbibliothek und erstellt
    einen Index aller Audiodateien.
    """

    files = []

    for path in scan_music_directory(directory):
        files.append(
            AudioFile(
                path=path,
                filename=path.stem,
                extension=path.suffix.lower(),
            )
        )

    return files