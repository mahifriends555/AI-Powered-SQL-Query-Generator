
from app.core.prompt import build_prompt
from app.core.llm import generate_response
from app.db.schema import get_schema
from app.db.executor import execute_sql
from app.safety.validator import validate_sql


def run_pipeline(user_query: str):
    # Step 1: Get schema
    schema = get_schema()

    # Step 2: Build prompt
    prompt = build_prompt(user_query, schema)

    # Step 3: Generate SQL
    sql = generate_response(prompt)
    print("\nGenerated SQL:\n", sql)

    # Step 4: Validate SQL
    validate_sql(sql)

    # Step 5: Execute SQL
    result = execute_sql(sql)

    return result