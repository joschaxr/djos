from pathlib import Path

import librosa


def analyze_beats(audio_path: str | Path) -> list[float]:
    """
    Gibt die Position jedes Beats in Sekunden zurück.
    """

    y, sr = librosa.load(audio_path, sr=None, mono=True)

    _, beat_frames = librosa.beat.beat_track(
        y=y,
        sr=sr,
    )

    beat_times = librosa.frames_to_time(
        beat_frames,
        sr=sr,
    )

    return beat_times.tolist()