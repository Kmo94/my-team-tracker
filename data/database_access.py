import mysql.connector
from config.config_loader import db_info

def get_connection():
    conn = mysql.connector.connect(**db_info)
    return conn
