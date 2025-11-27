class View:

    def main_menu():
        print("****************************************")
        print("          My Teams Tracker")
        print("****************************************")
        print("(1) Add favourite team")
        print("(2) Add favourite player")
        print("(3) Show favourite teams")
        print("(4) Show favourite players")
        print("(5) View team scores  (not finished)")
        print("(6) View player stats (not finished)")
        print("(0) Exit")
        option = input("Enter number to select an option: ")
        return option 

    def ask_team_info():
        print("****************************************")
        print("Add a favourite team")
        team_name = input("Team name (e.g. Lakers, Cowboys): ")
        sport = input("Sport (NBA or NFL): ")
        return team_name, sport

    def ask_player_info():
        print("****************************************")
        print("Add a favourite player")
        first_name = input("Player first name: ")
        last_name = input("Player last name: ")
        sport = input("Sport (NBA or NFL): ")
        full_name = first_name + " " + last_name
        return full_name, sport

    def show_favourite_teams(teams):
        """
        teams will later be a list of (team_name, sport)
        For now, this can be called with an empty list or simple test data.
        """
        print("****************************************")
        print("Your favourite teams:")
        if not teams:
            print("No favourite teams yet.")
        else:
            for team_name, sport in teams:
                print("- " + team_name + " [" + sport + "]")

    def show_favourite_players(players):
        print("****************************************")
        print("Your favourite players:")
        if not players:
            print("No favourite players yet.")
        else:
            for player_name, sport in players:
                print("- " + player_name + " [" + sport + "]")

    def show_message(message):
        print(message)
