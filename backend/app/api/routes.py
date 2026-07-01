from fastapi import APIRouter

from app.schemas.playlist import PlaylistResponse
from app.schemas.track import TrackResponse
from app.db.session import SessionLocal
from app.services.playlist_service import (
    get_playlist,
    list_playlist_tracks,
    list_playlists,
)
router = APIRouter()


@router.get("/")
def root():
    return {"message": "Welcome to DJOS"}


@router.get("/health")
def health():
    return {"status": "ok", "service": "DJOS API", "version": "0.1.0"}

@router.get("/playlists", response_model=list[PlaylistResponse])
def get_playlists():
    with SessionLocal() as session:
        playlists = list_playlists(session)

        return playlists

@router.get("/playlists/{playlist_id}", response_model=PlaylistResponse)
def get_playlist_by_id(playlist_id: int):
    with SessionLocal() as session:
        playlist = get_playlist(session, playlist_id)

        if playlist is None:
            return {"error": "Playlist not found"}

        return playlist

@router.get(
    "/playlists/{playlist_id}/tracks",
    response_model=list[TrackResponse],
)
def get_tracks_for_playlist(playlist_id: int):
    with SessionLocal() as session:
        tracks = list_playlist_tracks(session, playlist_id)

        return tracks
