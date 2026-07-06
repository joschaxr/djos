import re


def normalize(text: str | None) -> str:
    if not text:
        return ""

    text = text.lower()

    replacements = {
        "&": "and",
        "_": " ",
        "-": " ",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    noise = [
        "official video",
        "official audio",
        "music video",
        "visualizer",
        "lyrics",
        "extended mix",
        "radio edit",
        "original mix",
        "remix",
        "feat",
        "ft",
    ]

    for word in noise:
        text = text.replace(word, "")

    text = re.sub(r"[^a-z0-9 ]", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()