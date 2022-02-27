from flask import Flask , render_template ,request
import create

app = Flask(__name__)

@app.route('/')
def hello_world():


    return render_template("index.html")
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
       Password = request.form['password']
       User= request.form['email']
       print(User)
       print(Password)
       testpass =  create.data_login(User,Password)
       if testpass:
           return "<h1>OK</h1>"
       else :
           return "<h1>error</h1>"
    return render_template("login.html")



@app.route('/create',methods=['POST','GET'])
def createa():
    if request.method=='POST':
       Password = request.form['password']
       User= request.form['email']
       create.data_create(User, Password)
       return "<h1>OK CREATE</h1>"


    return render_template("create.html")
if __name__ == '__main__':
    app.run()
