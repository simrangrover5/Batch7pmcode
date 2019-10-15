from flask import Flask,render_template,request
import pymysql as sql
from flask import session

app = Flask(__name__)
app.secret_key = "pijfpijpijpfijpijpiwjeohwouhohohoiojwiojwoojenfjnojojojj"

@app.route('/')
def index():
    return render_template("index.html")
    #return "Hello world"

@app.route('/<var>/')
def hello(var):
    return render_template("one.html",name=var)

@app.route('/about/<var>/<int:m>')
def about(var,m):
    dict = {
        'name' : var,
        'marks' : m
    }
    return render_template("one.html",data=dict)
    #return f"<h1 style='color:red'>Welcome to my world {var} with num {m}</h1><br><p>"

@app.route('/login/')
def login():
    if session.get('email'):
        return render_template("one.html")
    else:
        return render_template("login.html")


@app.route('/signup/')
def signup():
    return render_template("signup.html")

@app.route('/login1/',methods=['GET','POST'])
def login1():
    email = request.form.get('email')
    password = request.form.get('pswd')
    try:
        db = sql.connect(host='localhost',port=3306,user='root',password='',database='batch7pm')
        c = db.cursor()
        cmd = 'select * from user where email="{}"'.format(email)
        c.execute(cmd)
        data = c.fetchone()
        print(data)
        if data:
            if password == data[1]:
                session['email'] = email
                session['password'] = password
                return render_template("one.html")
                #return "<h1 style='color:red'>Welcome user with email {}</h1>".format(email)
            else:
                error = "Password does not match"
                return render_template("login.html",error=error)
        else:
            error = "No such user"
            return render_template("login.html",error=error)
    except Exception as e:
        return e


@app.route('/signup1/',methods=['GET','POST'])
def signup1():
    password = request.form.get('pswd')
    cpassword = request.form.get('cpswd')
    if password == cpassword:
        email = request.form.get('email')
        file = request.form.get('myfile')
        f = request.files['myfile']
        fn = f.filename
        ext = fn.split('.')[-1]
        f.save("static/images/"+email+"."+ext)
        print(fn)
        """try:
            db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch7pm")
            c = db.cursor()
            cmd = "insert into user values('{}','{}','{}')".format(email,password,file)
            c.execute(cmd)
            db.commit()
            return render_template("login.html")
        except Exception as e:
            return "Error.....{}".format(e)"""
        return "Success"
            


    else:
        error = "Invalid password"
        return render_template("signup.html",error=error)

@app.route('/logout/')
def logout():
    del session['email']
    del session['password']
    return render_template("login.html")

app.run(host="localhost",port=80,debug=True)