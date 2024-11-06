import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY")
    PROJECT_ID = os.getenv("PROJECT_ID")
    MODEL_ID = os.getenv("MODEL_ID")
    URL = os.getenv("URL")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
    LLM_MODEL = os.getenv('LLM_MODEL')
