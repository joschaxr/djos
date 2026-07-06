from sqlalchemy.orm import Session

from app.models.audio_file import AudioFile


def get_all_audio_files(session: Session) -> list[AudioFile]:
    return (
        session.query(AudioFile)
        .order_by(AudioFile.artist, AudioFile.title)
        .all()
    )


def get_audio_file(session: Session, audio_file_id: int) -> AudioFile | None:
    return (
        session.query(AudioFile)
        .filter(AudioFile.id == audio_file_id)
        .first()
    )


def get_audio_file_by_path(
    session: Session,
    path: str,
) -> AudioFile | None:
    return (
        session.query(AudioFile)
        .filter(AudioFile.path == path)
        .first()
    )


def save_audio_file(
    session: Session,
    audio_file_data,
) -> AudioFile:
    existing = get_audio_file_by_path(
        session,
        str(audio_file_data.path),
    )

    if existing:
        existing.filename = audio_file_data.filename
        existing.extension = audio_file_data.extension
        existing.artist = audio_file_data.artist
        existing.title = audio_file_data.title
        existing.album = audio_file_data.album
        existing.duration_ms = audio_file_data.duration_ms
        existing.match_score = audio_file_data.match_score

        return existing

    audio_file = AudioFile(
        path=str(audio_file_data.path),
        filename=audio_file_data.filename,
        extension=audio_file_data.extension,
        artist=audio_file_data.artist,
        title=audio_file_data.title,
        album=audio_file_data.album,
        duration_ms=audio_file_data.duration_ms,
        match_score=audio_file_data.match_score,
    )

    session.add(audio_file)

    return audio_file