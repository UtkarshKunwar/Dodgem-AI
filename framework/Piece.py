'''
    File name: Piece.py
    Author: Siddhant Kumar
    Email: saytosid@gmail.com
    Date created: 1 Oct 2017
    Date last modified: 1 Oct 2017
    Python Version: 3.0
'''
class Piece:
    def __init__(self,color='black',position=(-1,-1)):
        '''
        :param color: color of the piece, by default black
        :param position: position of piece
        '''

        self.color = color
        self.pos = position
        self.dead = False
