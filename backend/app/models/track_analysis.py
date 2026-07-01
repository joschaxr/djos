from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class TrackAnalysis(Base):
    __tablename__ = "track_analysis"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    track_id: Mapped[int] = mapped_column(
        ForeignKey("tracks.id"),
        unique=True,
        nullable=False,
    )

    bpm: Mapped[float | None] = mapped_column(nullable=True)
    musical_key: Mapped[int | None] = mapped_column(nullable=True)
    mode: Mapped[int | None] = mapped_column(nullable=True)

    camelot_key: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )

    energy: Mapped[float | None] = mapped_column(nullable=True)
    danceability: Mapped[float | None] = mapped_column(nullable=True)
    valence: Mapped[float | None] = mapped_column(nullable=True)
    loudness: Mapped[float | None] = mapped_column(nullable=True)

    acousticness: Mapped[float | None] = mapped_column(nullable=True)
    instrumentalness: Mapped[float | None] = mapped_column(nullable=True)
    speechiness: Mapped[float | None] = mapped_column(nullable=True)
    liveness: Mapped[float | None] = mapped_column(nullable=True)

    track: Mapped["Track"] = relationship(
        back_populates="analysis",
    )