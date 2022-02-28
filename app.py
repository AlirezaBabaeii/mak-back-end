from flask import Flask , render_template ,request
import create

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
       testpass =  create.data_login(User,Password)
       if testpass:
           return '{"Response":"ok","mode":"login"}'
       else :
           return '{"Response":"error","mode":"login"}'
    return '{"Response":200}'



@app.route('/create',methods=['POST','GET'])
def createa():
    if request.method=='POST':
       Password = request.form['password']
       User= request.form['email']
       create.data_create(User, Password)
       return '{"Response":"ok","mode":"craete"}'


    return '{"Response":200}'
if __name__ == '__main__':
    app.run()
