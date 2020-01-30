from flask import Flask

app = Flask(__name__)

app.secret_key = b'thisisabadsessionprivatekey12'

from App import routes