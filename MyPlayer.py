'''
    File name: 18.py
    Author: Utkarsh Kunwar, Utkrisht Dhankar
    Email: utkarsh2602@gmail.com
    Date created: 22 Oct 2017
    Date last modified: 22 Oct 2017
'''
import copy
from framework import Board, Player, Piece

class MyPlayer(Player):

    def __init__(self):
        pass

    def get_move(self,board):
        '''
        :param board: Board object
        :return: (piece,new_position,BoardLeavingMove)
        '''
        # Get best move for first player
        if board.turn == 1:
            best_val = float('-inf')
            best_move = ()
            for move in board.get_valid_moves():
                board_copy = self.copy_board(board)
                board_copy = self.try_move(board_copy, move)[1]
                move_val = self.alphabeta(board_copy)
                #board.make_move(move)
                #move_val = self.alphabeta(board)
                #board.make_move(self.undo_move(board, move))
                if move_val > best_val:
                    best_val = move_val
                    best_move = move
            return best_move
        # Get best move for second player
        else:
            best_val = float('inf')
            best_move = ()
            for move in board.get_valid_moves():
                board_copy = self.copy_board(board)
                board_copy = self.try_move(board_copy, move)[1]
                move_val = self.alphabeta(board_copy)
                #board.make_move(move)
                #move_val = self.alphabeta(board)
                #board.make_move(self.undo_move(board, move))
                if move_val < best_val:
                    best_val = move_val
                    best_move = move
            return best_move

    # Returns the evaluation value of the board configuration
    def evaluate(self, board):
        from random import uniform
        return uniform(-1000, 1000)

    # Copies board... because paranoia.
    def copy_board(self, board):
        board_copy = Board(size=board.size)
        board_copy.turn = board.turn
        board_copy.player_1_pieces = copy.deepcopy(board.player_1_pieces)
        board_copy.player_2_pieces = copy.deepcopy(board.player_2_pieces)
        return board_copy

    # Uses the MiniMax Algorithm with AlphaBeta pruning to get the MiniMax value.
    def alphabeta(self, board, alpha=float('-inf'), beta=float('inf'), depth=3):
        # Terminal node
        if depth is 0 or not board.get_valid_moves():
            return self.evaluate(board)

        moves = board.get_valid_moves()
        # For MAX
        if board.turn == 1:
            for move in moves:
                board_copy = self.copy_board(board)
                board_copy = self.try_move(board_copy, move)[1]
                val = self.alphabeta(board_copy, alpha=alpha, beta=beta, depth=depth-1)
                #board.make_move(move)
                #val = self.alphabeta(board, alpha=alpha, beta=beta, depth=depth-1)
                #board.make_move(self.undo_move(board, move))
                if val > alpha:
                    alpha = val
                if alpha > beta:
                    break
            return alpha
        # For MIN
        else:
            for move in moves:
                board_copy = self.copy_board(board)
                board_copy = self.try_move(board_copy, move)[1]
                val = self.alphabeta(board_copy, alpha=alpha, beta=beta, depth=depth-1)
                #board.make_move(move)
                #val = self.alphabeta(board, alpha=alpha, beta=beta, depth=depth-1)
                #board.make_move(self.undo_move(board, move))
                if val < beta:
                    beta = val
                if alpha > beta:
                    break
            return beta

    # Just to do the move without the prints in the 'framework/Board.py'
    # and return the modified board along it as well.
    def try_move(self, board, move):
        if move not in board.get_valid_moves():
            return ('lost', board)
        if board.turn == 1:
            for piece in board.player_1_pieces:
                if piece == move[0]:
                    piece.pos = move[1]
                    if move[2] == True:
                        piece.dead = True
                    pieces_left = [item for item in board.player_1_pieces if item.dead == False]
                    if len(pieces_left) == 0:
                        # Opposite Loses
                        return ('lost', board)
            board.turn = 2
            return ('continue', board)

        elif board.turn == 2:
            for piece in board.player_2_pieces:
                if piece == move[0]:
                    piece.pos = move[1]
                    if move[2] == True:
                        piece.dead = True
                    pieces_left = [item for item in board.player_2_pieces if item.dead == False]
                    if len(pieces_left) == 0:
                        # Opposite Loses
                        return ('lost', board)
            board.turn = 1
            return ('continue', board)

        if len(board.get_valid_moves()) == 0:
            # Other oppoment is blocked by this move
            if board.turn == 1:
                # Opposite loses
                board.turn = 2
                return ('lost', board)
            elif board.turn == 2:
                # Opposite loses
                board.turn = 1
                return ('lost', board)

    # To undo the move made
    def undo_move(self, board, move):
        undo = list(move)
        if board.turn == 1:
            for piece in board.player_1_pieces:
                if piece == move[0]:
                    undo[1] = piece.pos
        if board.turn == 2:
            for piece in board.player_2_pieces:
                if piece == move[0]:
                    undo[1] = piece.pos
        return undo
