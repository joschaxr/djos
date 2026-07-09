from dataclasses import dataclass


@dataclass
class ChangePoint:
    index: int
    score: float


def detect_change_points(
    energy: list[float],
    flux: list[float],
    threshold: float = 0.15,
) -> list[ChangePoint]:

    if len(energy) != len(flux):
        raise ValueError(
            "Energy and spectral flux must have the same length."
        )

    change_points: list[ChangePoint] = []

    for i in range(1, len(energy)):

        delta_energy = abs(
            energy[i] - energy[i - 1]
        )

        delta_flux = abs(
            flux[i] - flux[i - 1]
        )

        score = (
            delta_energy * 0.5
            + delta_flux * 0.5
        )

        if score >= threshold:
            change_points.append(
                ChangePoint(
                    index=i,
                    score=round(score, 4),
                )
            )

    return change_points