from pydantic import BaseModel


class TrackBeatResponse(BaseModel):
    beat_index: int
    time_seconds: float

    model_config = {
        "from_attributes": True,
    }