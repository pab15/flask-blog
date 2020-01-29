from App import app
from flask import redirect, url_for, render_template, request, session
from flask_mail import Mail, Message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('sign-up.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
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
