from dataclasses import dataclass, field


@dataclass
class AudioAnalysisResult:
    # Tempo
    bpm: float | None = None
    bpm_confidence: float | None = None

    # Harmonic
    musical_key: int | None = None
    mode: int | None = None
    camelot_key: str | None = None
    key_confidence: float | None = None

    # Loudness
    loudness: float | None = None
    peak_db: float | None = None
    rms_db: float | None = None

    # Rhythm
    beat_positions: list[float] = field(default_factory=list)

    # Structure
    intro_start: float | None = None
    intro_end: float | None = None
    outro_start: float | None = None
    drop_positions: list[float] = field(default_factory=list)

    # DJ
    suggested_mix_in: float | None = None
    suggested_mix_out: float | None = None

    # High-level features
    energy: float | None = None
    danceability: float | None = None