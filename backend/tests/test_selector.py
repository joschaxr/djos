from app.intelligence.matching.selector import (
    select_best_match,
)

tracks = [
    {
        "name": "Hass Frau",
        "duration_ms": 238000,
        "artists": [
            {
                "name": "SXTN",
            }
        ],
    },
    {
        "name": "Ganz anderer Song",
        "duration_ms": 180000,
        "artists": [
            {
                "name": "Ikkimel",
            }
        ],
    },
]

result = select_best_match(
    spotify_tracks=tracks,
    local_artist="SXTN",
    local_title="Hass Frau",
    local_duration_ms=238001,
)

print(result)