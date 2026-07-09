from dataclasses import asdict

from fastapi import APIRouter

from app.db.session import SessionLocal

from app.intelligence.analysis.audio.analyzer import analyze_audio_file
from app.intelligence.analysis.audio.structure.change_points import (
    detect_change_points,
)

from app.repositories.audio_file_repository import get_audio_file_by_track_id
from app.repositories.track_beat_repository import get_beats_for_track

from app.schemas.audio_file import AudioFileResponse
from app.schemas.playlist import PlaylistResponse
from app.schemas.track import TrackResponse
from app.schemas.track_beat import TrackBeatResponse

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


@router.get("/tracks/{track_id}/analysis")
def get_track_analysis_by_id(track_id: int):
    with SessionLocal() as session:
        track = get_track(session, track_id)

        if track is None:
            return {"error": "Track not found"}

        stored_analysis = get_analysis_for_track(session, track_id)

        audio_file = get_audio_file_by_track_id(
            session=session,
            track_id=track_id,
        )

        if audio_file is None:
            return {
                "track": track,
                "analysis": stored_analysis,
                "audio_file": None,
                "beats": get_beats_for_track(session, track_id),
                "bars": [],
                "phrases": [],
                "change_points": [],
                "error": "No matched local audio file found",
            }

        result = analyze_audio_file(audio_file.path)

        change_points = detect_change_points(
            result.features.smoothed_energy_curve,
            result.features.smoothed_spectral_flux,
        )

        return {
            "track": track,
            "analysis": {
                "bpm": result.bpm,
                "musical_key": result.musical_key,
                "mode": result.mode,
                "camelot_key": result.camelot_key,
            },
            "audio_file": {
                "id": audio_file.id,
                "path": audio_file.path,
                "filename": audio_file.filename,
                "match_score": audio_file.match_score,
            },
            "beats": [
                {
                    "beat_index": index,
                    "time_seconds": time_seconds,
                }
                for index, time_seconds in enumerate(result.beat_positions)
            ],
            "bars": [asdict(bar) for bar in result.bars],
            "phrases": [asdict(phrase) for phrase in result.phrases],
            "change_points": [
                asdict(change_point)
                for change_point in change_points
            ],
        }


@router.get(
    "/tracks/{track_id}/beats",
    response_model=list[TrackBeatResponse],
)
def get_track_beats(track_id: int):
    with SessionLocal() as session:
        return get_beats_for_track(session, track_id)


@router.get("/tracks/{track_id}", response_model=TrackResponse)
def get_track_by_id(track_id: int):
    with SessionLocal() as session:
        track = get_track(session, track_id)

        if track is None:
            return {"error": "Track not found"}

        return track


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