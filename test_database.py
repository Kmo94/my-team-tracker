import mysql.connector
from db_config import DB_CONFIG

connection = mysql.connector.connect(host=DB_CONFIG['host'],
                                     database= DB_CONFIG['database'],
                                     user=DB_CONFIG['user'],
                                     password=DB_CONFIG['password'],
                                     port= DB_CONFIG['port']
)
print("Connected")
connection.close()