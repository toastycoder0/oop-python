import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")

cnx = mysql.connector.connect(host, port, user, password)

cursor = cnx.cursor()

cursor.execute("SELECT CURDATE()")

row = cursor.fetchone()

print("Current date is: {0}".format(row))

cnx.close()
