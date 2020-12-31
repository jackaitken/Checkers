import pygame

SCREEN_WIDTH = 800
screen = pygame.display.set_mode

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BROWN = (255, 213, 154)
LIGHT_BROWN = (213, 193, 170)
EMPTY = None
INVALID = None
white = "white"
black = "black"

    
def initial_board():
    """
    Board visualization
    """
    return [[INVALID, white, INVALID, white, INVALID, white, INVALID, white],
            [white, INVALID, white, INVALID, white, INVALID, white, INVALID],
            [INVALID, white, INVALID, white, INVALID, white, INVALID, white],
            [EMPTY, INVALID, EMPTY, INVALID, EMPTY, INVALID, EMPTY, INVALID],
            [INVALID, EMPTY, INVALID, EMPTY, INVALID, EMPTY, INVALID, EMPTY],
            [black, INVALID, black, INVALID, black, INVALID, black, INVALID],
            [INVALID, black, INVALID, black, INVALID, black, INVALID, black],
            [black, INVALID, black, INVALID, black, INVALID, black, INVALID]]

class Square:
    def __init__(self, row, col, width, total_rows):
        """
        initizalizes attributes for a single game square
        """
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = color
        self.width = width
        self.total_rows = total_rows

    

    def get_position(self):
        return self.row, self.col

    def player(self):
        """
        Returns current player turn
        """
        pass

    def is_empty(self):
        """
        Returns true if square is empty
        """
        pass

    def actions(self, board):
        """
        Returns available actions
        """
        pass

    def is_king(self):
        """
        Returns true if piece is king
        """
        pass

    def heuristic(self):
        """
        Simple heuristic based on the difference in total pieces
        """
        pass

    def terminal(self):
        """
        Returns true if game is in terminal state
        """
        pass

    def capture(self):
        """
        Returns true if capture event is possible
        """
        pass

    def minimax(self):
        """
        depth-limited minimax algorithm
        """
        pass

    def max_value(self):
        """
        Used by minimax
        """
        pass

    def min_value(self):
        """
        Used by minimax
        """
        pass

