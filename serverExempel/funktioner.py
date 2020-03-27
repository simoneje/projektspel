import numpy as np
import os
import sqlite3
from sqlite3 import Error
from flask import Flask, escape, request, jsonify, render_template
import requests
import time
import sys
RAD = 6
KOLUMN = 7

#Skapar en 2d array utav nollor
def boardCreate(Rad, Kolumn):
    board = np.((Rad,Kolumn))
    return board

#bestämmer vart objektet/pjäsen släpps
def dropObject(board, row, col, obj):
    board[row][col] = obj

#Kollar om kolumnen är tillgänglig för att 
def validLoc(board, col):
    return board[RAD-1][col] == 0

def getOpenRow(board, col, rad):
    for r in range(rad):
        if board[r][col] == 0:
            return r


def flipBoard(board):
    print(np.flip(board, 0))

def dbConnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        print(Error)
    return conn

def cleanDbTable(dbtable, db_file):

    conn = dbConnection(db_file)
    sql = f'DELETE FROM {dbtable}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def fillBoard(Rad, Kolumn):
    try:                 
        p1Move = requests.get('http://127.0.0.1:5000/playermoves1')
        p2Move = requests.get('http://127.0.0.1:5000/playermoves2')
    except requests.exceptions.ConnectionError:
        print('Error connecting to server')
    board = boardCreate(RAD, KOLUMN)
    p1Movelist = p1Move.json()
    p2Movelist = p2Move.json()
    if len(p1Movelist) > 0:
        while len(p1Movelist) or len(p2Movelist) > 0:
            inCol = p1Movelist.pop(0)      
            if validLoc(board, inCol):                
                row = getOpenRow(board, inCol, RAD)
                dropObject(board, row, inCol, 1)
                if victory(board, 1):
                    print('Game Over!')
                    flipBoard(board)
                    time.sleep(2)
                    print('But BOTH are WINNERS :D')
                    time.sleep(6)
                    cleanDbTable('player1moves', 'data.db')
                    cleanDbTable('player2moves', 'data.db')
                    cleanDbTable('game', 'data.db')
                    cleanDbTable('turn', 'data.db')
                    cleanDbTable('move', 'data.db')
                    sys.exit()
            if len(p2Movelist) > 0:
                inCol = p2Movelist.pop(0)
                if validLoc(board, inCol):
                    row = getOpenRow(board, inCol, RAD)
                    dropObject(board, row, inCol, 2)
                    if victory(board, 2):
                        print('Game Over!')
                        flipBoard(board)
                        time.sleep(2)
                        print('But BOTH are WINNERS :D')
                        time.sleep(6)
                        cleanDbTable('player1moves', 'data.db')
                        cleanDbTable('player2moves', 'data.db')
                        cleanDbTable('game', 'data.db')
                        cleanDbTable('turn', 'data.db')
                        cleanDbTable('move', 'data.db')                      
                        sys.exit()
            else:
                pass                   
        return flipBoard(board)
    else:
        board = boardCreate(RAD, KOLUMN)
        return board

def victory(board, piece):
    #Kollar horizentalt för vinst
    for k in range(KOLUMN-3): #tar bort tre eftersom det går ej att vinna från vissa postioner
        for r in range(RAD):
            if board[r][k] == piece and board[r][k+1] == piece and board[r][k+2] == piece and board[r][k+3] == piece:
                return True

    #Kollar vertikalt för vinst
        for k in range(KOLUMN):
            for r in range(RAD-3): # vi kan inte starta på top raden
                if board[r][k] == piece and board[r+1][k] == piece and board[r+2][k] == piece and board[r+3][k] == piece:
                    return True

    #Kollar diagonellt för vinst positiv, måste ha minus 3 på bägge eftersom man inte kan vinna från top 3.
    #Denna funktion kollar dem positiva värderna för diagonellt
    for k in range(KOLUMN-3):
        for r in range(RAD-3):
            if board[r][k] == piece and board[r+1][k+1] == piece and board[r+2][k+2] == piece and board[r+3][k+3] == piece:
                return True

    #Kollar diagonellt för vinst negativt, måste ha 
    for k in range(KOLUMN-3):
        for r in range(3, RAD): #har 3 för tredje indexet på spelplanen som behövs för att kunna få fyra i rad. 
            if board[r][k] == piece and board[r-1][k+1] == piece and board[r-2][k+2] == piece and board[r-3][k+3] == piece:
                return True


# cleanDbTable('player1moves', 'data.db')
# cleanDbTable('player2moves', 'data.db')
# cleanDbTable('game', 'data.db')
# cleanDbTable('turn', 'data.db')
# cleanDbTable('move', 'data.db')
