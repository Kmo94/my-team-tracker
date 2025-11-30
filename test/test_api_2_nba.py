
import requests
from datetime import date

# Your API key
api_key = "c08475d725374e6aaaa41753ce0c63c3"
base_url = "https://api.sportsdata.io/v3"

headers = {"Ocp-Apim-Subscription-Key": api_key}

# Test today's games
today = date.today().isoformat()
url = f"{base_url}/nba/scores/json/GamesByDate/{today}"

print(f"Fetching: {url}")
print(f"Date: {today}")
print("=" * 80)

response = requests.get(url, headers=headers)
games = response.json()

print(f"Found {len(games)} games today")
print("=" * 80)

# Find Raptors game
for game in games:
    home = game.get("HomeTeam")
    away = game.get("AwayTeam")
    
    if home == "TOR" or away == "TOR":
        print("RAPTORS GAME FOUND!")
        print("=" * 80)
        print(f"Status: {game.get('Status')}")
        print(f"Teams: {away} at {home}")
        print(f"HomeTeam: {home}")
        print(f"AwayTeam: {away}")
        print(f"HomeTeamScore: {game.get('HomeTeamScore')}")
        print(f"AwayTeamScore: {game.get('AwayTeamScore')}")
        print(f"HomeScore: {game.get('HomeScore')}")
        print(f"AwayScore: {game.get('AwayScore')}")
        print(f"Day: {game.get('Day')}")
        print(f"Date: {game.get('Date')}")
        print(f"DateTime: {game.get('DateTime')}")
        print(f"Quarter: {game.get('Quarter')}")
        print("=" * 80)
        print("ALL FIELDS IN GAME OBJECT:")
        for key, value in game.items():
            print(f"  {key}: {value}")
        break