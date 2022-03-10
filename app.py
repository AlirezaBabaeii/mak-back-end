from flask import Flask ,request ,make_response
import hash256
import sql
app = Flask(__name__)

@app.route('/')
def hello_world():

    return '{"Response":200,"URL":{"login":"/login","create":"/craete"}}'
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
       Password = request.form['password']
       User= request.form['email']
       print(User)
       print(Password)
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



@app.route('/create',methods=['POST','GET'])
def createa():
    if request.method=='POST':
       Password = request.form['password']
       User= request.form['email']
       datache=sql.data_create(User, Password)
       if datache==True:

           return '{"Response":"ok","mode":"craete"}'
       else : 
           return '{"Response":"ok","mode":"This email has already been registered"}'
    

    return '{"Response":200}'
if __name__ == '__main__':
    app.run()
