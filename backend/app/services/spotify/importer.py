from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.track import Track
from app.services.spotify.client import get_spotify_client
from app.services.spotify.playlists import (
    get_current_user_playlists,
    get_playlist_tracks,
)


def import_first_playlist() -> int:
    sp = get_spotify_client()

    playlists = get_current_user_playlists(sp)

    if not playlists:
        print("Keine Playlists gefunden.")
        return 0

    playlist = playlists[0]
    print(f"Playlist: {playlist['name']}")

    items = get_playlist_tracks(sp, playlist["id"])

    imported_count = 0

    with SessionLocal() as session:
        for item in items:
            spotify_track = item.get("track") or item.get("item")

            if not spotify_track or not spotify_track.get("id"):
                continue

            existing_track = session.scalar(
                select(Track).where(Track.spotify_id == spotify_track["id"])
            )

            if existing_track:
                continue

            album = spotify_track.get("album", {})

            track = Track(
                spotify_id=spotify_track["id"],
                title=spotify_track.get("name", ""),
                artist=", ".join(
                    artist.get("name", "")
                    for artist in spotify_track.get("artists", [])
                ),
                album=album.get("name"),
                spotify_url=spotify_track.get("external_urls", {}).get("spotify"),
            )

            session.add(track)
            imported_count += 1

        session.commit()

    print(f"Neue Tracks importiert: {imported_count}")
    return imported_count