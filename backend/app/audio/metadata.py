from mutagen import File

from app.audio.cleaner import clean_text
from app.audio.index import AudioFile


def read_audio_metadata(audio_file: AudioFile) -> AudioFile:
    metadata = File(audio_file.path)

    if metadata is None:
        _apply_filename_fallback(audio_file)
        _clean_metadata(audio_file)
        return audio_file

    audio_file.duration_ms = (
        int(metadata.info.length * 1000)
        if metadata.info and metadata.info.length
        else None
    )

    tags = metadata.tags

    if tags:
        audio_file.artist = _get_tag(tags, ["artist", "TPE1", "\xa9ART"])
        audio_file.title = _get_tag(tags, ["title", "TIT2", "\xa9nam"])
        audio_file.album = _get_tag(tags, ["album", "TALB", "\xa9alb"])

    _apply_filename_fallback(audio_file)
    _clean_metadata(audio_file)

    return audio_file


def _get_tag(tags, keys: list[str]) -> str | None:
    for key in keys:
        value = tags.get(key)

        if value:
            return str(value[0]) if isinstance(value, list) else str(value)

    return None


def _apply_filename_fallback(audio_file: AudioFile) -> None:
    if audio_file.title:
        return

    filename = audio_file.filename

    if " - " in filename:
        artist, title = filename.split(" - ", 1)

        if not audio_file.artist:
            audio_file.artist = artist.strip()

        audio_file.title = title.strip()
        return

    audio_file.title = filename.strip()


def _clean_metadata(audio_file: AudioFile) -> None:
    audio_file.artist = clean_text(audio_file.artist)
    audio_file.title = clean_text(audio_file.title)
    audio_file.album = clean_text(audio_file.album)