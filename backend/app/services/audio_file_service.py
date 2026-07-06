from sqlalchemy.orm import Session

from app.repositories.audio_file_repository import (
    get_all_audio_files,
    get_audio_file,
)


def list_audio_files(session: Session):
    return get_all_audio_files(session)


def get_audio_file_by_id(session: Session, audio_file_id: int):
    return get_audio_file(session, audio_file_id)