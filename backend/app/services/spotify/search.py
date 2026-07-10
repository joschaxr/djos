from app.services.spotify.client import get_spotify_client


def search_tracks(
    artist: str | None,
    title: str,
    limit: int = 20,
) -> list[dict]:
    sp = get_spotify_client()

    if artist:
        query = f'artist:"{artist}" track:"{title}"'
    else:
        query = f'track:"{title}"'

    result = sp.search(
        q=query,
        type="track",
        limit=limit,
    )

    return result["tracks"]["items"]