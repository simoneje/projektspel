import numpy as np
import os

RAD = 6
KOLUMN = 7


turn = 0
gameOver = False

def boardCreate():
    board = np.zeros((6,7))
    return board
board = boardCreate()


def dropPiece(board, row, col, piece):
    board[row][col] = piece


def validLoc(board, col):
    return board[5][col] == 0


def get_next_open_row(board, col):
    for r in range(RAD):
        if board[r][col] == 0:
            return r

def flipBoard(board):
    # os.system('cls')
    print(np.flip(board, 0))

def victory(board, row, col, piece):
    vinst = 1 * 4
    if col == vinst:
        print('vinst')
    else: 
        pass
# def colFull(board, col, piece):
#     if col in range(6):
#         print('error')


    
print(board)
while not gameOver:

    if turn == 0: 
        col = int(input("Player 1 Make your move (0-6):"))
        if validLoc(board, col):
            row = get_next_open_row(board, col)
            dropPiece(board, row, col, 1)

        else:
            turn -= 1
            print('\nInvalid location, try again')

    else:

        col = int(input("Player 2 Make your move (0-6):"))
        if validLoc(board, col):
            row = get_next_open_row(board, col)
            dropPiece(board, row, col, 2)
        else: 
            turn -= 1
            print('\nInvalid location, try again')
            
    flipBoard(board)
    turn += 1
    turn = turn % 2