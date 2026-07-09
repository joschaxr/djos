from sqlalchemy.orm import Session

from app.models.track_beat import TrackBeat


def delete_beats_for_track(session: Session, track_id: int) -> None:
    (
        session.query(TrackBeat)
        .filter(TrackBeat.track_id == track_id)
        .delete()
    )


def save_track_beats(
    session: Session,
    track_id: int,
    beat_positions: list[float],
) -> None:
    delete_beats_for_track(session, track_id)

    for index, time_seconds in enumerate(beat_positions):
        session.add(
            TrackBeat(
                track_id=track_id,
                beat_index=index,
                time_seconds=time_seconds,
            )
        )

def get_beats_for_track(
    session: Session,
    track_id: int,
) -> list[TrackBeat]:
    return (
        session.query(TrackBeat)
        .filter(TrackBeat.track_id == track_id)
        .order_by(TrackBeat.beat_index)
        .all()
    )        