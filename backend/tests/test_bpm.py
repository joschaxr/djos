from app.intelligence.analysis.audio.bpm import analyze_bpm

path = r"C:\Users\josch\Music\Neuer Ordner\SXTN - Hass Frau (Official Audio).mp3"

bpm = analyze_bpm(path)

print(f"BPM: {bpm}")