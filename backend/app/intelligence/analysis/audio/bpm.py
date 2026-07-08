from pathlib import Path

import librosa
import numpy as np


def analyze_bpm(audio_path: str | Path) -> float | None:
    y, sr = librosa.load(audio_path, sr=None, mono=True)

    tempo, _ = librosa.beat.beat_track(
        y=y,
        sr=sr,
    )

    tempo_value = float(np.asarray(tempo).squeeze())

    if tempo_value <= 0:
        return None

    return round(tempo_value, 2)