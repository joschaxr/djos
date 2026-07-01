from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Playlist(Base):
    __tablename__ = "playlists"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    spotify_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(255))

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    owner: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )