from app.intelligence.matching.matcher import calculate_match_score


def find_best_match(track, audio_files):
    best_audio_file = None
    best_score = 0.0

    for audio_file in audio_files:
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