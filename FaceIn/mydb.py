import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "12345678",
    
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE FaceInDB")

print("Database created")