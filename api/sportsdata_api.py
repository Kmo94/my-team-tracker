import requests
from datetime import date
from config.config_loader import api_key

base_url = "https://api.sportsdata.io/v3"


class SportsDataAPI:
    def __init__(self):
        self.key = api_key

    def _get(self, url):
        headers = {"Ocp-Apim-Subscription-Key": self.key}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()

    def _safe_get(self, url):
        try:
            return self._get(url)
        except:
            return None

    def _prefix(self, league):
        return "nba" if league.upper() == "NBA" else "nfl"

    def current_api_season(self, league):
        prefix = self._prefix(league)
        url = f"{base_url}/{prefix}/scores/json/CurrentSeason"
        data = self._safe_get(url)
        if isinstance(data, dict):
            return data.get("ApiSeason") or data.get("Season")
        return data

    def standings_for_season(self, league, api_season):
        prefix = self._prefix(league)
        url = f"{base_url}/{prefix}/scores/json/Standings/{api_season}"
        return self._safe_get(url)

    def team_standing(self, league, team_code, api_season):
        standings = self.standings_for_season(league, api_season)
        if not standings:
            return None
        for s in standings:
            if s.get("Key") == team_code or s.get("Team") == team_code:
                return s
        return None

    def games_by_date(self, league, date_str):
        prefix = self._prefix(league)
        url = f"{base_url}/{prefix}/scores/json/GamesByDate/{date_str}"
        try:
            return self._get(url)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return []
            raise

    def find_team_game_today(self, league, team_code):
        today = date.today().isoformat()
        games = self.games_by_date(league, today)
        for g in games:
            if g.get("HomeTeam") == team_code or g.get("AwayTeam") == team_code:
                return g.get("Status"), g
        return None, None

    def _get_current_nfl_week(self, season):
        url = f"{base_url}/nfl/scores/json/Timeframes/current"
        data = self._safe_get(url)
        
        if isinstance(data, list) and data:
            for timeframe in data:
                if timeframe.get("ApiWeek"):
                    return timeframe.get("ApiWeek")
        
        for week in range(1, 23):
            url = f"{base_url}/nfl/scores/json/ScoresByWeek/{season}/{week}"
            scores = self._safe_get(url)
            if scores and isinstance(scores, list):
                for game in scores:
                    status = game.get("Status", "")
                    if status in ["InProgress", "Scheduled"]:
                        return week
        
        return 1

    def player_live_stats_today(self, league, player_id):
        league = league.upper()

        if league == "NBA":
            today = date.today().isoformat()
            url = f"{base_url}/nba/stats/json/PlayerGameStatsByPlayer/{today}/{player_id}"
            return self._safe_get(url)

        if league == "NFL":
            season = self.current_api_season("NFL")
            current_week = self._get_current_nfl_week(season)
            
            if current_week:
                url = f"{base_url}/nfl/stats/json/PlayerGameStatsByPlayerID/{season}/{current_week}/{player_id}"
                return self._safe_get(url)
            
            return None

        return None

    def player_season_stats(self, league, api_season, player_id):
        league = league.upper()

        if league == "NBA":
            url = f"{base_url}/nba/stats/json/PlayerSeasonStatsByPlayer/{api_season}/{player_id}"
            data = self._safe_get(url)
            
            if isinstance(data, list) and data:
                return data[0]
            if isinstance(data, dict):
                return data
            
            return None

        if league == "NFL":
            season = api_season
            if season and isinstance(season, str) and len(season) == 4 and season.isdigit():
                season = f"{season}REG"
            
            url = f"{base_url}/nfl/stats/json/PlayerSeasonStatsByPlayerID/{season}/{player_id}"
            data = self._safe_get(url)
            
            if isinstance(data, list) and data:
                return data[0]
            if isinstance(data, dict):
                return data
            
            return None

        return None