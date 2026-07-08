# ADR-001: MusicIdentity wird die zentrale Entität von DJOS

## Status

Accepted

## Datum

2026

---

# Kontext

DJOS integriert mehrere Musikquellen:

- Spotify
- SoundCloud
- Apple Music
- YouTube Music
- Lokale Audiodateien
- Rekordbox
- Serato

Alle Quellen beschreiben letztlich dieselben Musikstücke.

Ein Spotify-Track ist jedoch nicht identisch mit einer lokalen MP3 oder einem Rekordbox-Eintrag.

Deshalb darf keine dieser Quellen die zentrale Entität darstellen.

---

# Entscheidung

Die zentrale Entität von DJOS wird zukünftig:

MusicIdentity

Alle anderen Objekte referenzieren diese Identität.

---

# Modell

MusicIdentity

↓

Version

↓

Source

↓

AudioAsset

↓

Analysis

↓

Knowledge

---

# Motivation

Diese Architektur ermöglicht:

- mehrere Quellen
- mehrere Dateiformate
- mehrere Versionen
- Fingerprinting
- Lyrics
- Audioanalyse
- Knowledge Graph
- DJ Intelligence

ohne Redundanz.

---

# Konsequenzen

Track bleibt zunächst bestehen.

MusicIdentity wird parallel eingeführt.

Schrittweise werden Daten migriert.

Track wird langfristig durch MusicIdentity ersetzt.

---

# Vorteile

- Plattformunabhängig
- Zukunftssicher
- Erweiterbar
- Unterstützt beliebige Musikquellen
- Unterstützt Fingerprints
- Unterstützt Versionen
- Unterstützt KI

---

# Nachteile

Höhere Komplexität.

Zusätzliche Tabellen.

Migration notwendig.

---

# Langfristiges Ziel

DJOS soll Musik nicht als Datei oder Spotify-Track betrachten.

DJOS soll Musik als Identität verstehen.