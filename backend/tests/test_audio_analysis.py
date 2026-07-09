from app.intelligence.analysis.audio.analyzer import analyze_audio_file

path = (
    r"C:\Users\josch\Music\Neuer Ordner"
    r"\SXTN - Hass Frau (Official Audio).mp3"
)

result = analyze_audio_file(path)

print("=" * 60)
print("DJOS AUDIO ANALYSIS")
print("=" * 60)

print(f"BPM: {result.bpm}")
print(f"Key: {result.musical_key}")
print(f"Mode: {result.mode}")
print(f"Camelot: {result.camelot_key}")

print()

print(f"Beats erkannt: {len(result.beat_positions)}")
print(f"Bars erkannt: {len(result.bars)}")
print(f"Phrases erkannt: {len(result.phrases)}")

print()

print("Erste 10 Beats")
print(result.beat_positions[:10])

print()

print("Erste 5 Bars")
print(result.bars[:5])

print()

print("Erste 3 Phrases")
print(result.phrases[:3])

print()

print("Energy Curve")
print(f"Points: {len(result.features.energy_curve)}")
print(f"First 20: {result.features.energy_curve[:20]}")

print()

print("Smoothed Energy Curve")
print(f"Points: {len(result.features.smoothed_energy_curve)}")
print(
    f"First 20: "
    f"{result.features.smoothed_energy_curve[:20]}"
)

print()

print("Spectral Flux")
print(f"Points: {len(result.features.spectral_flux)}")
print(f"First 20: {result.features.spectral_flux[:20]}")

print()

print("Smoothed Spectral Flux")
print(f"Points: {len(result.features.smoothed_spectral_flux)}")
print(
    f"First 20: "
    f"{result.features.smoothed_spectral_flux[:20]}"
)

print("=" * 60)