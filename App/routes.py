import os
import sqlite3
from App import app
from flask import redirect, url_for, render_template, request, session

# Database Initializer:
db_connection = sqlite3.connect('database/flaskblog.db')

curs = db_connection.cursor()

# Use the cursor.execute() to use sql commands:
# curs.execute("""CREATE TABLE users (
#                 id integer,
#                 username text,
#                 email text,
#                 password text
#             )""")

db_connection.commit()

def addUser(username, email, password):
    curs.execute("""INSERT INTO users (username, email, password)
                    VALUES ({username}, {email}, {password})
                """)
    db_connection.commit()

# Home Page if logged in, otherwise user if directed to login page:
@app.route('/')
def index():
    if "username" in session:
        return render_template('index.html')
    else:
        return render_template('login.html')
    
# Shows a list of all pages in the website if admin is logged in,
#   otherwise the user is redirected to the login page:
@app.route('/all')
def all():
    view_data = {}
    files = os.listdir(r"C:\Users\peter\Desktop\Courses\CS-232\Projects\flask-blog\App\templates")
    view_data["pages"] = files
    if "username" in session:
        return render_template('all.html', allfiles=view_data)
    else:
        return render_template('login.html')

# Basic login page that makes sure the username and password fields
#   are not blank and then creates a session for the user and redirects 
#   them to the home page
#   ToDo: VALIDATE THAT THE USER EXISTS IN THE DATABASE
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
            return redirect(url_for('index'))
    else:
        if "username" in session:
            return render_template('index.html')
        else:
            return render_template('login.html')

# Basic sign up page that checks to make sure that all fields are blank 
#   and then redirects to the login page (does nothing) 
#   information posted to the server
# ToDo: ADD THE SIGNED UP USER TO THE DATABASE:
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_name = request.form['user_name']
        e_mail = request.form['e_mail']
        pass_word = request.form['pass_word']
        password_confirm = request.form['pass_word_validate']
        if (user_name == "") or (e_mail == "") or (pass_word == "") or (password_confirm == "") or (pass_word != password_confirm):
             return render_template('sign-up.html')
        else:
            addUser(user_name, e_mail, pass_word)
            return render_template('login.html')
    else:
        return render_template('sign-up.html')

# About page that checks if the user is logged in and has a session, and if they
#   do, returns a customized page for the user
# ToDo: ALLOW THE USER TO CHANGE THEIR ABOUT/PROFILE AND PULL INFO FROM
#       THE DATABASE TO DISPLAY TO THE USER, IF THEY CHANGE THIS INFO,
#       UPDATE THE DATABASE:
@app.route('/about', methods=['GET', 'POST'])
def about():
    if "username" in session:
        user = session['username']
        return render_template('about.html', usr=user)
    else:
        return render_template('login.html')

# Contact form that posts the data to the server and returns a customized
#   paged confirming that their message was sent, also will redirect the 
#   user if they dont have a session
#   ToDo: PUT THE MESSAGE INTO A DATABASE OR USE AN SMTP SERVER TO EMAIL 
#         THE MESSAGE TO MYSELF
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

# @app.route("/<view_name>")
# #input parameter name must match route parameter
# def render_page(view_name):
#     html = 'view_name' + '.html'
#     view_data = {} #create empty dictionary
#     return render_template(html, view_data=session)
