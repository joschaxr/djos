from app.audio.library import scan_library
from app.audio.metadata import read_audio_metadata
from app.db.session import SessionLocal
from app.repositories.audio_file_repository import save_audio_file


def import_audio_library(directory: str):
    audio_files = scan_library(directory)

    with SessionLocal() as session:
        enriched_files = [
            read_audio_metadata(audio_file)
            for audio_file in audio_files
        ]

        for audio_file in enriched_files:
            save_audio_file(session, audio_file)

        session.commit()

    print(f"Audiodateien gespeichert: {len(enriched_files)}")

    for audio_file in enriched_files[:20]:
        print(audio_file.artist, "-", audio_file.title, "|", audio_file.path)

    return enriched_files