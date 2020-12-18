import pygame
from checkers.main import BROWN, ROWS, DARK_BROWN, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0

    def draw_rects(self, screen):
        screen.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(screen, DARK_BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, 
                                                        SQUARE_SIZE, SQUARE_SIZE))