# ADR-002: Die Analysis Engine ist quellenunabhängig

## Status

Accepted

---

## Problem

Spotify, Rekordbox oder Serato liefern teilweise Analyseinformationen.

Diese unterscheiden sich jedoch in Qualität, Umfang und Verfügbarkeit.

DJOS soll unabhängig von einer einzelnen Plattform sein.

---

## Entscheidung

Die DJOS Analysis Engine verwendet ausschließlich Audio als Eingabe.

Nicht:

Spotify

Nicht:

Rekordbox

Nicht:

Serato

Sondern:

AudioAsset

↓

Analysis Engine

↓

TrackAnalysis

---

## Eingaben

- MP3
- WAV
- FLAC
- AIFF

---

## Ausgaben

- BPM
- Key
- Camelot
- Beatgrid
- Segmente
- Intro
- Outro
- Drops
- Breaks
- Vocal Sections
- Loudness
- Dynamic Range
- Energy Curve

---

## Konsequenzen

Spotify dient ausschließlich als Metadatenquelle.

Die Analyse wird vollständig von DJOS erzeugt.

---

## Vorteile

- Plattformunabhängig
- Reproduzierbar
- Erweiterbar
- Einheitliche Analysequalität