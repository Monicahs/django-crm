import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd ='Monika@123',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE db")

print("all done")