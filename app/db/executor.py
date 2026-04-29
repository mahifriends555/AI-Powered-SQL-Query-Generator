
from app.db.connection import get_connection

def execute_sql(sql: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        result = f"Error: {str(e)}"

    conn.close()
    return result
