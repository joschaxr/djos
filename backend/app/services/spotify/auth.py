from spotipy.oauth2 import SpotifyOAuth

from app.core.config import settings


def get_auth_manager():
    return SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope="playlist-read-private playlist-read-collaborative",
    )