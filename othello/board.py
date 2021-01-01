import pygame
from .constants import BLACK, WHITE, GREEN, ROWS, COLS, SQUARE_SIZE
from .piece import Piece

pygame.init()

class Board:
    def __init__(self):
        self.game_field = [[0 for _row in range(ROWS)] for _col in range(COLS)]
        self.create_init_pieces()
    
    #piece is the stone of a player
    def add_piece(self, row, col, player_color):
        if player_color == 0:
            self.game_field[row][col] = 0
        else:
            self.game_field[row][col] = Piece(row, col, player_color)
    
    def get_piece(self, row, col):
        return self.game_field[row][col]
    
    def draw_board(self, window):
        background = pygame.Surface((600,600))
        background.fill(GREEN)
        # window.fill(GREEN)
        window.blit(background, (0,75))
        for row in range(ROWS):
            for col in range(1,COLS+1):
                pos = (row*SQUARE_SIZE, col* + 75, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(window, BLACK, pos, 1)

    def create_init_pieces(self):
        self.game_field[3][3] = Piece(3, 3, WHITE)
        self.game_field[4][4] = Piece(4, 4, WHITE)
        self.game_field[3][4] = Piece(3, 4, BLACK)
        self.game_field[4][3] = Piece(4, 3, BLACK)
    #draw board and pieces
    def draw(self, window):
        self.draw_board(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.game_field[row][col]
                if piece != 0:
                    piece.draw_piece(window)
    
  
    def get_pieces(self, player):
        """Get the coordinates (x,y) for all pieces on the board of a player"""
        pieces_cord = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.game_field[row][col]!= 0 and self.game_field[row][col].color == player:
                    pieces_cord.append([row, col])
        return pieces_cord

    #TO DO: should be updated
    def count_pieces(self):
        black_pieces = []
        white_pieces = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.game_field[row][col]!= 0 and self.game_field[row][col].color == BLACK:
                    black_pieces.append(self.game_field[row][col])
                if self.game_field[row][col]!= 0 and self.game_field[row][col].color == WHITE:
                    white_pieces.append(self.game_field[row][col])
        return len(black_pieces), len(white_pieces)
                
        