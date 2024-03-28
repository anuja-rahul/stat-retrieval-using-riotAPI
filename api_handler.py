"""
Backend connections and handler class for riot API
stat-retrieval-riot-api/api_handler.py
"""
import os
import dotenv
import requests

dotenv.load_dotenv()


class APIHandler:

    __API_KEY = os.getenv('API_KEY')
    __API_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    # fname%20lname

    def __init__(self):
        pass
