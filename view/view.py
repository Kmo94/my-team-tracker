class View:

    @staticmethod
    def welcome_page():
        print("****************************************")
        print("Welcome to My Teams Tracker")
        print("****************************************")
        print("(1) New user")
        print("(2) Returning user")
        print("(0) Exit")
        choice = input("Enter number: ")
        return choice

    @staticmethod
    def new_user_info():
        print("****************************************")
        print("Create a new user")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        return name, email

    @staticmethod
    def returning_user_id():
        print("****************************************")
        print("Returning user")
        user_id = input("Enter your user id: ")
        return user_id

    @staticmethod
    def show_login_success(username, user_id):
        print("****************************************")
        print("Logged in as", username, "id", user_id)

    @staticmethod
    def show_login_failed():
        print("****************************************")
        print("User not found")

    @staticmethod
    def main_menu():
        print("****************************************")
        print("My Teams Tracker")
        print("****************************************")
        print("(1) Add favourite team")
        print("(2) Add favourite player")
        print("(3) Show favourite teams")
        print("(4) Show favourite players")
        print("(5) View team results")
        print("(6) View player stats")
        print("(7) Remove favourite team")
        print("(8) Remove favourite player")
        print("(0) Logout")
        choice = input("Enter number: ")
        return choice

    @staticmethod
    def ask_team_sport():
        print("****************************************")
        print("Choose sport for the team")
        sport = input("Sport (NBA or NFL): ")
        return sport

    @staticmethod
    def choose_team_from_list(teams):
        print("****************************************")
        print("Choose a team")
        if not teams:
            print("No teams found")
            return None
        i = 1
        for name, code in teams:
            print("(" + str(i) + ")", code, "-", name)
            i += 1
        choice = input("Enter number: ")
        try:
            index = int(choice) - 1
        except ValueError:
            index = 0
        if index < 0 or index >= len(teams):
            index = 0
        return teams[index]

    @staticmethod
    def choose_team_from_favourites(teams):
        print("****************************************")
        print("Choose one of your favourite teams")
        if not teams:
            print("You have no favourite teams")
            return None
        i = 1
        for name, sport in teams:
            print("(" + str(i) + ")", name, "[", sport, "]")
            i += 1
        choice = input("Enter number: ")
        try:
            index = int(choice) - 1
        except ValueError:
            index = 0
        if index < 0 or index >= len(teams):
            index = 0
        return teams[index]

    @staticmethod
    def ask_player_sport():
        print("****************************************")
        print("Add favourite player")
        sport = input("Sport (NBA or NFL): ")
        return sport

    @staticmethod
    def ask_position_code():
        position = input("Position code (e.g. SG, PG, QB, WR): ")
        return position

    @staticmethod
    def choose_player_from_list(players):
        print("****************************************")
        print("Choose a player")
        if not players:
            print("No players found for that team/position")
            return None
        i = 1
        for name, position in players:
            print("(" + str(i) + ")", name, "-", position)
            i += 1
        choice = input("Enter number: ")
        try:
            index = int(choice) - 1
        except ValueError:
            index = 0
        if index < 0 or index >= len(players):
            index = 0
        return players[index]

    @staticmethod
    def choose_player_from_favourites(players):
        print("****************************************")
        print("Choose one of your favourite players")
        if not players:
            print("You have no favourite players")
            return None
        i = 1
        for name, sport, api_player_id in players:
            print("(" + str(i) + ")", name, "[", sport, "]")
            i += 1
        choice = input("Enter number: ")
        try:
            index = int(choice) - 1
        except ValueError:
            index = 0
        if index < 0 or index >= len(players):
            index = 0
        return players[index]

    @staticmethod
    def show_favourite_teams(teams):
        print("****************************************")
        print("Favourite teams")
        if not teams:
            print("None")
        else:
            for name, sport in teams:
                print("-", name, "[", sport, "]")

    @staticmethod
    def show_favourite_players(players):
        print("****************************************")
        print("Favourite players")
        if not players:
            print("None")
        else:
            for name, sport, api_player_id in players:
                print("-", name, "[", sport, "]")

    @staticmethod
    def show_game_result(game, team_code, league):
        home = game.get("HomeTeam")
        away = game.get("AwayTeam")
        status = game.get("Status")
        day = game.get("Day")
        if day is None:
            day = game.get("Date")
        
        if day and "T" in str(day):
            day = str(day).split("T")[0]
        
        home_score = game.get("HomeTeamScore")
        away_score = game.get("AwayTeamScore")
        
        if team_code == home:
            opponent = away
            where = "vs"
        else:
            opponent = home
            where = "at"
        
        result = "-"
        if home_score is not None and away_score is not None:
            if team_code == home:
                if home_score > away_score:
                    result = "W"
                elif home_score < away_score:
                    result = "L"
                else:
                    result = "T"
            else:
                if away_score > home_score:
                    result = "W"
                elif away_score < home_score:
                    result = "L"
                else:
                    result = "T"
        
        print(day, "|", where, opponent, "|", result, "-", status, "|", away_score, "at", home_score)

    @staticmethod
    def show_team_standing(standing, league):
        print("****************************************")
        print("Season standings")
        if standing is None:
            print("No standings found for this team")
            return
        team = standing.get("Team")
        if team is None:
            team = standing.get("Name")
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
        if wins is not None and losses is not None:
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
        print("****************************************")
        print("TODAY'S GAME STATS")
        if stats is None:
            print("No game today")
            return
        name = stats.get("Name")
        if name is None:
            name = stats.get("PlayerName")
        print("Player:", name)
        
        league = league.upper()
        if league == "NBA":
            mins = stats.get("Minutes")
            pts = stats.get("Points")
            reb = stats.get("Rebounds")
            ast = stats.get("Assists")
            stl = stats.get("Steals")
            blk = stats.get("BlockedShots")
            fg_m = stats.get("FieldGoalsMade")
            fg_a = stats.get("FieldGoalsAttempted")
            tp_m = stats.get("ThreePointersMade")
            tp_a = stats.get("ThreePointersAttempted")
            tov = stats.get("Turnovers")
            
            if mins is not None:
                print("Minutes:", mins)
            if pts is not None:
                print("Points:", pts)
            if reb is not None:
                print("Rebounds:", reb)
            if ast is not None:
                print("Assists:", ast)
            if stl is not None:
                print("Steals:", stl)
            if blk is not None:
                print("Blocks:", blk)
            if fg_m is not None and fg_a is not None:
                print("FG:", str(fg_m) + "/" + str(fg_a))
            if tp_m is not None and tp_a is not None:
                print("3PT:", str(tp_m) + "/" + str(tp_a))
            if tov is not None:
                print("Turnovers:", tov)
        else:
            pass_yards = stats.get("PassingYards")
            rush_yards = stats.get("RushingYards")
            rec_yards = stats.get("ReceivingYards")
            tds = stats.get("Touchdowns")
            if tds is None:
                tds = stats.get("TotalTouchdowns")
            if pass_yards is not None:
                print("Passing yards:", pass_yards)
            if rush_yards is not None:
                print("Rushing yards:", rush_yards)
            if rec_yards is not None:
                print("Receiving yards:", rec_yards)
            if tds is not None:
                print("Touchdowns:", tds)

    @staticmethod
    def show_player_season_stats(stats, league):
        print("****************************************")
        print("Season player stats (per game)")
        if stats is None:
            print("No season stats found for this player")
            return
        name = stats.get("Name")
        if name is None:
            name = stats.get("PlayerName")
        games = stats.get("Games")
        if games is None:
            games = stats.get("GamesPlayed")
        if games is None:
            games = 0
        print("Player:", name)
        if games:
            print("Games played:", games)
        league = league.upper()
        if league == "NBA":
            pts = stats.get("Points")
            reb = stats.get("Rebounds")
            ast = stats.get("Assists")
            stl = stats.get("Steals")
            blk = stats.get("BlockedShots")
            fg_m = stats.get("FieldGoalsMade")
            fg_a = stats.get("FieldGoalsAttempted")
            tp_m = stats.get("ThreePointersMade")
            tp_a = stats.get("ThreePointersAttempted")
            tov = stats.get("Turnovers")
            if games:
                if pts is not None:
                    print("Points:", round(pts / games, 1))
                if reb is not None:
                    print("Rebounds:", round(reb / games, 1))
                if ast is not None:
                    print("Assists:", round(ast / games, 1))
                if stl is not None:
                    print("Steals:", round(stl / games, 1))
                if blk is not None:
                    print("Blocks:", round(blk / games, 1))
                if fg_m is not None and fg_a is not None and fg_a:
                    print("FG per game:", str(round(fg_m / games,1)) + "/" + str(round(fg_a / games,1)))
                if tp_m is not None and tp_a is not None and tp_a:
                    print("3PT per game:", str(round(tp_m / games,1)) + "/" + str(round(tp_a / games,1)))
                if tov is not None:
                    print("Turnovers:", round(tov / games, 1))
        else:
            pass_yards = stats.get("PassingYards")
            rush_yards = stats.get("RushingYards")
            rec_yards = stats.get("ReceivingYards")
            tds = stats.get("Touchdowns")
            if tds is None:
                tds = stats.get("TotalTouchdowns")
            if games:
                if pass_yards is not None:
                    print("Passing yards per game:", round(pass_yards / games, 1))
                if rush_yards is not None:
                    print("Rushing yards per game:", round(rush_yards / games, 1))
                if rec_yards is not None:
                    print("Receiving yards per game:", round(rec_yards / games, 1))
                if tds is not None:
                    print("Touchdowns per game:", round(tds / games, 2))

    @staticmethod
    def show_message(message):
        print(message)