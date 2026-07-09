from app.services.music_library_scanner import scan_music_folder


folder_path = r"C:\Users\josch\Music\Neuer Ordner"

audio_files = scan_music_folder(folder_path)

print(f"Audiodateien gefunden: {len(audio_files)}")
print()

for file_path in audio_files[:20]:
    print(file_path)