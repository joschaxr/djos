from dataclasses import dataclass, field


@dataclass
class AudioFeatures:
    energy_curve: list[float] = field(default_factory=list)
    smoothed_energy_curve: list[float] = field(default_factory=list)

    spectral_flux: list[float] = field(default_factory=list)
    smoothed_spectral_flux: list[float] = field(default_factory=list)

    chroma: list[list[float]] = field(default_factory=list)
    mfcc: list[list[float]] = field(default_factory=list)