from dataclasses import dataclass

import numpy as np


@dataclass
class ChangePoint:
    index: int
    score: float


def detect_change_points(
    energy: list[float],
    flux: list[float],
    window_size: int = 256,
    step_size: int = 128,
    threshold_percentile: float = 92.0,
) -> list[ChangePoint]:

    if len(energy) != len(flux):
        raise ValueError(
            "Energy and spectral flux must have the same length."
        )

    if not energy:
        return []

    energy_values = np.array(energy)
    flux_values = np.array(flux)

    scores: list[ChangePoint] = []

    for index in range(
        window_size,
        len(energy_values) - window_size,
        step_size,
    ):
        energy_before = energy_values[index - window_size:index]
        energy_after = energy_values[index:index + window_size]

        flux_before = flux_values[index - window_size:index]
        flux_after = flux_values[index:index + window_size]

        energy_change = abs(
            float(np.mean(energy_after) - np.mean(energy_before))
        )

        flux_change = abs(
            float(np.mean(flux_after) - np.mean(flux_before))
        )

        score = (
            energy_change * 0.6
            + flux_change * 0.4
        )

        scores.append(
            ChangePoint(
                index=index,
                score=round(score, 4),
            )
        )

    if not scores:
        return []

    threshold = np.percentile(
        [point.score for point in scores],
        threshold_percentile,
    )

    return [
        point
        for point in scores
        if point.score >= threshold
    ]