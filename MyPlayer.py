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
                board_copy = self.try_move(board_copy, move)
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
                board_copy = self.try_move(board_copy, move)
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
        def lane_blocked(board):
            board_matrix = board.get_board_config()[0]
            h_value = 0
            for row in xrange(0, board.size):
                for col in xrange(0, board.size):
                    if board_matrix[row][col] == 1:
                        for down in xrange(row, board.size - 1):
                            if board_matrix[down][col] == 2:
                                h_value = h_value + 2 / (down - row + 1)
                        for right in xrange(col, board.size - 1):
                            if board_matrix[row][right] == 2:
                                h_value = h_value - 2 / (right - col + 1)
            return 10 * h_value

        def finish_distance(board):
            h_value = 0
            for piece in board.player_1_pieces:
                h_value = h_value + (2 / (board.size - piece.pos[1] + 2))
            for piece in board.player_2_pieces:
                h_value = h_value - (2 / (piece.pos[0] + 2))
            return h_value

        def num_pieces(board):
            h_value = 0
            for piece in board.player_1_pieces:
                if piece.dead:
                    h_value = h_value + 1
            for piece in board.player_2_pieces:
                if piece.dead:
                    h_value = h_value - 1
            return h_value

        return lane_blocked(board) + finish_distance(board) + num_pieces(board)

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
                board_copy = self.try_move(board_copy, move)
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
                board_copy = self.try_move(board_copy, move)
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
            return board
        if board.turn == 1:
            for piece in board.player_1_pieces:
                if piece == move[0]:
                    piece.pos = move[1]
                    if move[2] == True:
                        piece.dead = True
                    pieces_left = [item for item in board.player_1_pieces if item.dead == False]
                    if len(pieces_left) == 0:
                        # Opposite Loses
                        return board
            board.turn = 2
            return board

        elif board.turn == 2:
            for piece in board.player_2_pieces:
                if piece == move[0]:
                    piece.pos = move[1]
                    if move[2] == True:
                        piece.dead = True
                    pieces_left = [item for item in board.player_2_pieces if item.dead == False]
                    if len(pieces_left) == 0:
                        # Opposite Loses
                        return board
            board.turn = 1
            return board

        if len(board.get_valid_moves()) == 0:
            # Other oppoment is blocked by this move
            if board.turn == 1:
                # Opposite loses
                board.turn = 2
                return board
            elif board.turn == 2:
                # Opposite loses
                board.turn = 1
                return board
