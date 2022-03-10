from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1382",
  database="webali"
)
def  hashligondb(datetimedb,hashtodb,user):
    sql = mydb.cursor()
    sql.execute(f"INSERT INTO hashdb (hashtime,hashlogin,user) VALUES ('{datetimedb}','{hashtodb}','{user}')")
def hashgetdb(user):
    data_t=mydb.cursor()
    data_t.execute(f"SELECT user, hashlogin, timehash FROM hash WHERE user = '{user}'")
    db=data_t.fetchall()
    return  db
