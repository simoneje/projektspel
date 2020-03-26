import numpy as np
import os
import sqlite3
from sqlite3 import Error
RAD = 6
KOLUMN = 7

def boardCreate(Rad, Kolumn):
    board = np.zeros((Rad,Kolumn))
    return board

def fillBoard(Rad, Kolumn):
    turn = 0
    board = boardCreate(RAD, KOLUMN)
    conn = sqlite3.connect('playermove.db')
    c = conn.cursor()
    c.execute("SELECT Player1_move FROM move")
    p1Move = c.fetchall()
    c.execute("SELECT Player2_move FROM move")
    p2Move = c.fetchall()
    while len(p2Move) > 0:
        if turn == 0:
            col = p1Move.pop(0)
            os.system('cls')        
            if validLoc(board, col):                
                row = get_next_open_row(board, col, RAD)
                dropPiece(board, row, col, 1)
        else:
            col = p2Move.pop(0)
            os.system('cls')  
            if validLoc(board, col):
                row = get_next_open_row(board, col, RAD)
                dropPiece(board, row, col, 2)
                
        
        turn += 1
        turn = turn % 2 
    conn.commit()
    conn.close()  
    flipBoard(board)
    return board

def inputlist(move1, move2):
    playermove = [[move1, move2]]
    conn = sqlite3.connect('playermove.db')
    c = conn.cursor()
    c.executemany("INSERT INTO move (Player1_move, Player2_move) VALUES (?, ?)", playermove)
    conn.commit()
    conn.close()
    playermove.clear()
    # else:
        # c.execute("SELECT Player2_move FROM move")
        # p2Move = c.fetchall()
        # if len(p2Move) > 0:
        #     pass
        #     # skapa bord med moves
        # else:


def dropPiece(board, row, col, piece):
    board[row][col] = piece


def validLoc(board, col):
    return board[5][col] == 0


def get_next_open_row(board, col, rad):
    for r in range(rad):
        if board[r][col] == 0:
            return r

def flipBoard(board):
    # os.system('cls')
    print(np.flip(board, 0))

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def delete_all_tasks(dbtable, db_file):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    conn = create_connection(db_file)
    sql = f'DELETE FROM {dbtable}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

delete_all_tasks('move', 'playermove.db')
# fillBoard()