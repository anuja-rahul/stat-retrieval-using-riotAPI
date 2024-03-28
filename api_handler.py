"""
Backend connections and handler class for riot API
stat-retrieval-riot-api/api_handler.py
"""
import os
import dotenv
import requests

dotenv.load_dotenv()


class APIHandler:

    __REGIONS = {
        "AM": "americas",
        "AS": "asia",
        "EU": "europe",
        "SE": "sea"
    }

    __API_KEY = os.getenv('API_KEY')
    __API_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    __MATCH_V5_URL = "https://region.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    __MATCH_ID_URL = "https://region.api.riotgames.com/lol/match/v5/matches/"

    def __init__(self, summoner_name: str, region: str):

        if region not in APIHandler.__REGIONS.keys():
            raise Exception(f"Invalid region\n {self.get_regions()}")

        self.__summoner_name = summoner_name.split(" ")
        self.__region = APIHandler.__REGIONS[region.upper()]
        self.__puuid = self.__get_response(self.__get_authorized_url())['puuid']
        self.__match_url = None
        self.__matches = None

    # Private Methods

    def __get_authorized_url(self):
        for name in self.__summoner_name:
            self.__API_URL = self.__API_URL + name
            if self.__summoner_name[-1] != name:
                self.__API_URL += "%20"

        authorized_url = self.__API_URL + "?api_key=" + APIHandler.__API_KEY
        return authorized_url

    def __get_authorized_match_url(self):
        region_url = APIHandler.__MATCH_V5_URL.replace("region", self.__region)
        match_url = region_url + self.__puuid + "/ids?start=0&count=20"
        match_url = match_url + "&api_key=" + APIHandler.__API_KEY
        return match_url

    def __set_match_data(self):
        self.__match_url = self.__get_authorized_match_url()
        self.__matches = self.__get_response(self.__match_url)

    def _get_authorized_match_id_url(self, match_id):
        id_url = APIHandler.__MATCH_ID_URL.replace("region", self.__region)
        id_url = id_url + match_id
        return id_url

    # Public Methods

    def get_match_data(self):
        self.__set_match_data()
        all_match_urls = []
        all_match_timeline_urls = []

        for match in self.__matches:

            match_url = self._get_authorized_match_id_url(match)
            timeline_url = match_url + "/timeline"

            all_match_urls.append(match_url)
            all_match_timeline_urls.append(timeline_url)

        # TODO: Sort through the json responses of each of these urls and retrieve relevant information
        return all_match_urls, all_match_timeline_urls

    # Static Methods

    @staticmethod
    def __get_response(url):
        return requests.get(url).json()

    @staticmethod
    def get_regions():
        return APIHandler.__REGIONS
