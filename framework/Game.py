'''
    File name: Game.py
    Author: Siddhant Kumar
    Email: saytosid@gmail.com
    Date created: 1 Oct 2017
    Date last modified: 1 Oct 2017
    Python Version: 3.0
'''
from Board import Board
from Player import Player

class Game:

    def __init__(self,board, player_1, player_2):
        '''
        :param board: Board object
        :param player_1: Player object
        :param player_2: Player Object
        '''
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
        self.mov_ctr = 0
        self.game_over = False

    def step(self):
        '''
        :return: 1 if game is over, 0 otherwise
        '''
        if self.game_over == True:
            print('This game is over')
            return 1
        if self.board.turn == 1:
            status,extra_info = self.board.make_move(self.player_1.get_move(self.board))
            if status == 'lost':
                print('Player_'+str(extra_info)+' Lost')
                self.game_over = True
            self.board.turn = 2
        else:
            status,extra_info = self.board.make_move(self.player_2.get_move(self.board))
            if status == 'lost':
                print('Player_'+str(extra_info)+' Lost')
                self.game_over = True
            self.board.turn = 1

        self.mov_ctr += 1
        return 0


