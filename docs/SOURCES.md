# DJOS Music Sources

## Ziel

DJOS soll Musikdaten aus mehreren Quellen aufnehmen und in ein einheitliches internes Modell überführen.

Quellen:

- Spotify
- SoundCloud
- Apple Music
- YouTube Music
- Lokale Musikdateien
- Rekordbox
- Serato

Alle Quellen liefern am Ende Daten für:

- Tracks
- Playlists
- Audioquellen
- Metadaten
- spätere Analyse

## Architektur

```text
Spotify
SoundCloud
Apple Music
YouTube Music
Lokale Musik
Rekordbox
Serato
        ↓
     DJOS
        ↓
Music Intelligence Engine
        ↓
DJ-Unterstützung