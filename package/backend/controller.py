import pygame
import sys
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from frontend.viewers import GameView
from frontend.model import initialize_game, check_victory, consultar_ranking

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def game_loop(view):
    matrix_colors = [[(0, 0, 255)] * view.cols for _ in range(view.rows)]  

    while True:
        handle_input()
        view.draw_matrix(matrix_colors)

        
        if check_victory():
            ranking = consultar_ranking()
            view.show_victory_screen(ranking)

            pygame.time.wait(20000) 
            break

if __name__ == "__main__":
    WIDTH, HEIGHT = 800, 600
    CELL_SIZE = 50
    ROWS, COLS = 5, 10

    game_view = GameView(WIDTH, HEIGHT, CELL_SIZE, ROWS, COLS)
    initialize_game()
    game_loop(game_view)
