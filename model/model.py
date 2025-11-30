from data.database_access import get_connection


class Model:
    def create_user(self, name, email):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cur.execute(sql, (name, email))
        conn.commit()
        user_id = cur.lastrowid
        cur.close()
        conn.close()
        return user_id

    def get_user_by_id(self, user_id):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = "SELECT id, username FROM users WHERE id = %s"
        cur.execute(sql, (user_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def add_favourite_team(self, user_id, team_name, sport):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = "INSERT INTO favorite_teams (user_id, team_name, sport) VALUES (%s, %s, %s)"
        cur.execute(sql, (user_id, team_name, sport))
        conn.commit()
        cur.close()
        conn.close()

    def add_favourite_player(self, user_id, player_name, sport):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = "INSERT INTO favorite_players (user_id, player_name, sport) VALUES (%s, %s, %s)"
        cur.execute(sql, (user_id, player_name, sport))
        conn.commit()
        cur.close()
        conn.close()

    def get_favourite_teams(self, user_id):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = "SELECT team_name, sport FROM favorite_teams WHERE user_id = %s"
        cur.execute(sql, (user_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_favourite_players(self, user_id):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = "SELECT player_name, sport FROM favorite_players WHERE user_id = %s"
        cur.execute(sql, (user_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_teams_by_sport(self, sport):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = "SELECT DISTINCT team_name, team_key FROM teams WHERE league = %s ORDER BY team_name"
        cur.execute(sql, (sport.upper(),))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_team_key_by_name(self, team_name, sport):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = "SELECT team_key FROM teams WHERE team_name = %s AND league = %s"
        cur.execute(sql, (team_name, sport.upper()))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return row[0]
        return None

    def get_players_by_team_and_position(self, sport, team_key, position):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = """
            SELECT player_name, position
            FROM players
            WHERE league = %s AND team_key = %s AND position = %s
            ORDER BY player_name
        """
        cur.execute(sql, (sport.upper(), team_key, position.upper()))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_player_id_by_name(self, sport, player_name):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = """
            SELECT api_player_id
            FROM players
            WHERE league = %s AND player_name = %s
            LIMIT 1
        """
        cur.execute(sql, (sport.upper(), player_name))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return row[0]
        return None

    def get_player_team_key(self, sport, player_name):
        conn = get_connection()
        cur = conn.cursor(buffered=True)
        sql = """
            SELECT team_key
            FROM players
            WHERE league = %s AND player_name = %s
            LIMIT 1
        """
        cur.execute(sql, (sport.upper(), player_name))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return row[0]
        return None
