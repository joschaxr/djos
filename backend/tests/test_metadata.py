from pathlib import Path

from app.services.library.metadata_extractor import (
    extract_metadata,
)

metadata = extract_metadata(
    Path(
        r"C:\Users\josch\Music\Neuer Ordner\SXTN - Hass Frau (Official Audio).mp3"
    )
)

print(metadata)