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






def data_create(email, password):
    data_t=mydb.cursor()
    a = data_t.execute(f"SELECT email, password FROM SAS WHERE email = '{email}';")
    data_r=a.fetchall()
    try :
        if email in data_r[0]:
            print("ok")
    except:
        data.execute(f"""
        INSERT INTO SAS (
                        password,
                        email
                    )
                    VALUES (
                        '{str(password)}',
                        '{str(email)}'
                    );
        """)
        print("ok test")
        data.commit()
    data.close()













def data_login(email1,password):
    data_t = mydb.cursor()
    a = data_t.execute(f"SELECT email, password FROM SAS WHERE email = '{email1}';")
    data_r = a.fetchall()
    if email1 in data_r[0]:
        print("ok")
        if password in data_r[0][1]:
            print(data_r[0][1])
            print("ok password")
            data.close()
            return True
        else :
            print(data_r[0][1])
            print("error")
            data.close()
            return False
