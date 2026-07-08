from app.intelligence.matching.score import (
    duration_score,
    text_score,
)


def calculate_match_score(
    spotify_artist: str | None,
    spotify_title: str | None,
    spotify_duration_ms: int | None,
    local_artist: str | None,
    local_title: str |None,
    local_duration_ms: int | None,
) -> float:
    """
    Berechnet einen gewichteten Match-Score zwischen
    einem Spotify-Track und einer lokalen Audiodatei.
    """

    scores = {
        "artist": text_score(
            spotify_artist,
            local_artist,
        ),
        "title": text_score(
            spotify_title,
            local_title,
        ),
        "duration": duration_score(
            spotify_duration_ms,
            local_duration_ms,
        ),
    }

    weights = {
        "artist": 0.40,
        "title": 0.45,
        "duration": 0.15,
    }

    total = sum(
        scores[key] * weights[key]
        for key in scores
    )

    return round(total, 4)