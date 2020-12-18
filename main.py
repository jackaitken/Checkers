import pygame, sys, time, constants
from checkers_lib.constants import size

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers")

title_font = pygame.font.Font("Quicksand-VariableFont_wght.ttf", 64)
play_as_font = pygame.font.Font("Quicksand-VariableFont_wght.ttf", 42)

user = None
# board = checkers.initial_state()
ai_turn = False
FPS = 60

def main():
    # main game loop
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        screen.fill(DARK_BROWN)

        # main title screen
        if user is None:
            title = title_font.render("Checkers", True, WHITE)
            titleRect = title.get_rect()
            titleRect.center = ((WIDTH / 2), (HEIGHT / 3))
            screen.blit(title, titleRect)
            
            # Play as white
            play_white_button = pygame.Rect((WIDTH / 8), (HEIGHT / 2), (WIDTH / 4), 50)
            play_white = play_as_font.render("White", True, WHITE)
            play_white_rect = play_white.get_rect()
            play_white_rect.center = play_white_button.center
            pygame.draw.rect(screen, DARK_BROWN, play_white_button)
            screen.blit(play_white, play_white_rect)

            # Play as black
            play_black_button = pygame.Rect(5 * (WIDTH / 8), (HEIGHT / 2), (WIDTH / 4), 50)
            play_black = play_as_font.render("Black", True, WHITE)
            play_black_rect = play_black.get_rect()
            play_black_rect.center = play_black_button.center
            pygame.draw.rect(screen, DARK_BROWN, play_black_button)
            screen.blit(play_black, play_black_rect)
                            
            # need to create click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('click')
                
            pygame.display.update()
    
main()