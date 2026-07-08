from app.db.session import SessionLocal
from app.models.track_beat import TrackBeat

track_id = 376

with SessionLocal() as session:
    count = (
        session.query(TrackBeat)
        .filter(TrackBeat.track_id == track_id)
        .count()
    )

    first_beats = (
        session.query(TrackBeat)
        .filter(TrackBeat.track_id == track_id)
        .order_by(TrackBeat.beat_index)
        .limit(10)
        .all()
    )

print(f"Beats gespeichert: {count}")

for beat in first_beats:
    print(beat.beat_index, beat.time_seconds)