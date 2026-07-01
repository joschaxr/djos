from sqlalchemy import text

from app.db.session import engine


with engine.connect() as connection:
    result = connection.execute(
        text(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
        )
    )

    for row in result:
        print(row)