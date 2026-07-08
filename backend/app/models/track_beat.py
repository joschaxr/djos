from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class TrackBeat(Base):
    __tablename__ = "track_beats"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    track_id: Mapped[int] = mapped_column(
        ForeignKey("tracks.id"),
        nullable=False,
        index=True,
    )

    beat_index: Mapped[int] = mapped_column(Integer, nullable=False)

    time_seconds: Mapped[float] = mapped_column(nullable=False)

    track = relationship("Track", back_populates="beats")