from sqlalchemy import select

from app.models.playlist import Playlist


def get_all_playlists(session) -> list[Playlist]:
    return session.scalars(select(Playlist)).all()


def get_playlist_by_id(session, playlist_id: int) -> Playlist | None:
    return session.get(Playlist, playlist_id)