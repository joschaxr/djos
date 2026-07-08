from pathlib import Path

from app.intelligence.analysis.audio.beats import analyze_beats
from app.intelligence.analysis.audio.bpm import analyze_bpm
from app.intelligence.analysis.audio.key import analyze_key
from app.intelligence.analysis.audio.result import AudioAnalysisResult


def analyze_audio_file(audio_path: str | Path) -> AudioAnalysisResult:
    result = AudioAnalysisResult()

    result.bpm = analyze_bpm(audio_path)

    (
        result.musical_key,
        result.mode,
        result.camelot_key,
    ) = analyze_key(audio_path)

    result.beat_positions = analyze_beats(audio_path)

    return result