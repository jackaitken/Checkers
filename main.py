import pygame
import sys
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

ROWS = SCREEN_HEIGHT // 100
COLS = SCREEN_WIDTH // 100

SQUARE_SIZE = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

white = "white"
black = "black"

EMPTY = None
INVALID = None

surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Checkers")

surface.fill(WHITE)

class Piece:
	def __init__(self, row, col):
		self.row = row
		self.col = col

class Square:
	def __init__(self, row, col):
		self.row = row
		self.col = col

class Board:
	def __init__(self):
		self.board = [
		[INVALID, white, INVALID, white, INVALID, white, INVALID, white],
		[white, INVALID, white, INVALID, white, INVALID, white, INVALID],
		[INVALID, white, INVALID, white, INVALID, white, INVALID, white],
		[EMPTY, INVALID, EMPTY, INVALID, EMPTY, INVALID, EMPTY, INVALID],
		[INVALID, EMPTY, INVALID, EMPTY, INVALID, EMPTY, INVALID, EMPTY],
		[black, INVALID, black, INVALID, black, INVALID, black, INVALID],
		[INVALID, black, INVALID, black, INVALID, black, INVALID, black],
		[black, INVALID, black, INVALID, black, INVALID, black, INVALID]
		]
		self.moves_made = []
		self.black_to_move = True

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	grid = []
	for i in range(ROWS):
		grid.append([])
		for j in range(COLS):
			square = Square((j * SQUARE_SIZE), (i * SQUARE_SIZE))
			grid[i].append((square.col, square.row, SQUARE_SIZE, SQUARE_SIZE)) 

	row_counter = -1
	for row in grid:
		row_counter += 1
		col_counter = 0
		for square in row:
			if col_counter % 2 == 0 and row_counter % 2 == 0:
				pygame.draw.rect(surface, BLACK, square)
				col_counter += 1 

			elif col_counter % 2 == 0 and row_counter % 2 == 1:
				pygame.draw.rect(surface, WHITE, square)
				col_counter += 1 

			elif col_counter % 2 == 1 and row_counter % 2 ==1:
				pygame.draw.rect(surface, BLACK, square) 
				col_counter += 1 

			elif col_counter % 2 == 1 and row_counter % 2 ==0:
				pygame.draw.rect(surface, WHITE, square) 
				col_counter += 1 
				
	pygame.display.update()	