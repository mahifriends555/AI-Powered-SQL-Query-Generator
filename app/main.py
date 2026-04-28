

from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.utils.logger import get_logger

# Load environment variables
load_dotenv()

logger = get_logger(__name__)

app = FastAPI()

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "SQL AI Generator is running 🚀"}

