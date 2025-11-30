import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path(__file__).with_name("config.cfg"))

db_info = {
    "host": config["Database"]["host"],
    "database": config["Database"]["database"],
    "user": config["Database"]["user"],
    "password": config["Database"]["password"],
    "port": int(config["Database"]["port"])
}

api_key = config["API"]["sportsdata_api_key"]