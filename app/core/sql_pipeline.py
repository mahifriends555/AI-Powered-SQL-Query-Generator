
from app.core.prompt import build_prompt
from app.core.llm import generate_response
from app.db.schema import get_schema
from app.db.executor import execute_sql
from app.safety.validator import validate_sql
import json


def run_pipeline(user_query: str):
    # Step 1: Get schema
    schema = get_schema()

    # Step 2: Build prompt
    prompt = build_prompt(user_query, schema)

    # Step 3: Generate SQL
    response = generate_response(prompt)

    # Clean markdown if exists
    response = response.strip().replace("```json", "").replace("```", "").strip()

    try:
        parsed = json.loads(response)
    except Exception as e:
        return {
            "error": "Invalid JSON from LLM",
            "raw_output": response
        }

    sql = parsed.get("sql")

    # Step 4: Validate SQL
    validate_sql(sql)

    print("\nGenerated SQL:\n", sql)

    # Step 5: Execute SQL
    result = execute_sql(sql)

    return {
    "sql": sql,
    "result": result,
    "explanation": parsed.get("explanation"),
    "breakdown": parsed.get("breakdown"),
    "tables_used": parsed.get("tables_used"),
    "tip": parsed.get("tip")
    }