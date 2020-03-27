import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template
import requests
import time
import testinput
import numpy as np
import os
import funktioner as funk

RAD = 6
KOLUMN = 7

def playGame():
    os.system('cls')
    board = funk.fillBoard(RAD,KOLUMN)
    print(board)
    gameOver = False
    try:                 
        newGame = requests.get('http://127.0.0.1:5000/newgame').text
        player = int(newGame)
        newTurn = requests.get('http://127.0.0.1:5000/whosturn').text
        turn = int(newTurn)
    except requests.exceptions.ConnectionError:
        print('Error connecting to server')
    isMyTurn = turn == player   
    while not gameOver:      
        if isMyTurn == True:
            try:  
                funk.fillBoard(RAD,KOLUMN)                      
                inCol = int(input("Time to make your move (1-7):")) 
                inCol -= 1                                    
                if inCol > (KOLUMN-1):
                    turn -= 1
                    os.system('cls')
                    print('\nInvalid location, try again\n')
                else:
                    os.system('cls')  
                    if funk.validLoc(board, inCol):
                        row = funk.getOpenRow(board, inCol, RAD)
                        funk.dropObject(board, row, inCol, (turn+1))
                        if player == 0:
                            placeholder = 'sendmoves1'
                        else: 
                            placeholder = 'sendmoves2'
                        varmove = str(inCol)
                        requests.get(f'http://127.0.0.1:5000/{placeholder}', data={'move':varmove})
                        funk.fillBoard(RAD,KOLUMN)                            
                    else:
                        turn -= 1
                        os.system('cls')
                        print('\nInvalid location, try again\n')
            except ValueError:
                os.system('cls')
                print('\nThis is not a number\n')
                funk.fillBoard(RAD,KOLUMN)
                turn -= 1
        else:
            while True:
                newTurn = requests.get('http://127.0.0.1:5000/whosturn').text
                turn = int(newTurn)
                isMyTurn = turn == player 
                if isMyTurn == False:
                    print('Wait for your turn')
                    time.sleep(5)
                    os.system('cls')                    
                else:
                    break
        newTurn = requests.get('http://127.0.0.1:5000/whosturn').text
        turn = int(newTurn)
        isMyTurn = turn == player

playGame()





