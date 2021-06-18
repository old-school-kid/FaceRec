<<<<<<< HEAD
from flask import Flask,render_template,request,redirect
from flask_login import login_required, current_user, login_user, logout_user
from models import UserModel,db,login
import os
import cv2

app = Flask(__name__)
app.secret_key = 'xyz'
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
 
db.init_app(app)
login.init_app(app)
login.login_view = 'login'
 
@app.before_first_request
def create_all():
    db.create_all()
     
@app.route('/index')
@login_required
def index():
    return render_template('index.html')
 
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            exec(open('main_code.py').read())
            return redirect('/index')
     
    return render_template('login.html')
 
@app.route('/face_rec')
def face_rec(name):
    cap= cv2.VideoCapture(0)
    while(True):
        ret, frame= cap.read()
        #hit space to capture image
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord(' ') :
            cv2.imwrite("people/"+str(name)+".jpg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    return 'Face image recorded!'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        #profile_pic = request.form['profile_pic']
 
        if UserModel.query.filter_by(email=email).first():
            return ('Email already Present')
             
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        face_rec(username)
        return redirect('/index')
    return render_template('register.html')
 
 
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

if __name__ == "__main__":
=======
from flask import Flask,render_template,request,redirect
from flask_login import login_required, current_user, login_user, logout_user
from models import UserModel,db,login
import os
import cv2

app = Flask(__name__)
app.secret_key = 'xyz'
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
 
db.init_app(app)
login.init_app(app)
login.login_view = 'login'
 
@app.before_first_request
def create_all():
    db.create_all()
     
@app.route('/index')
@login_required
def index():
    return render_template('index.html')
 
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            exec(open('main_code.py').read())
            return redirect('/index')
     
    return render_template('login.html')
 
@app.route('/face_rec')
def face_rec(name):
    cap= cv2.VideoCapture(0)
    while(True):
        ret, frame= cap.read()
        #hit space to capture image
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord(' ') :
            cv2.imwrite("people/"+str(name)+".jpg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    return 'Face image recorded!'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        #profile_pic = request.form['profile_pic']
 
        if UserModel.query.filter_by(email=email).first():
            return ('Email already Present')
             
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        face_rec(username)
        return redirect('/index')
    return render_template('register.html')
 
 
@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

if __name__ == "__main__":
>>>>>>> 5f03060fac5de771be6c18ff3c1d1bebf250bafb
    app.run(debug=True)