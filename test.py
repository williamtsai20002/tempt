from flask import Flask
import mysql.connector
import os


# os.system("sudo /etc/init.d/mysql start")
mydb = mysql.connector.connect(
    host = "192.168.223.144",
    user = "root",
    passwd = "root",
    database = "test_database", 
    auth_plugin = 'mysql_native_password'
)

mycursor = mydb.cursor()
table_name = "test_table"
sql = "SELECT * FROM " + table_name
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)
