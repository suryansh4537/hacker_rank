import mysql.connector

mydb=mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="banana"
)

mycursor=mydb.cursor()
mycursor.execute("")



