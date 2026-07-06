# DJOS Architecture

## Vision

DJOS ist eine Music Intelligence Platform.

Ziel ist nicht nur Musikverwaltung, sondern der Aufbau von Wissen über Musik, Sets, Übergänge, Quellen und Performances.

## Kernprinzip

DJOS speichert nicht nur Musik.

DJOS speichert Wissen über Musik.

## Hauptmodule

### Sources

Datenquellen:

- Spotify
- SoundCloud
- Apple Music
- YouTube Music
- Lokale Musikdateien
- Rekordbox
- Serato

### Library

Verwaltet lokale und externe Musikdaten.

Aufgaben:

- Tracks speichern
- Playlists speichern
- lokale Audiodateien indexieren
- Metadaten lesen
- Dateien mit Tracks matchen
- Änderungen erkennen

### Intelligence

Berechnet Wissen aus vorhandenen Daten.

Aufgaben:

- Matching
- Audioanalyse
- Lyricsanalyse
- Empfehlungen
- Übergangsbewertung

### Analysis

Musikalische Analyse einzelner Tracks.

Daten:

- BPM
- Key
- Camelot Key
- Energy
- Loudness
- Beatgrid
- Segmente
- Drops
- Cue Points

### Knowledge

Speichert Beziehungen.

Beispiele:

- Track ähnelt Track
- Track passt zu Track
- Track ist Remix von Track
- Track gehört zu Set
- Übergang funktioniert gut

### Workflows

Orchestrieren größere Prozesse.

Geplante Workflows:

- `spotify_import.py`
- `library_sync.py`
- `track_analysis.py`
- `knowledge_update.py`

## Datenmodell

### Track

Logische Song-Entität.

Enthält:

- Titel
- Artist
- Album
- Dauer
- Spotify-ID aktuell noch direkt

Langfristig sollen Source-Daten ausgelagert werden.

### AudioFile

Lokale Audiodatei.

Enthält:

- Pfad
- Dateiname
- Format
- Artist
- Titel
- Album
- Dauer
- Match Score
- Track-Verknüpfung

### TrackAnalysis

Analyseergebnis eines Tracks.

Enthält:

- BPM
- Key
- Mode
- Camelot Key
- Energy
- Danceability
- Valence
- Loudness
- Acousticness
- Instrumentalness
- Speechiness
- Liveness

### Playlist

Playlist aus Spotify oder später anderen Quellen.

### PlaylistTrack

Verknüpfung zwischen Playlist und Track.

## Architekturregel

Jede Information hat genau eine Quelle der Wahrheit.

Beispiele:

- Trackdaten liegen in `Track`.
- Audiodateien liegen in `AudioFile`.
- Analysewerte liegen in `TrackAnalysis`.
- Lyrics sollen später in `Lyrics` liegen.
- Übergänge sollen später in `Transition` liegen.

## Pipelines

### Library Sync

```text
Musikordner
↓
Dateien scannen
↓
Metadaten lesen
↓
AudioFile speichern
↓
Matching vorbereiten
↓
Analyse vorbereiten