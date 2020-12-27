import pygame, sys, time
import helpers as h
import math

pygame.init()

# game pieces
black_piece = pygame.image.load("icons_and_fonts/black_piece.png")
white_piece = pygame.image.load("icons_and_fonts/white_piece.png")

pygame.display.set_caption("Checkers")

title_font = pygame.font.Font("icons_and_fonts/Quicksand-VariableFont_wght.ttf", 64)
play_as_font = pygame.font.Font("icons_and_fonts/Quicksand-VariableFont_wght.ttf", 42)

user = None
board = h.initial_board()
ai_turn = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    h.fill_empty_board()
    
    if user is None:
        title = title_font.render("Checkers", True, h.WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((h.WIDTH / 2), (h.HEIGHT / 3))
        h.screen.blit(title, titleRect)
        
        # Play as white
        play_white_button = pygame.Rect((h.WIDTH / 8), (h.HEIGHT / 2), (h.WIDTH / 4), 50)
        play_white = play_as_font.render("White", True, h.BLACK)
        play_white_rect = play_white.get_rect()
        play_white_rect.center = play_white_button.center
        pygame.draw.rect(h.screen, h.WHITE, play_white_button)
        h.screen.blit(play_white, play_white_rect)

        # Play as black
        play_black_button = pygame.Rect(5 * (h.WIDTH / 8), (h.HEIGHT / 2), (h.WIDTH / 4), 50)
        play_black = play_as_font.render("Black", True, h.WHITE)
        play_black_rect = play_black.get_rect()
        play_black_rect.center = play_black_button.center
        pygame.draw.rect(h.screen, h.BLACK, play_black_button)
        h.screen.blit(play_black, play_black_rect)
                        
        # handles user choice
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse_pos = pygame.mouse.get_pos()
            if play_black_button.collidepoint(mouse_pos):
                user = h.black
            elif play_white_button.collidepoint(mouse_pos):
                user = h.white
                ai_turn = True
    else:
        # after user is chosen, draw board
        h.fill_empty_board()
        
        # draw black pieces
        y_coord = -50
        for row in range(2):
            x_coord = 50
            y_coord += 100
            for col in range(8):
                if row == 0 and col % 2 == 1:
                    pygame.draw.circle(h.screen, h.BLACK,(x_coord, y_coord), 40)
                    x_coord += 100
                elif row == 1 and col % 2 == 0:
                    pygame.draw.circle(h.screen, h.BLACK, (x_coord, y_coord), 40)
                    x_coord += 100
                else:
                    x_coord += 100

        # draw white pieces
        y_coord = 550
        for row in range(2):
            x_coord = 50
            y_coord += 100
            for col in range(8):
                if row == 0 and col % 2 == 1:
                    pygame.draw.circle(h.screen, h.WHITE, (x_coord, y_coord), 40)
                    x_coord += 100
                elif row == 1 and col % 2 == 0:
                    pygame.draw.circle(h.screen, h.WHITE, (x_coord, y_coord), 40)
                    x_coord += 100
                else:
                    x_coord += 100

        if ai_turn:
            pass

        #get row and column of click event
        else:
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse_pos = pygame.mouse.get_pos()
                col = math.trunc(mouse_pos[0] / 100)
                row = math.trunc(mouse_pos[1] / 100)
                col_row = (col, row)
                print(col_row)

                if board[row][col] == user:
                    first_click = True
                    available_actions = h.actions(board, col, row, user)
                    print(available_actions)

                    #shows possible legal moves
                    for move in available_actions:
                        pygame.draw.rect(
                            h.screen, h.RED, (move[1] * h.SQUARE_SIZE, move[0] * h.SQUARE_SIZE, 
                            h.SQUARE_SIZE, h.SQUARE_SIZE)
                        )
    pygame.display.update()