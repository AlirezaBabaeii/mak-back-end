<<<<<<< HEAD
from flask import Flask ,request ,make_response
import hash256
import sql
=======
from flask import Flask , render_template ,request
import create

>>>>>>> 2b9c063bab1e06f6065e912903be6e36770cdf26
app = Flask(__name__)

@app.route('/')
def hello_world():

<<<<<<< HEAD
    return '{"Response":200,"URL":{"login":"/login","create":"/create"}}'
=======

    return render_template("index.html")
>>>>>>> 2b9c063bab1e06f6065e912903be6e36770cdf26
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
       Password = request.form['password']
       User= request.form['email']
       print(User)
       print(Password)
<<<<<<< HEAD
       testpass =  sql.data_login(User,Password)
       if testpass==True:
           out=make_response('{"Response":"ok","mode":"login"}')
           out.set_cookie("id User",User)
           hashes=hash256.hashlogin(User)
           out.set_cookie("hash",hashes)
           return out
       else :
           return '{"Response":"error","mode":"login"}'
    return '{"Response":200}'
=======
       testpass =  create.data_login(User,Password)
       if testpass:
           return "<h1>OK</h1>"
       else :
           return "<h1>error</h1>"
    return render_template("login.html")
>>>>>>> 2b9c063bab1e06f6065e912903be6e36770cdf26



@app.route('/create',methods=['POST','GET'])
def createa():
    if request.method=='POST':
       Password = request.form['password']
       User= request.form['email']
<<<<<<< HEAD
       datache=sql.data_create(User, Password)
       if datache==True:

           return '{"Response":"ok","mode":"craete"}'
       else : 
           return '{"Response":"ok","mode":"This email has already been registered"}'
    

    return '{"Response":200}'
=======
       create.data_create(User, Password)
       return "<h1>OK CREATE</h1>"


    return render_template("create.html")
>>>>>>> 2b9c063bab1e06f6065e912903be6e36770cdf26
if __name__ == '__main__':
    app.run()
