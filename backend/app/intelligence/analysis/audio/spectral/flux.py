from pathlib import Path

import librosa
import numpy as np


def analyze_spectral_flux(
    audio_path: str | Path,
    hop_length: int = 512,
) -> list[float]:
    y, sr = librosa.load(audio_path, sr=None, mono=True)

    onset_strength = librosa.onset.onset_strength(
        y=y,
        sr=sr,
        hop_length=hop_length,
    )

    return _normalize(onset_strength)


def analyze_smoothed_spectral_flux(
    audio_path: str | Path,
    window_size: int = 128,
) -> list[float]:
    flux = analyze_spectral_flux(audio_path)

    if not flux:
        return []

    values = np.array(flux)
    window = np.ones(window_size) / window_size

    smoothed = np.convolve(
        values,
        window,
        mode="same",
    )

    return [round(float(value), 4) for value in smoothed]


def _normalize(values) -> list[float]:
    if len(values) == 0:
        return []

    max_value = float(np.max(values))

    if max_value <= 0:
        return [0.0 for _ in values]

    normalized = values / max_value

    return [round(float(value), 4) for value in normalized]