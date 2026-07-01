from sqlalchemy import or_, select

from app.models.playlist_track import PlaylistTrack
from app.models.track import Track


def get_tracks_by_playlist_id(session, playlist_id: int) -> list[Track]:
    return (
        session.execute(
            select(Track)
            .join(PlaylistTrack, PlaylistTrack.track_id == Track.id)
            .where(PlaylistTrack.playlist_id == playlist_id)
            .order_by(PlaylistTrack.position)
        )
        .scalars()
        .all()
    )

def get_all_tracks(session) -> list[Track]:
    return session.scalars(select(Track).order_by(Track.artist, Track.title)).all()


def get_track_by_id(session, track_id: int) -> Track | None:
    return session.get(Track, track_id)    

def search_tracks(session, query: str) -> list[Track]:
    search = f"%{query}%"

    return session.scalars(
        select(Track).where(
            or_(
                Track.title.ilike(search),
                Track.artist.ilike(search),
                Track.album.ilike(search),
            )
        )
    ).all()