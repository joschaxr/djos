from pathlib import Path

import librosa
import numpy as np


KEY_NAMES = [
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
    "A",
    "A#",
    "B",
]

MAJOR_PROFILE = np.array([
    6.35, 2.23, 3.48, 2.33, 4.38, 4.09,
    2.52, 5.19, 2.39, 3.66, 2.29, 2.88,
])

MINOR_PROFILE = np.array([
    6.33, 2.68, 3.52, 5.38, 2.60, 3.53,
    2.54, 4.75, 3.98, 2.69, 3.34, 3.17,
])

CAMELOT_MAJOR = {
    0: "8B",
    1: "3B",
    2: "10B",
    3: "5B",
    4: "12B",
    5: "7B",
    6: "2B",
    7: "9B",
    8: "4B",
    9: "11B",
    10: "6B",
    11: "1B",
}

CAMELOT_MINOR = {
    0: "5A",
    1: "12A",
    2: "7A",
    3: "2A",
    4: "9A",
    5: "4A",
    6: "11A",
    7: "6A",
    8: "1A",
    9: "8A",
    10: "3A",
    11: "10A",
}


def analyze_key(audio_path: str | Path) -> tuple[int | None, int | None, str | None]:
    y, sr = librosa.load(audio_path, sr=None, mono=True)

    chroma = librosa.feature.chroma_cqt(
        y=y,
        sr=sr,
    )

    chroma_mean = chroma.mean(axis=1)

    best_key = None
    best_mode = None
    best_score = -1.0

    for key in range(12):
        major_score = np.corrcoef(
            chroma_mean,
            np.roll(MAJOR_PROFILE, key),
        )[0, 1]

        minor_score = np.corrcoef(
            chroma_mean,
            np.roll(MINOR_PROFILE, key),
        )[0, 1]

        if major_score > best_score:
            best_key = key
            best_mode = 1
            best_score = major_score

        if minor_score > best_score:
            best_key = key
            best_mode = 0
            best_score = minor_score

    if best_key is None or best_mode is None:
        return None, None, None

    camelot = (
        CAMELOT_MAJOR[best_key]
        if best_mode == 1
        else CAMELOT_MINOR[best_key]
    )

    return best_key, best_mode, camelot