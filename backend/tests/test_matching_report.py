from app.db.session import SessionLocal
from app.workflows.matching_report import print_matching_report

with SessionLocal() as session:
    print_matching_report(session, limit=50)