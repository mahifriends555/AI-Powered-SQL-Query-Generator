
from app.db.connection import get_connection

def get_schema():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = ""

    for table in tables:
        table_name = table[0]

        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        col_names = [col[1] for col in columns]

        schema += f"{table_name}({', '.join(col_names)})\n"

    conn.close()
    return schema
