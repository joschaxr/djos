from pathlib import Path

import librosa
import numpy as np


def analyze_energy_curve(
    audio_path: str | Path,
    frame_length: int = 2048,
    hop_length: int = 512,
) -> list[float]:
    y, _ = librosa.load(audio_path, sr=None, mono=True)

    rms = librosa.feature.rms(
        y=y,
        frame_length=frame_length,
        hop_length=hop_length,
    )[0]

    return _normalize(rms)


def analyze_smoothed_energy_curve(
    audio_path: str | Path,
    window_size: int = 128,
) -> list[float]:
    raw_curve = analyze_energy_curve(audio_path)

    if not raw_curve:
        return []

    values = np.array(raw_curve)

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