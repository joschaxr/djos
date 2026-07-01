import re


def normalize(text: str) -> str:
    """
    Vereinheitlicht Tracktitel und Dateinamen
    für Vergleiche.
    """

    text = text.lower()

    text = re.sub(r"\.[a-z0-9]{2,5}$", "", text)

    text = re.sub(r"[\(\)\[\]\-_]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()