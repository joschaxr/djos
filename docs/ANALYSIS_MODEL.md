# DJOS Analysis Model

## Ziel

DJOS soll Tracks nicht nur speichern, sondern musikalisch analysieren.

Die Analyse soll später Grundlage sein für:

- BPM-Filter
- Harmonic Mixing
- Energieverlauf
- Cue Points
- Übergangsvorschläge
- Remix-Empfehlungen
- KI-gestützte Setplanung

## Analyseebenen

### 1. Track-Level Analysis

Ein Wert pro Track.

- BPM
- musikalische Tonart
- Modus (Dur/Moll)
- Camelot Key
- durchschnittliche Energie
- durchschnittliche Lautheit
- Tanzbarkeit
- Stimmung / Valence
- Instrumentalität
- Sprachanteil
- Live-Anteil

### 2. Segment-Level Analysis

Mehrere Zeitabschnitte pro Track.

- Intro
- Verse
- Chorus
- Breakdown
- Drop
- Outro
- Instrumentalbereiche
- Vocalbereiche

### 3. Cue Points

Markierte DJ-Punkte.

- empfohlener Mix-In
- empfohlener Mix-Out
- Drop-Cue
- Breakdown-Cue
- Loop-Punkte

### 4. Transition Analysis

Vergleich zwischen zwei Tracks.

- BPM-Kompatibilität
- Tonart-Kompatibilität
- Energieübergang
- Vocal-Konflikt
- Intro-/Outro-Kompatibilität
- Harmonic Transition Score

## Geplante Tabellen

### track_analysis

Speichert globale Analysewerte pro Track.

### track_segments

Speichert Abschnitte innerhalb eines Tracks.

### cue_points

Speichert empfohlene oder manuelle Cue Points.

### transition_scores

Speichert berechnete Übergangsqualität zwischen zwei Tracks.

## Architekturprinzip

Analyse soll unabhängig von Spotify funktionieren.

Mögliche Quellen:

- Spotify-Metadaten
- lokale Audiodateien
- Preview-Audio
- spätere externe Audioquellen

Die Analysepipeline soll nur Audiodaten verarbeiten, unabhängig davon, woher sie stammen.