from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.playlist import Playlist
from app.models.playlist_track import PlaylistTrack
from app.models.track import Track
from app.services.spotify.client import get_spotify_client
from app.services.spotify.playlists import (
    get_current_user_playlists,
    get_playlist_tracks,
)


def extract_spotify_track(item: dict) -> dict | None:
    spotify_track = item.get("track") or item.get("item")

    if not spotify_track or not spotify_track.get("id"):
        return None

    return spotify_track


def update_track_from_spotify(track: Track, spotify_track: dict) -> None:
    album = spotify_track.get("album", {})

    track.title = spotify_track.get("name", "")
    track.artist = ", ".join(
        artist.get("name", "") for artist in spotify_track.get("artists", [])
    )
    track.album = album.get("name")
    track.spotify_url = spotify_track.get("external_urls", {}).get("spotify")
    track.duration_ms = spotify_track.get("duration_ms")
    track.popularity = spotify_track.get("popularity")
    track.explicit = spotify_track.get("explicit")
    track.preview_url = spotify_track.get("preview_url")
    track.release_date = album.get("release_date")

    if album.get("images"):
        track.image_url = album["images"][0].get("url")


def get_or_create_track(session, spotify_track: dict) -> Track:
    spotify_id = spotify_track["id"]

    track = session.scalar(select(Track).where(Track.spotify_id == spotify_id))

    if track:
        update_track_from_spotify(track, spotify_track)
        return track

    track = Track(spotify_id=spotify_id)
    update_track_from_spotify(track, spotify_track)

    session.add(track)
    session.flush()

    return track


def get_or_create_playlist(session, spotify_playlist: dict) -> Playlist:
    playlist = session.scalar(
        select(Playlist).where(Playlist.spotify_id == spotify_playlist["id"])
    )

    if playlist:
        playlist.name = spotify_playlist.get("name", "")
        playlist.description = spotify_playlist.get("description")
        playlist.owner = spotify_playlist.get("owner", {}).get("display_name")
        return playlist

    playlist = Playlist(
        spotify_id=spotify_playlist["id"],
        name=spotify_playlist.get("name", ""),
        description=spotify_playlist.get("description"),
        owner=spotify_playlist.get("owner", {}).get("display_name"),
    )

    session.add(playlist)
    session.flush()

    return playlist


def link_track_to_playlist(
    session,
    playlist: Playlist,
    track: Track,
    position: int,
) -> None:
    existing_link = session.scalar(
        select(PlaylistTrack).where(
            PlaylistTrack.playlist_id == playlist.id,
            PlaylistTrack.track_id == track.id,
            PlaylistTrack.position == position,
        )
    )

    if existing_link:
        return

    playlist_track = PlaylistTrack(
        playlist_id=playlist.id,
        track_id=track.id,
        position=position,
    )

    session.add(playlist_track)

def import_playlist(spotify_playlist: dict, sp) -> int:
    print(f"Playlist: {spotify_playlist['name']}")

    items = get_playlist_tracks(sp, spotify_playlist["id"])
    processed_count = 0

    with SessionLocal() as session:
        playlist = get_or_create_playlist(session, spotify_playlist)

        for position, item in enumerate(items):
            spotify_track = extract_spotify_track(item)

            if not spotify_track:
                continue

            track = get_or_create_track(session, spotify_track)
            link_track_to_playlist(session, playlist, track, position)

            processed_count += 1

        session.commit()

    print(f"Tracks verarbeitet: {processed_count}")
    return processed_count


def import_all_playlists() -> int:
    sp = get_spotify_client()
    playlists = get_current_user_playlists(sp)

    total_processed = 0

    for playlist in playlists:
        try:
            processed = import_playlist(playlist, sp)
            total_processed += processed

        except Exception as e:
            print(f"Fehler bei Playlist '{playlist['name']}': {e}")

    print(f"Gesamt Tracks verarbeitet: {total_processed}")
    return total_processed

def import_first_playlist_only() -> int:
    sp = get_spotify_client()
    playlists = get_current_user_playlists(sp)

    if not playlists:
        print("Keine Playlists gefunden.")
        return 0

    return import_playlist(playlists[0], sp)    