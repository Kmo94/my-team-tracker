import requests
import mysql.connector
import configparser


config = configparser.ConfigParser()
config.read("config.cfg")


api_key = config["API"]["key"]

db_info = {
    'host': config['Database']['host'],
    'database': config['Database']['database'],
    'user': config['Database']['user'],
    'password': config['Database']['password'],
    'port': int(config['Database']['port'])
}



def get_connection():
    return mysql.connector.connect(**db_info)


def fetch_teams(league):
    base = "https://api.sportsdata.io/v3"
    path = "nfl" if league == "NFL" else "nba"
    url = f"{base}/{path}/scores/json/Teams"

    response = requests.get(url, params={"key": api_key})
    response.raise_for_status()
    return response.json()


def save_teams(league):
    teams = fetch_teams(league)
    print(f"Fetched {len(teams)} {league} teams")

    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO teams (team_name, api_team_id, team_key, league)
        VALUES (%s, %s, %s, %s)
    """

    for t in teams:
        name = t.get("FullName") or t.get("Name")
        team_id = t.get("TeamID")
        team_key = t.get("Key")

        if not team_id or not name:
            continue

        cur.execute(sql, (name, team_id, team_key, league))

    conn.commit()
    cur.close()
    conn.close()

    print(f"Inserted {league} teams\n")


def fetch_players(league):
    base = "https://api.sportsdata.io/v3"
    path = "nfl" if league == "NFL" else "nba"
    url = f"{base}/{path}/scores/json/Players"

    response = requests.get(url, params={"key": api_key})
    response.raise_for_status()
    return response.json()


def save_players(league):
    players = fetch_players(league)
    print(f"Fetched {len(players)} {league} players")

    conn = get_connection()
    cur = conn.cursor()

    sql = """
        INSERT INTO players (player_name, api_player_id, team_key, position, league)
        VALUES (%s, %s, %s, %s, %s)
    """

    for p in players:
        player_id = p.get("PlayerID")

        name = p.get("Name")
        if not name:
            first = p.get("FirstName") or ""
            last = p.get("LastName") or ""
            name = f"{first} {last}".strip()

        team_key = p.get("Team")
        position = p.get("Position")

        if not player_id or not name:
            continue

        cur.execute(sql, (name, player_id, team_key, position, league))

    conn.commit()
    cur.close()
    conn.close()

    print(f"Inserted {league} players\n")



if __name__ == "__main__":
    # NFL
    save_teams("NFL")
    save_players("NFL")

    # NBA
    save_teams("NBA")
    save_players("NBA")

    print("DONE!")
