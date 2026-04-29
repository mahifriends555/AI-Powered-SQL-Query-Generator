
def validate_sql(sql: str):
    sql_upper = sql.upper().strip()

    forbidden = ["DROP", "DELETE", "TRUNCATE", "ALTER"]

    for word in forbidden:
        if word in sql_upper:
            raise Exception(f"Unsafe SQL detected: {word}")

    # 🔥 Only allow SELECT
    if not sql_upper.startswith("SELECT"):
        raise Exception("Only SELECT queries are allowed")

    return True


if __name__ == "__main__":

    # Test 1: Safe
    sql = "SELECT * FROM users;"
    print(validate_sql(sql))

    # Test 2: Dangerous
    sql = "DROP TABLE users;"
    try:
        validate_sql(sql)
    except Exception as e:
        print(e)

    sql = "UPDATE users SET password = 'hack';"
    try:
        validate_sql(sql)
    except Exception as e:
        print(e)