from view.view import View


class Controller:
    def __init__(self, model, api_client):
        self.model = model
        self.api_client = api_client
        self.current_user = None

    def login_flow(self):
        choice = View.welcome_page()
        if choice == "1":
            name, email = View.new_user_info()
            user_id = self.model.create_user(name, email)
            self.current_user = (user_id, name)
            View.show_login_success(name, user_id)
        elif choice == "2":
            user_id = View.returning_user_id()
            row = self.model.get_user_by_id(user_id)
            if row:
                user_id_value, username = row
                self.current_user = (user_id_value, username)
                View.show_login_success(username, user_id_value)
            else:
                View.show_login_failed()

    def main_loop(self):
        if self.current_user is None:
            return
        running = True
        while running:
            choice = View.main_menu()
            if choice == "0":
                running = False
            elif choice == "1":
                self.handle_add_team()
            elif choice == "2":
                self.handle_add_player()
            elif choice == "3":
                self.handle_show_teams()
            elif choice == "4":
                self.handle_show_players()
            elif choice == "5":
                self.handle_team_results()
            elif choice == "6":
                self.handle_player_stats()

    def handle_add_team(self):
        sport = View.ask_team_sport()
        teams = self.model.get_teams_by_sport(sport)
        chosen = View.choose_team_from_list(teams)
        if chosen is None:
            return
        team_name, team_code = chosen
        self.model.add_favourite_team(self.current_user[0], team_name, sport.upper())
        View.show_message("Favourite team added")

    def handle_add_player(self):
        sport = View.ask_player_sport()
        teams = self.model.get_teams_by_sport(sport)
        chosen_team = View.choose_team_from_list(teams)
        if chosen_team is None:
            return
        team_name, team_key = chosen_team
        position = View.ask_position_code()
        players = self.model.get_players_by_team_and_position(sport, team_key, position)
        chosen_player = View.choose_player_from_list(players)
        if chosen_player is None:
            return
        player_name, pos = chosen_player
        self.model.add_favourite_player(self.current_user[0], player_name, sport.upper())
        View.show_message("Favourite player added")

    def handle_show_teams(self):
        teams = self.model.get_favourite_teams(self.current_user[0])
        View.show_favourite_teams(teams)

    def handle_show_players(self):
        players = self.model.get_favourite_players(self.current_user[0])
        View.show_favourite_players(players)

    def handle_team_results(self):
        teams = self.model.get_favourite_teams(self.current_user[0])
        chosen = View.choose_team_from_favourites(teams)
        if chosen is None:
            return

        team_name, sport = chosen
        league = sport.upper()
        team_code = self.model.get_team_key_by_name(team_name, league)

        if team_code is None:
            View.show_message("Could not find team code for " + team_name)
            return

        status, game = self.api_client.find_team_game_today(league, team_code)
        if game is not None:
            print("****************************************")
            print("Today's Game")
            View.show_game_result(game, team_code, league)

        api_season = self.api_client.current_api_season(league)
        standing = self.api_client.team_standing(league, team_code, api_season)
        View.show_team_standing(standing, league)

    def handle_player_stats(self):
        players = self.model.get_favourite_players(self.current_user[0])
        chosen = View.choose_player_from_favourites(players)
        if chosen is None:
            return

        player_name, sport = chosen
        league = sport.upper()

        player_id = self.model.get_player_id_by_name(league, player_name)
        if player_id is None:
            View.show_message("Could not find player id for " + player_name)
            return

        team_code = self.model.get_player_team_key(league, player_name)
        if team_code is None:
            View.show_message("Could not find team code for this player")
            return

        live_stats = self.api_client.player_live_stats_today(league, player_id, team_code)
        View.show_player_live_stats(live_stats, league)

        api_season = self.api_client.current_api_season(league)
        season_stats = self.api_client.player_season_stats(league, api_season, player_id, team_code)
        View.show_player_season_stats(season_stats, league)
