import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template
import requests
import time
import testinput
import numpy as np
import os
import funktioner as funk
# import collect 
RAD = 6
KOLUMN = 7
def playGame():
    board = funk.fillBoard(RAD, KOLUMN)
    # print(board)
    # SKA VI FYLLA BORDET?
    # funk.fillBoard()
    #  
    gameOver = False                 
    turn = 0
    player1 = requests.get('http://127.0.0.1:5000/newgame')
    print(player1.text)
    if player1.text == 'player1':
        turn == 0
    else: 
        turn == 1
    while not gameOver:
        if turn == 0:
            try:                        
                col1 = int(input("Player 1 Make your move (1-7):")) 
                col1 -= 1
                if col1 > 6:
                    turn -= 1
                    os.system('cls')
                    print('\nInvalid location, try again\n')
                else:
                    os.system('cls')  
                    if funk.validLoc(board, col1):
                        row = funk.get_next_open_row(board, col1, RAD)
                        funk.dropPiece(board, row, col1, 1)                
                    else:
                        turn -= 1
                        os.system('cls')
                        print('\nInvalid location, try again\n')
            except ValueError:
                os.system('cls')
                print('\nThis is not a number\n')
                turn -= 1
        else:
            try:                
                col2 = int(input("Player 2 Make your move (1-7):"))
                col2 -= 1
                if col2 > 6:
                    turn -= 1
                    os.system('cls')
                    print('\nInvalid location, try again\n')
                else:
                    os.system('cls')  
                    if funk.validLoc(board, col2):
                        row = funk.get_next_open_row(board, col2, RAD)
                        funk.dropPiece(board, row, col2, 2)
                    else: 
                        turn -= 1
                        os.system('cls')
                        print('\nInvalid location, try again\n')
            except ValueError:
                os.system('cls')
                print('\nThis is not a number\n')
                turn -= 1
        
        funk.flipBoard(board)
        turn += 1  
        if turn == 2:
            funk.inputlist(col1, col2)      
        turn = turn % 2

playGame()

# def turnTime():

#     player1 = requests.get('http://127.0.0.1:5000/newgame')
#     board = funk.boardCreate(RAD, KOLUMN)
#     if player1.text == 'player1':

#         int(input("Player 1 Make your move (1-7):"))


