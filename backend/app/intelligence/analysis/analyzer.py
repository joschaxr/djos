from pathlib import Path

from app.intelligence.analysis.audio.bars import analyze_bars
from app.intelligence.analysis.audio.beats import analyze_beats
from app.intelligence.analysis.audio.bpm import analyze_bpm
from app.intelligence.analysis.audio.energy import (
    analyze_energy_curve,
    analyze_smoothed_energy_curve,
)
from app.intelligence.analysis.audio.key import analyze_key
from app.intelligence.analysis.audio.phrases import analyze_phrases
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
    result.bars = analyze_bars(result.beat_positions)
    result.phrases = analyze_phrases(result.bars)

    result.energy_curve = analyze_energy_curve(audio_path)
    result.smoothed_energy_curve = analyze_smoothed_energy_curve(audio_path)

    return result