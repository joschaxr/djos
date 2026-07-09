from app.intelligence.analysis.audio.result import AudioBar


BEATS_PER_BAR = 4


def analyze_bars(beat_positions: list[float]) -> list[AudioBar]:
    bars: list[AudioBar] = []

    for index in range(0, len(beat_positions), BEATS_PER_BAR):
        bar_index = index // BEATS_PER_BAR
        start_time = beat_positions[index]

        next_bar_index = index + BEATS_PER_BAR
        end_time = (
            beat_positions[next_bar_index]
            if next_bar_index < len(beat_positions)
            else None
        )

        bars.append(
            AudioBar(
                bar_index=bar_index,
                start_time=start_time,
                end_time=end_time,
            )
        )

    return bars