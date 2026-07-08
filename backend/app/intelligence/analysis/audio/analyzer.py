from pathlib import Path

from app.intelligence.analysis.audio.bpm import analyze_bpm
from app.intelligence.analysis.audio.result import AudioAnalysisResult


def analyze_audio_file(audio_path: str | Path) -> AudioAnalysisResult:
    result = AudioAnalysisResult()

    result.bpm = analyze_bpm(audio_path)

    return result