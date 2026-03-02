import pymysql

connect = pymysql.connect(host="localhost", user="root", password="admin", db="library")

if connect.open:
    cont = 0
else:
    print("Connection failed")
    exit(1)
