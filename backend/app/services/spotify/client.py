import spotipy

from app.services.spotify.auth import get_auth_manager


def get_spotify_client():
    return spotipy.Spotify(
        auth_manager=get_auth_manager(),
    )