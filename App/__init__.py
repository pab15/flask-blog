from flask import Flask

app = Flask(__name__)

app.secret_key = b'thisisabadsessionprivatekey1235464345'
app.config['TEMPLATES_AUTO_RELOAD'] = True

from App import routes