from app.intelligence.analysis.audio.result import (
    AudioBar,
    AudioPhrase,
)

BARS_PER_PHRASE = 8


def analyze_phrases(
    bars: list[AudioBar],
) -> list[AudioPhrase]:

    phrases: list[AudioPhrase] = []

    for index in range(0, len(bars), BARS_PER_PHRASE):

        phrase_index = index // BARS_PER_PHRASE

        start_time = bars[index].start_time

        next_phrase = index + BARS_PER_PHRASE

        end_time = (
            bars[next_phrase].start_time
            if next_phrase < len(bars)
            else None
        )

        phrases.append(
            AudioPhrase(
                phrase_index=phrase_index,
                start_time=start_time,
                end_time=end_time,
                bars_count=min(
                    BARS_PER_PHRASE,
                    len(bars) - index,
                ),
            )
        )

    return phrases