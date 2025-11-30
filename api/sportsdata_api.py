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

    def _nfl_last_game_stats(self, season, player_id):
        for w in range(22, 0, -1):
            url = f"{base_url}/nfl/stats/json/PlayerGameStatsByWeek/{season}/{w}"
            data = self._safe_get(url)
            if isinstance(data, list):
                for p in data:
                    if p.get("PlayerID") == player_id:
                        return p
        return None

    def player_live_stats_today(self, league, player_id, team_code):
        league = league.upper()

        if league == "NBA":
            today = date.today().isoformat()
            url = f"{base_url}/nba/stats/json/PlayerGameStatsByDate/{today}"
            data = self._safe_get(url)
            if isinstance(data, list):
                for p in data:
                    if p.get("PlayerID") == player_id:
                        return p
            return None

        if league == "NFL":
            season = self.current_api_season("NFL")
            return self._nfl_last_game_stats(season, player_id)

        return None

    def player_season_stats(self, league, api_season, player_id, team_code):
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
            season = api_season or self.current_api_season("NFL")
            return self._nfl_last_game_stats(season, player_id)

        return None
