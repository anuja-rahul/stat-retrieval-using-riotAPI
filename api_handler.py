"""
Backend connections and handler class for riot API
stat-retrieval-riot-api/api_handler.py
"""
import os
import dotenv

dotenv.load_dotenv()


class APIHandler:

    __API_KEY = os.getenv('API_KEY')

    def __init__(self):
        pass
