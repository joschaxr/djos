from sqlalchemy.orm import Session

from app.intelligence.analysis.audio.analyzer import analyze_audio_file
from app.repositories.audio_file_repository import get_all_audio_files
from app.repositories.track_analysis_repository import save_track_analysis
from app.repositories.track_beat_repository import save_track_beats


def run_audio_analysis(session: Session) -> int:
    analyzed = 0
    audio_files = get_all_audio_files(session)

    for audio_file in audio_files:
        if audio_file.track_id is None:
            continue

        print(f"Analysiere: {audio_file.path}", flush=True)

        result = analyze_audio_file(audio_file.path)

        save_track_analysis(
            session=session,
            track_id=audio_file.track_id,
            analysis_result=result,
        )

        save_track_beats(
            session=session,
            track_id=audio_file.track_id,
            beat_positions=result.beat_positions,
        )

        analyzed += 1

    session.commit()

    return analyzed