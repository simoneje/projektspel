import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template
import requests
import time
import testinput
import numpy as np
import os


app = Flask(__name__)
app.debug = True

@app.route('/newgame')
def gametime():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    Player1 = '0'
    Player2 = '1'
    c.execute("SELECT Player1 FROM game")
    result = c.fetchall()

    #Om result är en tom lista eller om index i result är 0
    if not result or (not result and result[len(result)-1][0] == False):
        c.execute("INSERT INTO game (Player1, Player2) VALUES (True, False)")        
        conn.commit()
        conn.close()
        return Player1
    else:
        c.execute("INSERT INTO game (Player1, Player2) VALUES (True, True)")
        c.execute("INSERT INTO turn (Player1, Player2) VALUES (True, False)")
        conn.commit()
        conn.close()
        return Player2
    conn.commit()
    conn.close()

@app.route('/playermoves1')
def getMoves1():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM player1moves")
    p1Move = c.fetchall()
    conn.commit()
    conn.close()
    return jsonify(p1Move)

@app.route('/playermoves2')
def getMoves2():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM player2moves")
    p2Move = c.fetchall()
    conn.commit()
    conn.close()
    return jsonify(p2Move)

@app.route('/sendmoves1')
def postMoves():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    data = request.form.get('move')
    c.executemany("INSERT INTO player1moves (Player1_move) VALUES (?)", data)
    c.execute("INSERT INTO turn (Player1, Player2) VALUES (False, False)")

    conn.commit()
    conn.close() 

@app.route('/sendmoves2')
def postMoves2():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    data = request.form.get('move')
    c.executemany("INSERT INTO player2moves (Player2_move) VALUES (?)", data)
    c.execute("INSERT INTO turn (Player1, Player2) VALUES (True, True)")
    conn.commit()
    conn.close() 

@app.route('/whosturn')
def vemsTur():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    Player1 = '0'
    Player2 = '1'
    c.execute("SELECT Player1 FROM turn")
    result = c.fetchall()
    if not result or result[len(result)-1][0] == True:    
        return Player1
    else:
        return Player2

  
if __name__ == '__main__':
    app.run()
