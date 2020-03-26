import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template
import requests
import time
import testinput
import numpy as np
import os

# import game


app = Flask(__name__)


@app.route('/newgame')
def gametime():

    conn = sqlite3.connect('data.db')
    c = conn.cursor()


    c.execute("SELECT Player1 FROM game")
    result = c.fetchall()
    if result[len(result)-1][0] == True:
        c.execute("INSERT INTO game (Player1, Player2) VALUES (False, False)")
        conn.commit()
        conn.close()
        return ('Player 2, Make your move')
    else:
        c.execute("INSERT INTO game (Player1, Player2) VALUES (True, True)")
        conn.commit()
        conn.close()
        return ('Player1, Make your move')
    conn.commit()
    conn.close()
    


   
if __name__ == '__main__':
    app.run()




# def victory(board, piece):

#     for c in range(KOLUMN-3): #för att tre på ena sidan kan man inte vinna på
#         for r in range(RAD):
#             if board[r:r+4][c].all() == piece:
#                 return True

# def colFull(board, col, piece):
#     if col in range(6):
#         print('error')
# col = -1 + int(input("Player 1 Make your move (1-7):"))