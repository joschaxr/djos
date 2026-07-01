from app.schemas.common import ORMModel


class PlaylistResponse(ORMModel):
    id: int
    name: str
    spotify_id: str
    owner: str | None = None
    description: str | None = None