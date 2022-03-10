
import datetime
import hashlib
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1382",
 database="webali"
)
def hashlogin(user):
    datatime = datetime.datetime.now()
    hase = hashlib.sha256()
    hase.update(b"test")
    hase.update(b"abolfazl")
    hase.update(str(datatime.date()).encode())
    hashligondb(datatime.date(),hase.hexdigest(),user)
    return hase.hexdigest()
def gethash(hash,user):
    data_t=mydb.cursor()
    data_t.execute(f"SELECT user, hashlogin, timehash FROM hash WHERE user = '{user}'")
    da=data_t.fetchall()
    if da[0][1] in hash:
        print ("ok hash")
        data=datetime.datetime.now()
        if str(data.date()) in da[0][2]:
            print("ok time")
            return True
        else:
            print("error time")
            return False
    else :
        print("error hash")
        return False
