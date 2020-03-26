import sqlite3
from random import randint
from flask import Flask, escape, request, jsonify, render_template

conn = sqlite3.connect('playermove.db')
c = conn.cursor()

# c.execute("""CREATE TABLE move(
#     Player1_move integer,
#     Player2_move integer
# )""")
# c.execute("""CREATE TABLE game(
#     Player1 bool,
#     Player2 bool
# )""")

lista1 = [1,5,6,4,2,4,5]
lista2 = [4,2,5,3,1,5,2]

# c.execute("INSERT INTO game (Player1, Player2) VALUES (True, False)")
# c.execute("SELECT * FROM game")


# merged_list = [[lista1[i], lista2[i]] for i in range(0, len(lista1))] 

      


# c.executemany("INSERT INTO move (Player1_move, Player2_move) VALUES (?, ?)", merged_list)



# # c.execute("SELECT * FROM game")
c.execute("SELECT Player2_move FROM move")
p2Move = c.fetchall()
print(p2Move)

conn.commit()
conn.close()