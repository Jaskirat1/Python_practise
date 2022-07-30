import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user ="root",
    password ="",
    database ="NewDB"
)

cursor =mydb.cursor()

cursor.execute("CREATE TABLE students (std_name VARCHAR(255), std_address VARCHAR(255))")


print(mydb)