from app.repositories.playlist_repository import (
    get_all_playlists,
    get_playlist_by_id,
)
from app.repositories.track_repository import (
    get_all_tracks,
    get_track_analysis,
    get_track_by_id,
    get_tracks_by_playlist_id,
    search_tracks,
)


def list_playlists(session):
    return get_all_playlists(session)


def get_playlist(session, playlist_id: int):
    return get_playlist_by_id(session, playlist_id)


def list_playlist_tracks(session, playlist_id: int):
    return get_tracks_by_playlist_id(session, playlist_id)

def list_tracks(session):
    return get_all_tracks(session)


def get_track(session, track_id: int):
    return get_track_by_id(session, track_id)

def search_tracks_by_query(session, query: str):
    return search_tracks(session, query)    

def get_analysis_for_track(session, track_id: int):
    return get_track_analysis(session, track_id)  