from flask import Flask

app = Flask(__name__)

app.secret_key = b'thisisabadsessionprivatekey12354643'

from App import routes