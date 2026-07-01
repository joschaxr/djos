from pathlib import Path

from mutagen import File

from app.audio.index import AudioFile


def read_audio_metadata(audio_file: AudioFile) -> AudioFile:
    metadata = File(audio_file.path)

    if metadata is None:
        return audio_file

    audio_file.duration_ms = (
        int(metadata.info.length * 1000)
        if metadata.info and metadata.info.length
        else None
    )

    tags = metadata.tags

    if not tags:
        return audio_file

    audio_file.artist = _get_tag(tags, ["artist", "TPE1", "\xa9ART"])
    audio_file.title = _get_tag(tags, ["title", "TIT2", "\xa9nam"])
    audio_file.album = _get_tag(tags, ["album", "TALB", "\xa9alb"])

    return audio_file


def _get_tag(tags, keys: list[str]) -> str | None:
    for key in keys:
        value = tags.get(key)

        if value:
            return str(value[0]) if isinstance(value, list) else str(value)

    return None