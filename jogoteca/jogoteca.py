# pip3 install flask==0.12.2
from flask import Flask
#pip3 install flask_mysqldb==0.2.0
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

from views import *

# Garantindo que o app.run não é executado quando é importado
if __name__ == '__main__':
    app.run(debug=True)