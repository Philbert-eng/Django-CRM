import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'SOF',
    passwd = 'Philbe-3@'
)

# prepare a cursor object
cursorObject = database.cursor()

#create a database

cursorObject.execute("CREATE DATABASE SOF_DATABASE")

print("All Done!")

