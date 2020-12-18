import pygame
import copy
import math

black = "black"
white = "white"
EMPTY = None

def initial_board():
    return [[white, white, white, white, white, white, white, white]
            [white, white, white, white, white, white, white, white]
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
            [black, black, black, black, black, black, black, black]
            [black, black, black, black, black, black, black, black]]

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

def actions(board):
    """
    Returns set of available actions
    """
    actions_set = set()

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

