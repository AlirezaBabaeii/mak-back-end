import sqlite3
import datetime
import hashlib
def hashlogin(user,password):
    datatime = datetime.datetime.now()
    hase = hashlib.sha256()
    hase.update(b"test")
    hase.update(b"abolfazl")
    hase.update(str(datatime.date()).encode())
    sql = sqlite3.connect("sis.db")
    sql.execute(f"INSERT INTO hash (timehash,hashlogin,user) VALUES ('{datatime.date()}','{hase.hexdigest()}','{user}')")
    sql.commit()
    sql.close()
    hashlogin("virustest","111222")
def gethash(hash,user):
    sql=sqlite3.connect("sis.db")
    data_t=sql.cursor()
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
