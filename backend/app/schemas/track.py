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