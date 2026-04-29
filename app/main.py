
from urllib import request

from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.core.sql_pipeline import run_pipeline
from app.models import QueryRequest, QueryResponse

from app.utils.logger import get_logger

# Load environment variables
load_dotenv()

logger = get_logger(__name__)

app = FastAPI()

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "SQL AI Generator is running 🚀"}


@app.post("/query")
def query(request: QueryRequest):
    result = run_pipeline(request.query)
    return result


