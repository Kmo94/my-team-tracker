import mysql.connector
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('config.cfg')

    db_info = {
        'host': config['Database']['host'],
        'database': config['Database']['database'],
        'user': config['Database']['user'],
        'password': config['Database']['password'],
        'port': int(config['Database']['port'])
    }

    try:
        connection = mysql.connector.connect(**db_info)

        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT id, username, email, is_nba_fan, is_nfl_fan FROM users WHERE id = %s"
            cursor.execute(query, (1,))
            user_data = cursor.fetchone()

            if user_data:
                print("Connection successful.\n")
                print("Retrieved user information:")
                print(f"  ID: {user_data[0]}")
                print(f"  Username: {user_data[1]}")
                print(f"  Email: {user_data[2]}")
                print(f"  NBA Fan: {bool(user_data[3])}")
                print(f"  NFL Fan: {bool(user_data[4])}")
            else:
                print("Connected to database, but no user found with id 1.")

    except mysql.connector.Error as err:
        print("Database connection error:", err)

    finally:
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except NameError:
            pass

if __name__ == "__main__":
    main()
