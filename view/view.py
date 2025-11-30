class View:

    @staticmethod
    def print_line(title=None):
        print("****************************************")
        if title:
            print(title)

    @staticmethod
    def print_numbered_list(items):
        for i, item in enumerate(items, start=1):
            print(f"({i}) {item}")

    @staticmethod
    def get_index_choice(items):
        choice = input("Enter number: ")
        try:
            idx = int(choice) - 1
        except:
            idx = 0
        if idx < 0 or idx >= len(items):
            idx = 0
        return items[idx]

    @staticmethod
    def welcome_page():
        View.print_line("Welcome to My Team Tracker")
        print("(1) New user")
        print("(2) Returning user")
        return input("Enter number: ")

    @staticmethod
    def new_user_info():
        View.print_line("Create new user")
        name = input("Enter username: ")
        email = input("Enter email: ")
        return name, email

    @staticmethod
    def returning_user_id():
        View.print_line("Returning user")
        return input("Enter your user ID: ")

    @staticmethod
    def show_login_success(name, user_id):
        View.print_line()
        print(f"Welcome, {name}! (User ID: {user_id})")

    @staticmethod
    def show_login_failed():
        View.print_line()
        print("Login failed. User not found.")

    @staticmethod
    def main_menu():
        View.print_line()
        print("(1) Add favourite team")
        print("(2) Add favourite player")
        print("(3) View favourite teams")
        print("(4) View favourite players")
        print("(5) View team results")
        print("(6) View player stats")
        print("(0) Logout")
        return input("Enter number: ")

    @staticmethod
    def ask_team_sport():
        View.print_line("Choose sport for the team")
        return input("Sport (NBA, NFL, etc.): ")

    @staticmethod
    def choose_team_from_list(teams):
        View.print_line("Choose a team")
        if not teams:
            print("No teams found.")
            return None

        display = [f"{code} - {name}" for name, code in teams]
        View.print_numbered_list(display)
        return View.get_index_choice(teams)

    @staticmethod
    def choose_team_from_favourites(teams):
        View.print_line("Choose a favourite team")
        if not teams:
            print("You have no favourite teams.")
            return None

        display = [f"{name} [{sport}]" for name, sport in teams]
        View.print_numbered_list(display)
        return View.get_index_choice(teams)

    @staticmethod
    def show_favourite_teams(teams):
        View.print_line("Favourite teams")
        if not teams:
            print("None")
            return
        for name, sport in teams:
            print(f"- {name} [{sport}]")

    @staticmethod
    def ask_player_sport():
        View.print_line("Add favourite player")
        return input("Sport (NBA, NFL, etc.): ")

    @staticmethod
    def ask_position_code():
        return input("Position code (e.g. SG, PG, QB, WR): ")

    @staticmethod
    def choose_player_from_list(players):
        View.print_line("Choose a player")
        if not players:
            print("No players found for that team/position.")
            return None

        display = [f"{name} - {pos}" for name, pos in players]
        View.print_numbered_list(display)
        return View.get_index_choice(players)

    @staticmethod
    def choose_player_from_favourites(players):
        View.print_line("Choose a favourite player")
        if not players:
            print("You have no favourite players.")
            return None

        display = [f"{name} [{sport}]" for name, sport in players]
        View.print_numbered_list(display)
        return View.get_index_choice(players)

    @staticmethod
    def show_favourite_players(players):
        View.print_line("Favourite players")
        if not players:
            print("None")
            return
        for name, sport in players:
            print(f"- {name} [{sport}]")


    @staticmethod
    def show_game_result(game, team_code, league):
        home = game.get("HomeTeam")
        away = game.get("AwayTeam")
        status = game.get("Status")
        day = game.get("Day") or game.get("Date")

        if day and "T" in str(day):
            day = str(day).split("T")[0]

        if league.upper() == "NBA":
            home_score = game.get("HomeTeamScore")
            away_score = game.get("AwayTeamScore")
        else:
            home_score = game.get("HomeTeamScore2") or game.get("HomeScore")
            away_score = game.get("AwayTeamScore2") or game.get("AwayScore")

        if team_code == home:
            opponent = away
            where = "vs"
            team_score = home_score
            opp_score = away_score
        else:
            opponent = home
            where = "at"
            team_score = away_score
            opp_score = home_score

        # Win/Loss/Tie
        result = "-"
        if team_score is not None and opp_score is not None:
            if team_score > opp_score:
                result = "W"
            elif team_score < opp_score:
                result = "L"
            else:
                result = "T"

        print(f"{day} | {where} {opponent} | {result} - {status} | {away_score} at {home_score}")

    @staticmethod
    def show_team_standing(standing, league):
        View.print_line("Season standings")
        if standing is None:
            print("No standings found for this team.")
            return

        team = standing.get("Team") or standing.get("Name")
        conf = standing.get("Conference")
        div = standing.get("Division")
        wins = standing.get("Wins")
        losses = standing.get("Losses")
        ties = standing.get("Ties")
        pct = standing.get("Percentage")
        pf = standing.get("PointsFor")
        pa = standing.get("PointsAgainst")
        net = standing.get("NetPoints")

        print("Team:", team)
        if conf or div:
            print("Conference/Division:", conf or "", "/", div or "")
        if ties:
            print("Record:", wins, "-", losses, "-", ties)
        else:
            print("Record:", wins, "-", losses)
        if pct is not None:
            print("Win %:", round(pct, 3))
        if pf is not None and pa is not None:
            print("Points for:", pf, "| Points against:", pa, "| Net:", net or 0)

    @staticmethod
    def show_player_live_stats(stats, league):
        View.print_line("Live / today player stats")
        if not stats:
            print("No live stats for this player today.")
            return

        name = stats.get("Name") or stats.get("PlayerName")
        print("Player:", name)

        league = league.upper()
        if league == "NBA":
            print("Minutes:", stats.get("Minutes"))
            print("Points:", stats.get("Points"))
            print("Rebounds:", stats.get("Rebounds"))
            print("Assists:", stats.get("Assists"))
            print("Steals:", stats.get("Steals"))
            print("Blocks:", stats.get("BlockedShots"))
        else:
            print("Passing yards:", stats.get("PassingYards"))
            print("Rushing yards:", stats.get("RushingYards"))
            print("Receiving yards:", stats.get("ReceivingYards"))
            print("Touchdowns:", stats.get("Touchdowns") or stats.get("TotalTouchdowns"))

    @staticmethod
    def show_player_season_stats(stats, league):
        View.print_line("Season player stats (per game)")
        if not stats:
            print("No season stats found for this player.")
            return

        name = stats.get("Name") or stats.get("PlayerName")
        games = stats.get("Games") or stats.get("GamesPlayed") or 0

        print("Player:", name)
        print("Games played:", games)

        league = league.upper()
        if league == "NBA":
            if games:
                print("Points:", round(stats.get("Points") / games, 1))
                print("Rebounds:", round(stats.get("Rebounds") / games, 1))
                print("Assists:", round(stats.get("Assists") / games, 1))
        else:
            if games:
                print("Passing yards per game:", round(stats.get("PassingYards") / games, 1))
                print("Rushing yards per game:", round(stats.get("RushingYards") / games, 1))
                print("Receiving yards per game:", round(stats.get("ReceivingYards") / games, 1))


    @staticmethod
    def show_message(message):
        print(message)
