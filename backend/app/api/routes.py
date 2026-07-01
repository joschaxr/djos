from fastapi import APIRouter
from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.playlist import Playlist
from app.models.playlist_track import PlaylistTrack
from app.models.track import Track

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
        playlists = session.scalars(select(Playlist)).all()

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
def get_playlist(playlist_id: int):
    with SessionLocal() as session:
        playlist = session.get(Playlist, playlist_id)

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
def get_playlist_tracks(playlist_id: int):
    with SessionLocal() as session:
        rows = session.execute(
            select(Track)
            .join(PlaylistTrack, PlaylistTrack.track_id == Track.id)
            .where(PlaylistTrack.playlist_id == playlist_id)
            .order_by(PlaylistTrack.position)
        ).scalars().all()

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
            for track in rows
        ]
