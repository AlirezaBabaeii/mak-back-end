import datetime
import hashlib
def hash_admin_login(user,password):
    datatime = datetime.datetime.now()
    hase=hashlib.sha256()
    hase.update(str(user).encode())
    hase.update(str(password).encode())
    hase.update(str(user+user).encode())
    hase.update(str(datatime.date()).encode())
    return hase.hexdigest()