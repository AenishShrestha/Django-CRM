import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",  
    user="root",
    password = "Apple12!!"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE! YAY")