from fastapi import APIRouter

from app.db.session import SessionLocal

from app.schemas.audio_file import AudioFileResponse
from app.schemas.playlist import PlaylistResponse
from app.schemas.track import TrackResponse
from app.schemas.track_analysis import TrackAnalysisResponse

from app.services.audio_file_service import (
    get_audio_file_by_id,
    list_audio_files,
)

from app.services.playlist_service import (
    get_analysis_for_track,
    get_playlist,
    get_track,
    list_playlist_tracks,
    list_playlists,
    list_tracks,
    search_tracks_by_query,
)

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Welcome to DJOS"}


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "DJOS API",
        "version": "0.1.0",
    }


# ------------------------
# Playlists
# ------------------------

@router.get("/playlists", response_model=list[PlaylistResponse])
def get_playlists():
    with SessionLocal() as session:
        return list_playlists(session)


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
        return list_playlist_tracks(session, playlist_id)


# ------------------------
# Tracks
# ------------------------

@router.get("/tracks", response_model=list[TrackResponse])
def get_tracks():
    with SessionLocal() as session:
        return list_tracks(session)


@router.get("/tracks/search", response_model=list[TrackResponse])
def search_tracks(q: str):
    with SessionLocal() as session:
        return search_tracks_by_query(session, q)


@router.get("/tracks/{track_id}", response_model=TrackResponse)
def get_track_by_id(track_id: int):
    with SessionLocal() as session:
        track = get_track(session, track_id)

        if track is None:
            return {"error": "Track not found"}

        return track


@router.get(
    "/tracks/{track_id}/analysis",
    response_model=TrackAnalysisResponse | None,
)
def get_track_analysis_by_id(track_id: int):
    with SessionLocal() as session:
        return get_analysis_for_track(session, track_id)


# ------------------------
# Audio Library
# ------------------------

@router.get(
    "/audio-files",
    response_model=list[AudioFileResponse],
)
def get_audio_files():
    with SessionLocal() as session:
        return list_audio_files(session)


@router.get(
    "/audio-files/{audio_file_id}",
    response_model=AudioFileResponse,
)
def get_audio_file(audio_file_id: int):
    with SessionLocal() as session:
        audio_file = get_audio_file_by_id(
            session,
            audio_file_id,
        )

        if audio_file is None:
            return {"error": "Audio file not found"}

        return audio_file