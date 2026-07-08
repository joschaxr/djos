from app.intelligence.matching.service import find_best_match
from app.repositories.audio_file_repository import get_all_audio_files
from app.repositories.track_repository import get_all_tracks


def print_matching_report(session, limit: int = 100, min_score: float = 0.30):
    tracks = get_all_tracks(session)
    audio_files = get_all_audio_files(session)

    for track in tracks[:limit]:
        audio_file, score = find_best_match(track, audio_files)

        if audio_file is None:
            continue

        if score < min_score:
            continue

        print(
            f"{score:.4f} | "
            f"{track.artist} - {track.title} "
            f"=> "
            f"{audio_file.artist} - {audio_file.title}"
        )