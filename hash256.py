import datetime
import hashlib
import sql
def hashlogin(user):
    datatime = datetime.datetime.now()
    hase = hashlib.sha256()
    hase.update(str(user).encode())
    hase.update(str(user+user).encode())
    hase.update(str(datatime.date()).encode())
    sql.hashligondb(datatime.date(),hase.hexdigest(),user)
    return hase.hexdigest()






def gethash(hash,user):
    db=sql.hashgetdb(user)
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
    
    
    
    
def hash_admin_login(user,password):
    datatime = datetime.datetime.now()
    hase=hashlib.sha256()
    hase.update(str(user).encode())
    hase.update(str(password).encode())
    hase.update(str(user+user).encode())
    hase.update(str(datatime.date()).encode())
    return hase.hexdigest()
print(hash_admin_login("sisrsis@gmail.com","virus1122"))
