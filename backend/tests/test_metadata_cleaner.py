from app.intelligence.metadata.cleaner import clean_title

tests = [
    "SXTN - Hass Frau (Official Audio)",
    "KATJA KRASAVICE x IKKIMEL - BITCH (Official Video)",
    "Ikkimel - WELLNESS (prod. by Barré & gx488 _ Offizielles Musikvideo)",
]

for text in tests:
    print("Original :", text)
    print("Cleaned  :", clean_title(text))
    print()