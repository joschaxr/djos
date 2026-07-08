from app.db.session import SessionLocal
from app.workflows.audio_analysis import run_audio_analysis

with SessionLocal() as session:
    analyzed = run_audio_analysis(session)

print(f"{analyzed} Tracks analysiert.")