import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template

# conn = sqlite3.connect('data.db')
# c = conn.cursor()

# # c.execute("""CREATE TABLE player2moves(
# #     Player2_move integer
# # )""")
# # c.execute("""CREATE TABLE turn(
# #     Player1 bool,
# #     Player2 bool
# # )""")

# lista1 = '3'
# lista2 = '6'

# # c.execute("INSERT INTO game (Player1, Player2) VALUES (True, False)")
# # c.execute("SELECT * FROM game")


# # merged_list = [[lista1[i], lista2[i]] for i in range(0, len(lista1))] 

      


# c.executemany("INSERT INTO player1moves (Player1_move) VALUES (?)", lista1)
# c.executemany("INSERT INTO player2moves (Player2_move) VALUES (?)", lista2)



# # # c.execute("SELECT * FROM game")
# # c.execute("SELECT Player2_move FROM move")
# # p2Move = c.fetchall()
# # print(p2Move)

# conn.commit()
# conn.close()
