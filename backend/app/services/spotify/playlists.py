from typing import Any


def get_current_user_playlists(sp) -> list[dict[str, Any]]:
    playlists = []
    page = sp.current_user_playlists(limit=50)

    while page:
        playlists.extend(page.get("items", []))

        if page.get("next"):
            page = sp.next(page)
        else:
            break

    return playlists


def get_playlist_tracks(sp, playlist_id: str) -> list[dict[str, Any]]:
    items = []
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/items"

    params = {
        "limit": 100,
        "offset": 0,
        "additional_types": "track",
    }

    while url:
        response = sp._session.get(
            url,
            headers=sp._auth_headers(),
            params=params,
        )
        response.raise_for_status()

        page = response.json()
        items.extend(page.get("items", []))

        url = page.get("next")
        params = None

    return items