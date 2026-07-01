from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.track import Track
from app.models.playlist import Playlist
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


def create_track_from_spotify(spotify_track: dict) -> Track:
    album = spotify_track.get("album", {})

    return Track(
        spotify_id=spotify_track["id"],
        title=spotify_track.get("name", ""),
        artist=", ".join(
            artist.get("name", "")
            for artist in spotify_track.get("artists", [])
        ),
        album=album.get("name"),
        spotify_url=spotify_track.get("external_urls", {}).get("spotify"),
        duration_ms=spotify_track.get("duration_ms"),
        popularity=spotify_track.get("popularity"),
        explicit=spotify_track.get("explicit"),
        preview_url=spotify_track.get("preview_url"),
        image_url=(
            album.get("images", [{}])[0].get("url")
            if album.get("images")
            else None
        ),
        release_date=album.get("release_date"),
    )

def create_playlist_from_spotify(spotify_playlist: dict) -> Playlist:
    return Playlist(
        spotify_id=spotify_playlist["id"],
        name=spotify_playlist.get("name", ""),
        description=spotify_playlist.get("description"),
        owner=spotify_playlist.get("owner", {}).get("display_name"),
    )

def get_or_create_playlist(session, spotify_playlist: dict) -> Playlist:
    existing_playlist = session.scalar(
        select(Playlist).where(Playlist.spotify_id == spotify_playlist["id"])
    )

    if existing_playlist:
        existing_playlist.name = spotify_playlist.get("name", "")
        existing_playlist.description = spotify_playlist.get("description")
        existing_playlist.owner = spotify_playlist.get("owner", {}).get("display_name")
        return existing_playlist

    playlist = create_playlist_from_spotify(spotify_playlist)
    session.add(playlist)
    return playlist

def import_playlist(playlist: dict, sp, existing_spotify_ids: set[str]) -> int:
    print(f"Playlist: {playlist['name']}")

    items = get_playlist_tracks(sp, playlist["id"])
    imported_count = 0

    with SessionLocal() as session:
        get_or_create_playlist(session, playlist)

        for item in items:
            spotify_track = extract_spotify_track(item)

            if not spotify_track:
                continue

            spotify_id = spotify_track["id"]

            if spotify_id in existing_spotify_ids:
                existing_track = session.scalar(
                    select(Track).where(Track.spotify_id == spotify_id)
                )

                if existing_track:
                    album = spotify_track.get("album", {})

                    existing_track.duration_ms = spotify_track.get("duration_ms")
                    existing_track.popularity = spotify_track.get("popularity")
                    existing_track.explicit = spotify_track.get("explicit")
                    existing_track.preview_url = spotify_track.get("preview_url")
                    existing_track.release_date = album.get("release_date")

                    if album.get("images"):
                        existing_track.image_url = album["images"][0].get("url")

                continue

            track = create_track_from_spotify(spotify_track)

            session.add(track)
            existing_spotify_ids.add(spotify_id)
            imported_count += 1

        session.commit()

    print(f"Neue Tracks importiert: {imported_count}")
    return imported_count


def import_all_playlists() -> int:
    sp = get_spotify_client()
    playlists = get_current_user_playlists(sp)

    with SessionLocal() as session:
        existing_spotify_ids = set(session.scalars(select(Track.spotify_id)).all())

    total_imported = 0

    for playlist in playlists:
        try:
            imported = import_playlist(
                playlist,
                sp,
                existing_spotify_ids,
            )
            total_imported += imported

        except Exception as e:
            print(f"Fehler bei Playlist '{playlist['name']}': {e}")

    print(f"Gesamt neue Tracks importiert: {total_imported}")
    return total_imported