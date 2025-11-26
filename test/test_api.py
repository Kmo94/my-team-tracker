import configparser
import requests

class APIClient:
    def __init__(self, config_file="config.cfg"):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.api_key = config["API"]["key"]
        self.base_url = "https://api.sportsdata.io/v3/nfl/scores/json/ScoresByDateFinal"
        self.headers = {"Ocp-Apim-Subscription-Key": self.api_key}

    def fetch_steelers_game_by_date(self, date="2025-11-09"):
        try:
            url = f"{self.base_url}/{date}"
            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:
                games = response.json()
                Steelersgame = False
                print(f"\nSteelers game results for {date}:\n")

                for game in games:
                    if game["HomeTeam"] == "PIT" or game["AwayTeam"] == "PIT":
                        Steelersgame = True
                        print(f"Game ID: {game['GameKey']}")
                        print(f"Date: {game['Day']}")
                        print(f"Status: {game['Status']}")
                        print(f"Stadium: {game['StadiumDetails']['Name']}")
                        print(f"Home Team: {game['HomeTeam']} ({game['HomeScore']})")
                        print(f"Away Team: {game['AwayTeam']} ({game['AwayScore']})")
                        print(f"Quarter: {game.get('Quarter', 'N/A')}")
                        print(f"Season: {game['Season']}")
                        print(f"Week: {game['Week']}")

                if not Steelersgame:
                    print("No game")
            else:
                print(f"Error: Received status code {response.status_code}")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    client = APIClient()
    client.fetch_steelers_game_by_date()
