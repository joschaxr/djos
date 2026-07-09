from app.intelligence.metadata.cleaner import clean_title
from app.intelligence.metadata.parser import parse_artist_title


tests = [
    "SXTN - Hass Frau (Official Audio)",
    "KATJA KRASAVICE x IKKIMEL - BITCH (Official Video)",
    "Ikkimel - WELLNESS (prod. by Barré & gx488 _ Offizielles Musikvideo)",
    "VICKY - FKK (prod. by Robbensohn)",
]

for text in tests:
    cleaned = clean_title(text)
    parsed = parse_artist_title(cleaned)

    print("Original:", text)
    print("Cleaned :", cleaned)
    print("Artist  :", parsed.artist)
    print("Title   :", parsed.title)
    print()