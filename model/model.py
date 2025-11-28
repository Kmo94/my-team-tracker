from data.database_access import get_connection

class Model:
    def create_user(self, name, email):
        conn = get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cur.execute(sql, (name, email))
        conn.commit()
        user_id = cur.lastrowid
        cur.close()
        conn.close()
        return user_id

    def get_user_by_id(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        sql = "SELECT id, username FROM users WHERE id = %s"
        cur.execute(sql, (user_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def add_favourite_team(self, user_id, team_name, sport):
        conn = get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO favorite_teams (user_id, team_name, sport) VALUES (%s, %s, %s)"
        cur.execute(sql, (user_id, team_name, sport))
        conn.commit()
        cur.close()
        conn.close()

    def add_favourite_player(self, user_id, player_name, sport):
        conn = get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO favorite_players (user_id, player_name, sport) VALUES (%s, %s, %s)"
        cur.execute(sql, (user_id, player_name, sport))
        conn.commit()
        cur.close()
        conn.close()

    def get_favourite_teams(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        sql = "SELECT team_name, sport FROM favorite_teams WHERE user_id = %s"
        cur.execute(sql, (user_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def get_favourite_players(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        sql = "SELECT player_name, sport FROM favorite_players WHERE user_id = %s"
        cur.execute(sql, (user_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
