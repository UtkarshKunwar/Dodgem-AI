#!/usr/bin/env python
'''
    File name: Assign2.py
    Author: Siddhant Kumar
    Email: saytosid@gmail.com
    Date created: 1 Oct 2017
    Date last modified: 1 Oct 2017
    Python Version: 3.0
'''

from framework import Board,Game,Player
import numpy as np
import time
from Group18 import MyPlayer
from OtherPlayer import MyPlayer as OtherPlayer
np.set_printoptions(suppress=True)


if __name__=='__main__':
    board = Board(size=5)
    player_1 = OtherPlayer() # Random player
    player_2 = MyPlayer() # MyPlayer

    game = Game(board,player_1,player_2)

    start = time.time()
    while (game.step()==0):
        stop = time.time()
        board_matrix,turn = board.get_board_config()
        print(board_matrix)
        print("Time = ", stop - start)
        print(" ")
        start = stop

