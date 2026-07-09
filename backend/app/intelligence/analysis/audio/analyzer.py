from pathlib import Path

from app.intelligence.analysis.audio.harmonic.bpm import analyze_bpm
from app.intelligence.analysis.audio.harmonic.key import analyze_key

from app.intelligence.analysis.audio.rhythm.beats import analyze_beats
from app.intelligence.analysis.audio.rhythm.bars import analyze_bars
from app.intelligence.analysis.audio.rhythm.phrases import analyze_phrases

from app.intelligence.analysis.audio.spectral.energy import (
    analyze_energy_curve,
    analyze_smoothed_energy_curve,
)

from app.intelligence.analysis.audio.result import AudioAnalysisResult

def analyze_audio_file(audio_path: str | Path) -> AudioAnalysisResult:
    result = AudioAnalysisResult()

    # Tempo
    result.bpm = analyze_bpm(audio_path)

    # Harmonic analysis
    (
        result.musical_key,
        result.mode,
        result.camelot_key,
    ) = analyze_key(audio_path)

    # Rhythm
    result.beat_positions = analyze_beats(audio_path)

    # Bars
    result.bars = analyze_bars(result.beat_positions)

    # Phrases
    result.phrases = analyze_phrases(result.bars)

    return result