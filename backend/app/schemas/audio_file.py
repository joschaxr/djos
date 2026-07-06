from app.schemas.common import ORMModel


class AudioFileResponse(ORMModel):
    id: int
    path: str
    filename: str
    extension: str

    artist: str | None = None
    title: str | None = None
    album: str | None = None

    duration_ms: int | None = None
    match_score: float | None = None
    track_id: int | None = None