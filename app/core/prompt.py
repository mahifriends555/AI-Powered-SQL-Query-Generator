
# app/core/prompt.py

def build_prompt(user_query: str, schema: str, dialect: str = "SQLite") -> str:
    """
    Builds the full prompt to send to the LLM.

    Args:
        user_query : what the user asked in plain English
        schema     : the database tables and columns
        dialect    : SQL dialect (SQLite, PostgreSQL, MySQL etc.)

    Returns:
        A complete prompt string ready to send to the LLM
    """

    prompt = f"""
You are an expert SQL developer and AI architect who teaches step by step for basic learners.

When generating SQL, always:
1. First explain what you understood from the user's request in simple words
2. Then show the SQL query
3. Then explain each part of the SQL line by line, like teaching a beginner
4. Point out any important things the user should know

Rules:
- Use only the tables and columns provided in the schema below
- Do not invent columns or tables that are not in the schema
- Never use SELECT *
- Always alias subqueries
- Never generate DROP, DELETE, TRUNCATE, or ALTER statements
- Use proper JOINs when data is in multiple tables
- Use foreign key relationships correctly
- If aggregation is needed, use GROUP BY
- Return ONLY valid JSON — no markdown, no explanation outside JSON

Database Schema:
{schema}

Dialect: {dialect}

User Request:
{user_query}

Return this exact JSON format:
{{
  "sql": "your SQL query here",
  "explanation": "one sentence explaining what the query does",
  "breakdown": [
    {{"line": "SELECT name, email", "meaning": "We are picking only the name and email columns"}},
    {{"line": "FROM users", "meaning": "From the users table"}}
  ],
  "tables_used": ["table1", "table2"],
  "tip": "one beginner tip related to this query"
}}
"""
    return prompt


# ============================================================
# TEST — run this file directly to test: python -m app.core.prompt
# ============================================================
if __name__ == "__main__":
    sample_query = "Show me all customers from Delhi"

    sample_schema = """
    customers(id, name, city)
    orders(id, customer_id, amount, date)
    """

    result = build_prompt(sample_query, sample_schema)
    print(result)
    