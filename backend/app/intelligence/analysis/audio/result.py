from dataclasses import dataclass, field

from app.intelligence.analysis.audio.features import AudioFeatures


@dataclass
class AudioBar:
    bar_index: int
    start_time: float
    end_time: float | None = None


@dataclass
class AudioPhrase:
    phrase_index: int
    start_time: float
    end_time: float | None = None
    bars_count: int | None = None


@dataclass
class AudioSection:
    section_type: str
    start_time: float
    end_time: float | None = None
    confidence: float | None = None


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
    bars: list[AudioBar] = field(default_factory=list)
    phrases: list[AudioPhrase] = field(default_factory=list)

    # Audio feature layer
    features: AudioFeatures = field(default_factory=AudioFeatures)

    # Structure
    sections: list[AudioSection] = field(default_factory=list)
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