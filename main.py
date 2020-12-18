import pygame, sys, time
import helpers

pygame.init()

# game board
size = WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

BROWN = (195, 155, 119)
DARK_BROWN = (128, 96, 77)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (150, 0, 24)

# game pieces
black_piece = pygame.image.load("icons_and_fonts/black_piece.png")
white_piece = pygame.image.load("icons_and_fonts/white_piece.png")


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers")

title_font = pygame.font.Font("icons_and_fonts/Quicksand-VariableFont_wght.ttf", 64)
play_as_font = pygame.font.Font("icons_and_fonts/Quicksand-VariableFont_wght.ttf", 42)

user = None
# board = checkers.initial_state()
ai_turn = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    screen.fill(BROWN)
    for row in range(ROWS):
        for col in range(row % 2, ROWS, 2):
            pygame.draw.rect(screen, DARK_BROWN, (row * SQUARE_SIZE, col * SQUARE_SIZE, 
                            SQUARE_SIZE, SQUARE_SIZE))
    # main title screen
    if user is None:
        title = title_font.render("Checkers", True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((WIDTH / 2), (HEIGHT / 3))
        screen.blit(title, titleRect)
        
        # Play as white
        play_white_button = pygame.Rect((WIDTH / 8), (HEIGHT / 2), (WIDTH / 4), 50)
        play_white = play_as_font.render("White", True, BLACK)
        play_white_rect = play_white.get_rect()
        play_white_rect.center = play_white_button.center
        pygame.draw.rect(screen, WHITE, play_white_button)
        screen.blit(play_white, play_white_rect)

        # Play as black
        play_black_button = pygame.Rect(5 * (WIDTH / 8), (HEIGHT / 2), (WIDTH / 4), 50)
        play_black = play_as_font.render("Black", True, WHITE)
        play_black_rect = play_black.get_rect()
        play_black_rect.center = play_black_button.center
        pygame.draw.rect(screen, BLACK, play_black_button)
        screen.blit(play_black, play_black_rect)
                        
        # need to create click events
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse_pos = pygame.mouse.get_pos()
            if play_black_button.collidepoint(mouse_pos):
                time.sleep(0.2)
                user = helpers.black
            elif play_white_button.collidepoint(mouse_pos):
                time.sleep(0.2)
                user = helpers.white
            
        pygame.display.update()