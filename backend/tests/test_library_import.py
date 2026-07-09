from app.db.session import SessionLocal
from app.services.library.library_service import import_music_folder

session = SessionLocal()

files = import_music_folder(
    session,
    r"C:\Users\josch\Music\Neuer Ordner",
)

print(f"{len(files)} Dateien importiert")
print()

for file in files:
    print(f"ID: {file.id}")
    print(f"Filename: {file.filename}")
    print(f"Artist: {file.artist}")
    print(f"Title: {file.title}")
    print(f"Album: {file.album}")
    print()