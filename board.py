import pygame, sys, time
import checkers

pygame.init()

# game board
BROWN = (195, 155, 119)
DARK_BROWN = (128, 96, 77)
WHITE = (255, 255, 255)

# game pieces
black_piece = pygame.image.load("icons/black_piece.png")
white_piece = pygame.image.load("icons/white_piece.png")

# initializes game board
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers")

title_font = pygame.font.Font("Quicksand-VariableFont_wght.ttf", 64)

user = None
# board = checkers.initial_state()
ai_turn = False

# main game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill((DARK_BROWN))
    pygame.display.update()

    # main title screen
    if user is None:
        title = title_font.render("Checkers", True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), (height / 3))
        screen.blit(title, titleRect)
        pygame.display.update()
