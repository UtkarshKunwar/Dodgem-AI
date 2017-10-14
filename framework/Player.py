'''
    File name: Player.py
    Author: Siddhant Kumar
    Email: saytosid@gmail.com
    Date created: 1 Oct 2017
    Date last modified: 1 Oct 2017
    Python Version: 3.0
'''
import random

class Player:
    '''Defines a Random Move Player'''
    def __init__(self):
        pass

    def get_move(self, board):
        '''
        Override this method to create your player
        :param board: Board object
        :return: move i the format (piece,new_position,BoardLeavingMove)
        '''

        return alphabeta(board)

    def eval(self, board):
        return random.uniform(-1000, 1000)

    def alphabeta(self, board, max_player=True, alpha=float('-inf'), beta=float('inf'), max_ply=3):
        if max_ply == 1:
            return eval(board)

        board_copy=[row[:] for row in board]
        if max_player:
            best_val = float('-inf')
            for move in board.get_valid_moves():
                board_copy.make_move(move)
                val = alphabeta(board_copy, max_player=false, alpha=alpha, beta=beta, max_ply=max_ply - 1)
                best_val = max(best_val, val)
                alpha = max(alpha, best_val)

                if alpha >= beta:
                    break
            return best_val
        else:
            best_val = float('inf')
            for move in board.get_valid_moves():
                board_copy.make_move(move)
                val = alphabeta(board_copy, max_player=True, alpha=alpha, beta=beta, max_ply=max_ply - 1)
                best_val = min(best_val, val)
                beta = min(beta, best_val)

                if alpha >= beta:
                    break
            return best_val
