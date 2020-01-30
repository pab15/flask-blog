from App import app
from flask import redirect, url_for, render_template, request, session
from flask_mail import Mail, Message

@app.route('/')
def index():
    if "username" in session:
        return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/all', methods=['GET', 'POST'])
def all():
    if "username" in session:
        return render_template('all.html')
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username == "") or (password == ""):
             return render_template('login.html')
        else:
            session["username"] = username
            session["password"] = password
            return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/signup')
def signup():
    if request.method == 'POST':
        user_name = request.form['user_name']
        e_mail = request.form['e_mail']
        pass_word = request.form['pass_word']
        password_confirm = request.form['pass_word_validate']
        if (user_name == "") or (e_mail == "") or (pass_word == "") or (password_confirm == ""):
             return render_template('sign-up.html')
        else:
            return render_template('login.html')
    else:
        return render_template('sign-up.html')

@app.route('/about')
def about():
    if "username" in session:
        user = session['username']
        return render_template('about.html', usr=user)
    else:
        return render_template('login.html')

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if "username" in session:
        if request.method == 'POST':
            first_name = request.form['firstname']
            last_name = request.form['lastname']
            email = request.form['email']
            message = request.form['message']
            if (first_name == "") or (last_name == "") or (email == "") or (message == ""):
                return render_template('contact.html')
            else:
                return render_template('successfulsub.html', fn=first_name, msg=message)
        else:
            return render_template('contact.html')
    else:
        return render_template('login.html')