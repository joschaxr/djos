from app.intelligence.analysis.audio.analyzer import analyze_audio_file

path = r"C:\Users\josch\Music\Neuer Ordner\SXTN - Hass Frau (Official Audio).mp3"

result = analyze_audio_file(path)

print(f"BPM: {result.bpm}")
print(f"Key: {result.musical_key}")
print(f"Mode: {result.mode}")
print(f"Camelot: {result.camelot_key}")
print(f"Beats erkannt: {len(result.beat_positions)}")
print(f"Erste 10 Beats: {result.beat_positions[:10]}")