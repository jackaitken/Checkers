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

    h.screen.fill(h.WHITE)

    if user is None:
        title = title_font.render("Checkers", True, h.BLACK)
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
        play_black = play_as_font.render("Black", True, h.BLACK)
        play_black_rect = play_black.get_rect()
        play_black_rect.center = play_black_button.center
        pygame.draw.rect(h.screen, h.WHITE, play_black_button)
        h.screen.blit(play_black, play_black_rect)
                        
        # handles user choice
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse_pos = pygame.mouse.get_pos()
            if play_black_button.collidepoint(mouse_pos):
                user = h.B
            elif play_white_button.collidepoint(mouse_pos):
                user = h.W
                ai_turn = True
    else:      
        h.screen.fill(h.BLACK)  
        # draw board
        tile_size = 90
        tile_origin = (h.WIDTH / 4.5 - (1.5 * tile_size),
                       h.HEIGHT / 4.5 - (1.5 * tile_size))
        tiles = []
        for i in range(8):
            row = []
            for j in range(8):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(h.screen, h.WHITE, rect, 3)

                if board[i][j] != h.EMPTY:
                    move = title_font.render(board[i][j], True, h.WHITE)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    h.screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)


        if ai_turn:
            pass

        #get row and column of click event
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            for i in range(8):
                for j in range(8):
                    if (board[i][j] == user and tiles[i][j].collidepoint(mouse)):
                        available_actions = h.actions(board,j, i, user)
                        print(available_actions)

    pygame.display.update()