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

    