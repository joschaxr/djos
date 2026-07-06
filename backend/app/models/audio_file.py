from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class AudioFile(Base):
    __tablename__ = "audio_files"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    path: Mapped[str] = mapped_column(
        String(1000),
        unique=True,
        index=True,
    )

    filename: Mapped[str] = mapped_column(String(500))
    extension: Mapped[str] = mapped_column(String(20))

    artist: Mapped[str | None] = mapped_column(String(255), nullable=True)
    title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    album: Mapped[str | None] = mapped_column(String(255), nullable=True)

    duration_ms: Mapped[int | None] = mapped_column(nullable=True)

    match_score: Mapped[float | None] = mapped_column(nullable=True)

    track_id: Mapped[int | None] = mapped_column(
        ForeignKey("tracks.id"),
        nullable=True,
    )

    track: Mapped["Track | None"] = relationship(
        back_populates="audio_files",
    )