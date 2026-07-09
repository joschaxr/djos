from app.intelligence.analysis.audio.analyzer import analyze_audio_file
from app.intelligence.analysis.audio.structure.change_points import (
    detect_change_points,
)

path = (
    r"C:\Users\josch\Music\Neuer Ordner"
    r"\SXTN - Hass Frau (Official Audio).mp3"
)

result = analyze_audio_file(path)

points = detect_change_points(
    result.features.smoothed_energy_curve,
    result.features.smoothed_spectral_flux,
)

print(f"Change Points: {len(points)}")
print()

for point in points[:20]:
    print(point)