from sqlalchemy import select

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