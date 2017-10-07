'''
    File name: Board.py
    Author: Siddhant Kumar
    Email: saytosid@gmail.com
    Date created: 1 Oct 2017
    Date last modified: 1 Oct 2017
    Python Version: 3.0
'''
from Piece import Piece

class Board:
    def __init__(self,size = 3):
        '''
        :param size: Defines the size of the board
        '''
        self.size = size
        self.turn = 1 # Player 1 goes first
        self.player_1_pieces = list()
        for i in xrange(size):
            if i != size-1:
                self.player_1_pieces.append(Piece(color='black',position=(i,0)))

        self.player_2_pieces = list()
        for i in xrange(size):
            if i != 0:
                self.player_2_pieces.append(Piece(color='white',position=(size-1,i)))

    def get_board_config(self):
        '''
        :return: tupple (board_configuration,turn)
        '''

        import numpy as np
        board_matrix = np.zeros((self.size,self.size))
        for piece in self.player_1_pieces:
            if piece.dead == False:
                board_matrix[piece.pos[0],piece.pos[1]] = 1
        for piece in self.player_2_pieces:
            if piece.dead == False:
                board_matrix[piece.pos[0],piece.pos[1]] = 2

        return (board_matrix, self.turn)

    def make_move(self,(piece,new_pos,extra_info)):
        '''
        :return: ('lost',player_who_lost) or ('game continues',None)
        '''
        print('Player_'+str(self.turn)+' played: '+str(piece.pos)+'->'+str(new_pos))
        if (piece,new_pos,extra_info) not in self.get_valid_moves():
            print("Invalid Move, You Lose")
            return ('lost',self.turn)

        if self.turn == 1:
            for p in self.player_1_pieces:
                if p==piece:
                    p.pos = new_pos
                    if extra_info==True:
                        p.dead = True
                    pieces_left = [item for item in self.player_1_pieces if item.dead == False]
                    if len(pieces_left)==0:
                        return ('lost',2)
            self.turn = 2

        elif self.turn == 2:
            for p in self.player_2_pieces:
                if p==piece:
                    p.pos = new_pos
                    if extra_info==True:
                        p.dead = True
                    pieces_left = [item for item in self.player_2_pieces if item.dead == False]
                    if len(pieces_left)==0:
                        return ('lost',1)
            self.turn = 1



        if len(self.get_valid_moves()) == 0:
            # Other oppoment is blocked by this move
            print('Blocked other player, You Lose')
            if self.turn == 1:
                return ('lost', 2)
            elif self.turn == 2:
                return ('lost', 1)

        # If normal play continues
        return ('game continues', None)




    def get_valid_moves(self):
        '''
        list of valid moves. Does not check if a move blocks other player. You must check it yourself
        :return: list( (piece,new_position,BoardLeavingMove) )
        '''

        board_matrix,turn = self.get_board_config()
        valid_moves = [] # A move is a tupple of the form (Piece,(new_position_tuple),piece_will_leave_board)
        if self.turn == 1:
            for piece in self.player_1_pieces:
                pos = piece.pos
                if piece.dead == False:
                    forward_move = (pos[0],pos[1]+1) # towards right for player_1
                    if forward_move[1] < self.size:
                        if board_matrix[forward_move] == 0:
                            # if new position is unoccupied and piece doesnt jump off the board
                            valid_moves.append((piece,forward_move,False))
                    elif forward_move[1] == self.size:
                        # Piece can leave the board
                        valid_moves.append((piece,forward_move,True))

                    sideways_left = (pos[0]-1,pos[1])
                    if sideways_left[0] != -1:
                        if board_matrix[sideways_left] == 0 and sideways_left != (self.size-1,0):
                            # Piece doesnt go to bottom left corner, doesnt leave board and moves on empty block
                            valid_moves.append((piece,sideways_left,False))

                    sideways_right = (pos[0]+1,pos[1])
                    if sideways_right[0] != self.size:
                        if sideways_right != (self.size-1,0) and board_matrix[sideways_right] == 0:
                            # Piece doesnt go to bottom, doesnt leave board left corner and moves on empty block
                            valid_moves.append((piece,sideways_right,False))

        elif self.turn == 2:
            for piece in self.player_2_pieces:
                pos = piece.pos
                if piece.dead == False:

                    forward_move = (pos[0]-1,pos[1]) # towards up for player_2
                    if forward_move[0] != -1:
                        if board_matrix[forward_move] == 0:
                            # if new position is unoccupied and piece doesnt jump off the board
                            valid_moves.append((piece,forward_move,False))
                    elif forward_move[0] == -1:
                        # Piece can leave the board
                        valid_moves.append((piece,forward_move,True))

                    sideways_left = (pos[0],pos[1]-1)
                    if sideways_left[1] != -1:
                        if board_matrix[sideways_left] == 0 and sideways_left != (self.size-1,0):
                            # Piece doesnt go to bottom left corner, doesnt leave board and moves on empty block
                            valid_moves.append((piece,sideways_left,False))

                    sideways_right = (pos[0],pos[1]+1)
                    if sideways_right[1] != self.size:
                        if sideways_right != (self.size-1,0) and board_matrix[sideways_right] == 0:
                            # Piece doesnt go to bottom, doesnt leave board left corner and moves on empty block
                            valid_moves.append((piece,sideways_right,False))
        return valid_moves
