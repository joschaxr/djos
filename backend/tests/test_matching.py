from app.db.session import SessionLocal
from app.workflows.matching import run_matching

with SessionLocal() as session:
    run_matching(session)