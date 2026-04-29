
# app/models.py

from pydantic import BaseModel

# What the user SENDS to your API
class QueryRequest(BaseModel):
    query: str        # the question in English
    dialect: str = "SQLite"   # optional, default is SQLite


# What your API SENDS BACK
class QueryResponse(BaseModel):
    sql: str          # the generated SQL
    explanation: str  # what the query does in simple words