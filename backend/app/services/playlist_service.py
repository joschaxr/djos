from app.repositories.playlist_repository import (
    get_all_playlists,
    get_playlist_by_id,
)
from app.repositories.track_repository import get_tracks_by_playlist_id


def list_playlists(session):
    return get_all_playlists(session)


def get_playlist(session, playlist_id: int):
    return get_playlist_by_id(session, playlist_id)


def list_playlist_tracks(session, playlist_id: int):
    return get_tracks_by_playlist_id(session, playlist_id)