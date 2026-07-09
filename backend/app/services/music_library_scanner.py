from pathlib import Path


SUPPORTED_AUDIO_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".aiff",
    ".aif",
    ".m4a",
}


def scan_music_folder(folder_path: str) -> list[Path]:
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {folder}")

    audio_files: list[Path] = []

    for file_path in folder.rglob("*"):
        if file_path.is_file():
            extension = file_path.suffix.lower()

            if extension in SUPPORTED_AUDIO_EXTENSIONS:
                audio_files.append(file_path)

    return sorted(audio_files)