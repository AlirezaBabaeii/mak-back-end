
import sqlite3
def data_create(email, password):
    data=sqlite3.connect('sis.db')
    data_t=data.cursor()
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
    data = sqlite3.connect('sis.db')
    data_t = data.cursor()
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

