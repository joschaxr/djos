from app.intelligence.analysis.audio.analyzer import analyze_audio_file

path = r"C:\Users\josch\Music\Neuer Ordner\SXTN - Hass Frau (Official Audio).mp3"

result = analyze_audio_file(path)

print(result)