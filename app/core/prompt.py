
def build_prompt(user_query: str, schema: str) -> str:
    prompt = f"""
You are an expert SQL generator.

Database Schema:
{schema}

Rules:
- Use only the tables and columns provided
- Do not invent columns or tables
- Generate only SQL (no explanation)
- Use proper SQL syntax

User Query:
{user_query}

SQL:
"""
    return prompt

if __name__ == "__main__":
    user_query = "List all users who signed up in the last month"
    schema = """
    Table: users
    Columns: id, name, email, signup_date
    """
    prompt = build_prompt(user_query, schema)
    print(prompt)