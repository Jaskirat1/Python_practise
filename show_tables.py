from sqlite3 import Cursor, dbapi2
import mysql.connector


mydb = mysql.connector.connect(

    host ="localhost",
    user = "root",
    password ="",
    database ="NewDB"

)

cursor = mydb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)