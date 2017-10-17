'''
    File name: Player.py
    Author: Siddhant Kumar
    Email: saytosid@gmail.com
    Date created: 1 Oct 2017
    Date last modified: 1 Oct 2017
    Python Version: 3.0
'''
import random, copy

class MyPlayer:
    '''Defines a Random Move Player'''
    def __init__(self):
        pass

    def get_move(self, board):
        '''
        Override this method to create your player
        :param board: Board object
        :return: move i the format (piece,new_position,BoardLeavingMove)
        '''

        return self.alphabeta(board)

    def eval(self, board):
        return random.uniform(-1000, 1000)

    def alphabeta(self, board, max_player=True, alpha=float('-inf'), beta=float('inf'), max_ply=3):
        if max_ply == 1:
            return self.eval(board)

        board_copy = copy.deepcopy(board)
        if max_player is True:
            best_val = float('-inf')
            best_move = ()
            for move in board.get_valid_moves():
                board_copy.make_move(move)
                val = self.alphabeta(board_copy, max_player=False, alpha=alpha, beta=beta, max_ply=max_ply - 1)
                best_val = max(best_val, val)
                alpha = max(alpha, best_val)
                best_move = move

                if alpha >= beta:
                    break
            return best_move
        else:
            best_val = float('inf')
            best_move = ()
            for move in board.get_valid_moves():
                board_copy.make_move(move)
                val = self.alphabeta(board_copy, max_player=True, alpha=alpha, beta=beta, max_ply=max_ply - 1)
                best_val = min(best_val, val)
                beta = min(beta, best_val)

                if alpha >= beta:
                    break
            return best_move
