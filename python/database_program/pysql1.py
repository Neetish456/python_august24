import pymysql as py

try:
    connectionobj = py.connect(host="localhost", user="root" , password="root123",database="neetish_db",port=3306 , charset="utf8")
    print("Connection was succesful!")    
except RuntimeError as err:
    print("Connection was unsuccesful")