from dataclasses import dataclass
from typing import Any

from app.intelligence.matching.matcher import (
    calculate_match_score,
)


@dataclass
class MatchResult:
    track: dict
    score: float


def select_best_match(
    spotify_tracks: list[dict],
    local_artist: str | None,
    local_title: str | None,
    local_duration_ms: int | None,
    minimum_score: float = 0.85,
) -> MatchResult | None:

    best_result: MatchResult | None = None

    for track in spotify_tracks:

        spotify_artist = ", ".join(
            artist["name"]
            for artist in track.get("artists", [])
        )

        score = calculate_match_score(
            spotify_artist=spotify_artist,
            spotify_title=track.get("name"),
            spotify_duration_ms=track.get("duration_ms"),
            local_artist=local_artist,
            local_title=local_title,
            local_duration_ms=local_duration_ms,
        )

        if (
            best_result is None
            or score > best_result.score
        ):
            best_result = MatchResult(
                track=track,
                score=score,
            )

    if (
        best_result is None
        or best_result.score < minimum_score
    ):
        return None

    return best_result