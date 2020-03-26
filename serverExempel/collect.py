import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template
import requests
import time



# app = Flask(__name__)


# @app.route('/weatherstation')
def collectGame():

    response = requests.get('http://127.0.0.1:5000/new')
    
    klientsvar = response.json()

    print(klientsvar)
collectGame()
# if __name__ == '__main__':
#     app.run()


