from app.schemas.common import ORMModel


class TrackAnalysisResponse(ORMModel):
    id: int
    track_id: int

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