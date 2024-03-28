"""
Entry point main file for stat-retrieval-riot-api
stat-retrieval-riot-api/api_handler.py
"""
import pprint

from api_handler import APIHandler

test = APIHandler("jack j", "EU")
pprint.pprint(test.get_match_data())

# Still under construction 😊
