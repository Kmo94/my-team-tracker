class View:

    def welcome_page():
        print("****************************************")
        print("Welcome to My Teams Tracker")
        print("****************************************")
        print("(1) New user")
        print("(2) Returning user")
        print("(0) Exit")
        choice = input("Enter number: ")
        return choice

    def new_user_info():
        print("****************************************")
        print("Create a new user")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        return name, email

    def returning_user_id():
        print("****************************************")
        print("Returning user")
        user_id = input("Enter your user id: ")
        return user_id

    def show_login_success(username, user_id):
        print("****************************************")
        print("Logged in as", username, "id", user_id)

    def show_login_failed():
        print("****************************************")
        print("User not found")

    def main_menu():
        print("****************************************")
        print("My Teams Tracker")
        print("****************************************")
        print("(1) Add favourite team")
        print("(2) Add favourite player")
        print("(3) Show favourite teams")
        print("(4) Show favourite players")
        print("(5) View team scores")
        print("(6) View player stats")
        print("(0) Logout")
        choice = input("Enter number: ")
        return choice

    def ask_team_info():
        print("****************************************")
        print("Add favourite team")
        team_name = input("Team name: ")
        sport = input("Sport (NBA or NFL): ")
        return team_name, sport

    def ask_player_info():
        print("****************************************")
        print("Add favourite player")
        first = input("First name: ")
        last = input("Last name: ")
        sport = input("Sport (NBA or NFL): ")
        full_name = first + " " + last
        return full_name, sport

    def show_favourite_teams(teams):
        print("****************************************")
        print("Favourite teams")
        if not teams:
            print("None")
        else:
            for name, sport in teams:
                print("-", name, "[", sport, "]")


    def show_favourite_players(players):
        print("****************************************")
        print("Favourite players")
        if not players:
            print("None")
        else:
            for name, sport in players:
                print("-", name, "[", sport, "]")

    def show_message(message):
        print(message)
