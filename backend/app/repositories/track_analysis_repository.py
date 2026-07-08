from sqlalchemy.orm import Session

from app.models.track_analysis import TrackAnalysis


def get_analysis_by_track_id(
    session: Session,
    track_id: int,
) -> TrackAnalysis | None:
    return (
        session.query(TrackAnalysis)
        .filter(TrackAnalysis.track_id == track_id)
        .first()
    )


def save_track_analysis(
    session: Session,
    track_id: int,
    analysis_result,
) -> TrackAnalysis:
    analysis = get_analysis_by_track_id(session, track_id)

    if analysis is None:
        analysis = TrackAnalysis(track_id=track_id)
        session.add(analysis)

    analysis.bpm = analysis_result.bpm
    analysis.musical_key = analysis_result.musical_key
    analysis.mode = analysis_result.mode
    analysis.camelot_key = analysis_result.camelot_key
    analysis.loudness = analysis_result.loudness
    analysis.energy = analysis_result.energy

    return analysis