from pathlib import Path


SUPPORTED_AUDIO_FORMATS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aiff",
    ".m4a",
}


def scan_music_directory(directory: str) -> list[Path]:
    """
    Durchsucht einen Musikordner rekursiv nach Audiodateien.
    """

    root = Path(directory)

    if not root.exists():
        return []

    audio_files = []

    for file in root.rglob("*"):
        if file.suffix.lower() in SUPPORTED_AUDIO_FORMATS:
            audio_files.append(file)

    return audio_files