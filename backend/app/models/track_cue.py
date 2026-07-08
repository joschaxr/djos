from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class TrackCue(Base):
    __tablename__ = "track_cues"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    track_id: Mapped[int] = mapped_column(
        ForeignKey("tracks.id"),
        nullable=False,
        index=True,
    )

    cue_type: Mapped[str] = mapped_column(String(50), nullable=False)

    time_seconds: Mapped[float] = mapped_column(nullable=False)

    label: Mapped[str | None] = mapped_column(String(100), nullable=True)

    confidence: Mapped[float | None] = mapped_column(nullable=True)

    track = relationship("Track", back_populates="cues")