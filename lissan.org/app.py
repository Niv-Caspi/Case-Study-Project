from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyBXMcC8_EtUT0nozIWQPCbJ10rzdHNwMJQ",
  "authDomain": "case-study-project-3d992.firebaseapp.com",
  "databaseURL": "https://case-study-project-3d992-default-rtdb.firebaseio.com",
  "projectId": "case-study-project-3d992",
  "storageBucket": "case-study-project-3d992.appspot.com",
  "messagingSenderId": "255120934931",
  "appId": "1:255120934931:web:f21c9ea3e89f2522d617e6",
  "measurementId": "G-LJQ8B3589M"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='', static_folder='')
app.config['srtHRHTTRHTRJtyKutueyew432436%$7%CVu'] = 'gerGREREhetHTRJyt325#V34Tv3easace'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def home():
    return render_template('Home/index.html')

@app.route("/for-students")
def student():
    return render_template('lissan-for-students.org/index.html')

@app.route("/for-students/shop")
def shop():
    return render_template('lissan-for-students.org/מי-אנחנו/index.html')

@app.route("/for-students/grades")
def grades():
    return render_template('lissan-for-students.org/אודות/index.html')

@app.route("/for-students/forum", methods = ['POST', 'GET'])
def forum():

    comm = db.child("Comments").get().val()
    if request.method == 'POST':
        name = request.form["name"]
        content = request.form["content"]
        date = request.form["date"]        
        comment = {"name": name, "date": date, "content": content}
        db.child("Comments").push(comment)
        comm = db.child("Comments").get().val()
        return render_template("lissan-for-students.org/עדכונים/index.html", c = comm)
    
    return render_template("lissan-for-students.org/עדכונים/index.html", c = comm)
    

@app.route('/for-students/login', methods = ['POST', 'GET'])
def login():
    error = ""
    if request.method == 'POST':
        email = request.form['lemail']
        password = request.form['lpassword']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            print("Way To Go!")
            return redirect(url_for('student'))
        except:
            error = "Authentication failed"
            return render_template("lissan-for-students.org/Login/index.html")
    return render_template("lissan-for-students.org/Login/index.html")
    
@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['semail']
        password = request.form['spassword']
        name = request.form['susername']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"name": name, "email": email, "password": password}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('student'))
        except: 
            return render_template("lissan-for-students.org/Login/index.html")
    return render_template("lissan-for-students.org/Login/index.html")


if __name__ == '__main__':
    app.run(debug=True)