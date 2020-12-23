import pygame
import copy
import math

black = "black"
white = "white"
white_king = "white king"
black_king = "black king"

size = WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

BROWN = (195, 155, 119)
DARK_BROWN = (128, 96, 77)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (150, 0, 24)

EMPTY_BLACK = None
EMPTY_WHITE = None

screen = pygame.display.set_mode(size)

def fill_empty_board():
    """
    Returns empty board with no pieces
    """
    screen.fill(BROWN)
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
            pygame.draw.rect(screen, DARK_BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, 
                            SQUARE_SIZE, SQUARE_SIZE))

def initial_board():
    return [[EMPTY_WHITE, black, EMPTY_WHITE, black, EMPTY_WHITE, black, EMPTY_WHITE, black],
            [black, EMPTY_WHITE, black, EMPTY_WHITE, black, EMPTY_WHITE, black, EMPTY_WHITE],
            [EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK],
            [EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE],
            [EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK],
            [EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE, EMPTY_BLACK, EMPTY_WHITE],
            [EMPTY_WHITE, white, EMPTY_WHITE, white, EMPTY_WHITE, white, EMPTY_WHITE, white],
            [white, EMPTY_WHITE, white, EMPTY_WHITE, white, EMPTY_WHITE, white, EMPTY_WHITE]]

def player(board):
    """
    Returns who has next turn
    """
    black_counter = 0
    white_counter = 0
    for i in board:
        for j in i:
            if j == black:
                black_counter += 1
            if j == white:
                white_counter += 1
    
    if black_counter == white_counter:
        return black
    else:
        return white

def actions(board, col, row, user):
    """
    Returns set of available actions
    """
    white_actions_set = set()
    black_actions_set = set()

    # check if piece is not on edge of board
    if col != 0 and col != 7:
        if user is white:
            northwest = (row - 1, col - 1)
            white_actions_set.add(northwest)
            northeast = (row - 1, col + 1)
            white_actions_set.add(northeast)
            return white_actions_set

def result(board, action):
    """
    Returns the board that results from a specific action
    """
    new_board = copy.deepcopy(board)
    action_i = action[0]
    action_j = action[1]

    if new_board[action_i][action_j] == EMPTY:
        new_board[action_i][action_j] = player(board)
        return new_board
    else:
        raise ValueError(action)

def winner(board):
    """
    Returns the winner of the game if there is one
    """

def terminal(board):
    """
    Returns true if game in terminal state
    """

def heuristic(board):
    """
    Defines a current winner and/or loser based on amount of pieces and amount of kings
    """

def capture():
    """
    Handles a capture scenario
    """

def minimax():
    """
    Returns optimal move for user
    """

def max_value():
    """
    Used as a part of minimax algorithm
    """

def min_value():
    """
    Used as a part of minimax algorithm
    """

