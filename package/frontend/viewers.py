import pygame
import model

class GameView:
    def __init__(self, width, height, cell_size, rows, cols):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("TERMINAL DO BALÃO")
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.start_x = (width - cols * cell_size) // 2
        self.start_y = (height - rows * cell_size) // 2
        self.font = pygame.font.Font(None, 36)

    def draw_matrix(self, matrix_colors):
        self.screen.fill((0, 0, 0))  

        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.draw.rect(self.screen, matrix_colors[row][col], (
                    self.start_x + col * self.cell_size, self.start_y + row * self.cell_size, self.cell_size,
                    self.cell_size))
                number = row * self.cols + col + 1
                text_surface = self.font.render(str(number), True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(
                    self.start_x + col * self.cell_size + self.cell_size // 2,
                    self.start_y + row * self.cell_size + self.cell_size // 2))
                self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

    def show_victory_screen(self, ranking):
        self.screen.fill((0, 0, 0))  # Limpar a tela

        x, y = 50, 50
        ranking_font = pygame.font.Font(None, 28)
        titulo_font = pygame.font.Font(None, 36)

        titulo_surface = titulo_font.render("RANKING DE USUÁRIOS", True, (255, 0, 0))
        self.screen.blit(titulo_surface, (x, y))
        y += 50

        for posicao, (nome, tempo, acertos, data) in enumerate(ranking, start=1):
            linha_ranking = f"{posicao}. {nome} - Tempo: {tempo}s, Acertos: {acertos}, Data: {data}"
            ranking_surface = ranking_font.render(linha_ranking, True, (255, 255, 255))
            self.screen.blit(ranking_surface, (x, y))
            y += 30

        pygame.display.flip()
