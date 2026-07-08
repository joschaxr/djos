from sqlalchemy.orm import Session

from app.intelligence.matching.service import find_best_match
from app.repositories.audio_file_repository import get_all_audio_files
from app.repositories.track_repository import get_all_tracks


def run_matching(session: Session):
    """
    Führt das Matching zwischen Spotify-Tracks und
    lokalen AudioFiles durch.
    """

    tracks = get_all_tracks(session)
    audio_files = get_all_audio_files(session)

    matched = 0

    for track in tracks:
        audio_file, score = find_best_match(
            track,
            audio_files,
        )

        if audio_file is None:
            continue

        if score < 0.90:
            continue

        audio_file.track_id = track.id
        audio_file.match_score = score

        matched += 1

    session.commit()

    print(f"{matched} Tracks gematcht.")

    return matched