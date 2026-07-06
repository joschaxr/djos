from app.analysis.bpm import analyze_bpm
from app.analysis.result import AnalysisResult
from app.models.track import Track


def analyze_track(track: Track) -> AnalysisResult:
    """
    Führt alle verfügbaren Analysen eines Tracks aus.
    """

    result = AnalysisResult()

    result.bpm = analyze_bpm(track)

    return result