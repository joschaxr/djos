from dataclasses import dataclass


@dataclass
class AudioAnalysisResult:
    bpm: float | None = None
    musical_key: int | None = None
    mode: int | None = None
    camelot_key: str | None = None

    loudness: float | None = None
    energy: float | None = None