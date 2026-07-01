from fastapi import APIRouter

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

@router.get("/playlists")
def get_playlists():
    with SessionLocal() as session:
        playlists = list_playlists(session)

        return [
            {
                "id": playlist.id,
                "name": playlist.name,
                "spotify_id": playlist.spotify_id,
                "owner": playlist.owner,
            }
            for playlist in playlists
        ]

@router.get("/playlists/{playlist_id}")
def get_playlist_by_id(playlist_id: int):
    with SessionLocal() as session:
        playlist = get_playlist(session, playlist_id)

        if playlist is None:
            return {"error": "Playlist not found"}

        return {
            "id": playlist.id,
            "name": playlist.name,
            "spotify_id": playlist.spotify_id,
            "owner": playlist.owner,
            "description": playlist.description,
        }

@router.get("/playlists/{playlist_id}/tracks")
def get_tracks_for_playlist(playlist_id: int):
    with SessionLocal() as session:
        tracks = list_playlist_tracks(session, playlist_id)

        return [
            {
                "id": track.id,
                "title": track.title,
                "artist": track.artist,
                "album": track.album,
                "spotify_url": track.spotify_url,
                "duration_ms": track.duration_ms,
                "popularity": track.popularity,
                "image_url": track.image_url,
            }
            for track in tracks
        ]
