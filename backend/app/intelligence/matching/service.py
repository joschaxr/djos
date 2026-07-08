from app.intelligence.matching.matcher import calculate_match_score


MIN_AUDIO_DURATION_MS = 60_000

IGNORED_PATH_PARTS = [
    "rekordbox\\sampler",
    "pioneerdj\\demo tracks",
]


def find_best_match(track, audio_files):
    best_audio_file = None
    best_score = 0.0

    for audio_file in audio_files:
        path = str(audio_file.path).lower()

        if any(part in path for part in IGNORED_PATH_PARTS):
            continue

        if not audio_file.title:
            continue

        if audio_file.duration_ms and audio_file.duration_ms < MIN_AUDIO_DURATION_MS:
            continue

        score = calculate_match_score(
            spotify_artist=track.artist,
            spotify_title=track.title,
            spotify_duration_ms=track.duration_ms,
            local_artist=audio_file.artist,
            local_title=audio_file.title,
            local_duration_ms=audio_file.duration_ms,
        )

        if score > best_score:
            best_score = score
            best_audio_file = audio_file

    return best_audio_file, best_score