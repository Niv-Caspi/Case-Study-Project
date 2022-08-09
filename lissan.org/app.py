from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyD-suLqhR2ikGog6OiAXgVqoYouTWa5tE8",
  "authDomain": "individual-project-7e24c.firebaseapp.com",
  "projectId": "individual-project-7e24c",
  "storageBucket": "individual-project-7e24c.appspot.com",
  "messagingSenderId": "640220452831",
  "appId": "1:640220452831:web:f9dcabe78cbd0f41a4966a",
  "measurementId": "G-HWRB93R0M8",
  "databaseURL": "https://individual-project-7e24c-default-rtdb.firebaseio.com"
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

@app.route('/for-students/login', methods = ['POST', 'GET'])
def login():
    """
    error = ""
    if request.method == 'POST':
        email = request.form['email-signin']
        password = request.form['password-signin']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            return render_template("lissan-for-students.org/Login/index.html")
    """
    return render_template("lissan-for-students.org/Login/index.html")


if __name__ == '__main__':
    app.run(debug=True)