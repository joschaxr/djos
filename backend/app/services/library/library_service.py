from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.orm import Session

from app.intelligence.metadata.resolver import resolve_metadata
from app.repositories.audio_file_repository import save_audio_file
from app.services.library.metadata_extractor import extract_metadata
from app.services.music_library_scanner import scan_music_folder


@dataclass
class AudioFileImportData:
    path: Path
    filename: str
    extension: str
    artist: str | None
    title: str | None
    album: str | None
    duration_ms: int | None
    match_score: float | None = 0.0


def import_music_folder(
    session: Session,
    folder_path: str,
):
    file_paths = scan_music_folder(folder_path)

    imported_files = []

    for file_path in file_paths:
        metadata = extract_metadata(file_path)
        resolved = resolve_metadata(metadata)

        import_data = AudioFileImportData(
            path=metadata.path,
            filename=metadata.filename,
            extension=metadata.extension,
            artist=resolved.artist,
            title=resolved.title,
            album=resolved.album,
            duration_ms=metadata.duration_ms,
            match_score=0.0,
        )

        audio_file = save_audio_file(
            session,
            import_data,
        )

        imported_files.append(audio_file)

    session.commit()

    return imported_files