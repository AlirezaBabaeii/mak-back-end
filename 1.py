import sqlite3
uaser="virussisrsis@gmail.com"
passs="122"








def data_login(email, password):
    data=sqlite3.connect('sis.db')
    data_t=data.cursor()
    a = data_t.execute(f"SELECT email, password FROM SAS WHERE email = '{email}';")
    data_r=a.fetchall()
    try :
        if uaser in data_r[0]:
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


data_login("virussisfsis@gmail.com","112222")
