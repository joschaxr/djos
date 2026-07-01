from app.schemas.common import ORMModel


class TrackResponse(ORMModel):
    id: int
    title: str
    artist: str
    album: str | None = None
    spotify_url: str | None = None
    duration_ms: int | None = None
    popularity: int | None = None
    image_url: str | None = None

    bpm: float | None = None
    musical_key: int | None = None
    mode: int | None = None
    camelot_key: str | None = None

    energy: float | None = None
    danceability: float | None = None
    valence: float | None = None
    loudness: float | None = None
    acousticness: float | None = None
    instrumentalness: float | None = None
    speechiness: float | None = None
    liveness: float | None = None