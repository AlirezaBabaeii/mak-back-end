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
    mydb.commit()
def hashgetdb(user):
    data_t=mydb.cursor()
    data_t.execute(f"SELECT user, hashlogin, timehash FROM hash WHERE user = '{user}'")
    db=data_t.fetchall()
    return  db






def data_create(email, password):
    data_t=mydb.cursor()
    data_t.execute(f"SELECT email FROM user WHERE email = '{email}';")
    data_r=data_t.fetchall()
    print(data_r)
    try :
        if email in data_r[0]:
          print("ok")
    except:
        te=mydb.cursor()
        te.execute(f"INSERT INTO user(email,pass) VALUES ('{str(email)}','{str(password)}')")
        print("ok test")
        mydb.commit()









def data_login(email1,password):
    data_t = mydb.cursor()
    data_t.execute(f"SELECT email,pass FROM user WHERE email = '{email1}'")
    data_r = data_t.fetchall()
    print(data_r)
    if email1 in data_r[0]:
        print("ok")
        if password in data_r[0][1]:
            print(data_r[0][1])
            print("ok password")
            return True
        else :
            print(data_r[0][1])
            print("error")
            return False


def admin_carate_db(user,password):
    data_db=mydb.cursor()
    data_db.execute(f"SELECT user FROM admins WHERE user = '{user}';")
    data_r=data_db.fetchall()
    try :
        if user in data_r[0][0]:
          print("ok")
          return False
    except:
        data_db=mydb.cursor()
        data_db.execute(f"INSERT INTO admins(user,pass,hashs) VALUES ('{str(user)}','{str(password)}','NULL')")
        mydb.commit()
        return True