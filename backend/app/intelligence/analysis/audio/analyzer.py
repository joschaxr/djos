from pathlib import Path

import librosa

from app.intelligence.analysis.audio.features import AudioFeatures

from app.intelligence.analysis.audio.harmonic.bpm import analyze_bpm
from app.intelligence.analysis.audio.harmonic.key import analyze_key

from app.intelligence.analysis.audio.rhythm.beats import analyze_beats
from app.intelligence.analysis.audio.rhythm.bars import analyze_bars
from app.intelligence.analysis.audio.rhythm.phrases import analyze_phrases

from app.intelligence.analysis.audio.spectral.energy import (
    analyze_energy_curve,
    analyze_smoothed_energy_curve,
)

from app.intelligence.analysis.audio.spectral.flux import (
    analyze_spectral_flux,
    analyze_smoothed_spectral_flux,
)

from app.intelligence.analysis.audio.result import AudioAnalysisResult


HOP_LENGTH = 512


def analyze_audio_file(audio_path: str | Path) -> AudioAnalysisResult:
    result = AudioAnalysisResult()

    # ----------------------------------
    # Audio metadata
    # ----------------------------------

    _, sample_rate = librosa.load(
        audio_path,
        sr=None,
        mono=True,
        duration=0.01,
    )

    result.features = AudioFeatures(
        sample_rate=sample_rate,
        hop_length=HOP_LENGTH,
    )

    # ----------------------------------
    # Tempo
    # ----------------------------------

    result.bpm = analyze_bpm(audio_path)

    # ----------------------------------
    # Harmonic
    # ----------------------------------

    (
        result.musical_key,
        result.mode,
        result.camelot_key,
    ) = analyze_key(audio_path)

    # ----------------------------------
    # Rhythm
    # ----------------------------------

    result.beat_positions = analyze_beats(audio_path)

    result.bars = analyze_bars(
        result.beat_positions,
    )

    result.phrases = analyze_phrases(
        result.bars,
    )

    # ----------------------------------
    # Audio Features
    # ----------------------------------

    result.features.energy_curve = (
        analyze_energy_curve(audio_path)
    )

    result.features.smoothed_energy_curve = (
        analyze_smoothed_energy_curve(audio_path)
    )

    result.features.spectral_flux = (
        analyze_spectral_flux(audio_path)
    )

    result.features.smoothed_spectral_flux = (
        analyze_smoothed_spectral_flux(audio_path)
    )

    return result