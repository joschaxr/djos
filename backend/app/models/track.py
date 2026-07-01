from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    spotify_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(String(255))
    artist: Mapped[str] = mapped_column(String(255))
    album: Mapped[str | None] = mapped_column(String(255), nullable=True)
    spotify_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    duration_ms: Mapped[int | None] = mapped_column(nullable=True)
    popularity: Mapped[int | None] = mapped_column(nullable=True)
    explicit: Mapped[bool | None] = mapped_column(nullable=True)

    preview_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    release_date: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )