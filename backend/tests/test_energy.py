from app.intelligence.analysis.audio.energy import (
    analyze_energy_curve,
    analyze_smoothed_energy_curve,
)

path = r"C:\Users\josch\Music\Neuer Ordner\SXTN - Hass Frau (Official Audio).mp3"

raw = analyze_energy_curve(path)
smoothed = analyze_smoothed_energy_curve(path)

print(f"Raw points: {len(raw)}")
print(f"Smoothed points: {len(smoothed)}")

print(f"Raw first 20: {raw[:20]}")
print(f"Smoothed first 20: {smoothed[:20]}")

print(f"Smoothed min: {min(smoothed)}")
print(f"Smoothed max: {max(smoothed)}")