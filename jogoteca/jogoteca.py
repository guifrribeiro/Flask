# pip3 install flask==0.12.2
from flask import Flask
#pip3 install flask_mysqldb==0.2.0
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

app.run(debug=True)