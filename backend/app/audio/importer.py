from app.audio.library import scan_library


def import_audio_library(directory: str):
    """
    Importiert eine lokale Musikbibliothek.

    Aktuell:
    - scannt den Ordner
    - gibt gefundene Audiodateien aus

    Später:
    - liest Metadaten
    - matcht Dateien mit Tracks
    - speichert Audioquellen
    - startet Audioanalyse
    """

    audio_files = scan_library(directory)

    print(f"Audiodateien gefunden: {len(audio_files)}")

    for audio_file in audio_files[:20]:
        print(audio_file.path)

    return audio_files