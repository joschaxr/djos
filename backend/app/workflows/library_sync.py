from sqlalchemy.orm import Session

from app.audio.importer import import_audio_library
from app.repositories.audio_file_repository import get_all_audio_files


def sync_library(
    session: Session,
    directory: str,
):
    """
    Synchronisiert die lokale Musikbibliothek.

    1. Dateien scannen
    2. AudioFiles speichern
    3. AudioFiles erneut laden
    4. (später) Matching starten
    5. (später) Analyse starten
    """

    import_audio_library(directory)

    audio_files = get_all_audio_files(session)

    print(f"{len(audio_files)} AudioFiles in Datenbank.")

    return audio_files