from dataclasses import dataclass, field


@dataclass
class AudioFeatures:
    sample_rate: int | None = None
    hop_length: int = 512

    energy_curve: list[float] = field(default_factory=list)
    smoothed_energy_curve: list[float] = field(default_factory=list)

    spectral_flux: list[float] = field(default_factory=list)
    smoothed_spectral_flux: list[float] = field(default_factory=list)

    chroma: list[list[float]] = field(default_factory=list)
    mfcc: list[list[float]] = field(default_factory=list)