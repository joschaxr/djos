from app.audio.index import AudioFile
from app.matching.score import similarity_score
from app.models.track import Track


def find_best_audio_match(
    track: Track,
    audio_files: list[AudioFile],
) -> AudioFile | None:
    best_match = None
    best_score = 0.0

    search_text = f"{track.artist} {track.title}"

    for audio_file in audio_files:
        score = similarity_score(search_text, audio_file.filename)

        if score > best_score:
            best_score = score
            best_match = audio_file

    if best_score < 0.75:
        return None

    return best_match