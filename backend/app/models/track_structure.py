from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class TrackStructure(Base):
    __tablename__ = "track_structures"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    track_id: Mapped[int] = mapped_column(
        ForeignKey("tracks.id"),
        nullable=False,
        index=True,
    )

    section_type: Mapped[str] = mapped_column(String(50), nullable=False)

    start_time: Mapped[float] = mapped_column(nullable=False)
    end_time: Mapped[float | None] = mapped_column(nullable=True)

    confidence: Mapped[float | None] = mapped_column(nullable=True)

    track = relationship("Track", back_populates="structures")