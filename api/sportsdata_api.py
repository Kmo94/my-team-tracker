import requests
from config.config_loader import api_key

base_url = "https://api.sportsdata.io/v3"

class SportsDataAPI:
    def get_nfl_players(self):
        url = base_url + "/nfl/scores/json/Players"
        headers = {"Ocp-Apim-Subscription-Key": api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_nba_players(self):
        url = base_url + "/nba/scores/json/Players"
        headers = {"Ocp-Apim-Subscription-Key": api_key}
        response = requests.get(url, headers=headers)
        return response.json()
