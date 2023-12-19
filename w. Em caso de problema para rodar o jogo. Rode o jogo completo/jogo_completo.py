import pygame
import sys
import model
import shared_data

# Inicializar o Pygame
pygame.init()

# Função para desenhar botões
# Definir constantes
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 50
ROWS, COLS = 5, 10

# Calcular a posição inicial para centralizar a matriz
start_x = (WIDTH - COLS * CELL_SIZE) // 2
start_y = (HEIGHT - ROWS * CELL_SIZE) // 2

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def draw_textbox(screen, text, position, size):
    font = pygame.font.Font(None, 36)
    textbox_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, WHITE, textbox_rect, 2)
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (position[0] + 5, position[1] + 5))
    return textbox_rect

def draw_button(screen, text, position, size):
    font = pygame.font.Font(None, 36)
    text_render = font.render(text, True, (0, 255, 0))
    button_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, (0, 0, 0), button_rect)
    text_rect = text_render.get_rect(center=button_rect.center)
    screen.blit(text_render, text_rect)
    return button_rect

# Tela de boas-vindas
def welcome_screen(screen, user_text):
    screen.fill(BLACK)
    welcome_font = pygame.font.Font(None, 50)
    welcome_text = welcome_font.render("BEM-VINDO AO TERMINAL DO BALÃO!", True, WHITE)
    screen.blit(welcome_text, (WIDTH // 2 - welcome_text.get_width() // 2, HEIGHT // 4))

    # Adicionando a primeira frase nova
    adventure_font = pygame.font.Font(None, 30)
    adventure_text = adventure_font.render("UMA AVENTURA DIVERTIDA", True, WHITE)
    screen.blit(adventure_text, (WIDTH // 2 - adventure_text.get_width() // 2, HEIGHT // 4 + 60))

    # Adicionando a segunda frase nova
    challenge_font = pygame.font.Font(None, 30)
    challenge_text = challenge_font.render("**RESOLVA AS EQUAÇÕES NO MENOR TEMPO**", True, WHITE)
    screen.blit(challenge_text, (WIDTH // 2 - challenge_text.get_width() // 2, HEIGHT // 4 + 100))

    # Desenhar botões
    start_button = draw_button(screen, "Modo Anônimo", (WIDTH // 2 - 100, HEIGHT // 2), (200, 50))
    register_button = draw_button(screen, "Cadastrar Player", (WIDTH // 2 - 100, HEIGHT // 2 + 60), (200, 50))

    # Desenhar a caixa de texto
    textbox = draw_textbox(screen, user_text, (WIDTH // 2 - 100, HEIGHT // 2 + 120), (200, 40))
    return start_button, register_button, textbox



# Definir constantes
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 50
ROWS, COLS = 5, 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Criar a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TERMINAL DO BALÃO")

# Estado do jogo
game_started = False
user_text = ''

# Tela de boas-vindas
while not game_started:
    start_button, register_button, textbox = welcome_screen(screen, user_text)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game_started = True
            elif register_button.collidepoint(event.pos):
                model.nome_do_jogador = user_text
                game_started = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    pygame.display.flip()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TERMINAL DO BALÃO")

# fonte para os números
font = pygame.font.Font(None, 36)

# Função para gerar expressões
def generate_expression():
    return [
        "(20 + 20) - (9 + 9)",
        "(30 - 30) + (60 - 30)",
        "(20 - 28) + 90",
        "(70 - 7) + (30 - 5) - (9)",
        "(13 ** 2)"
    ]

# dicionário associando linhas a expressões
# janela do jogo
line_expressions = {i: generate_expression()[i-1] for i in range(1, ROWS + 1)}

# Dicionário para associar linhas a letras
line_letters = {
    1: 'B',
    2: 'A',
    3: 'L',
    4: 'Ã',
    5: 'O'
}

# Lista para armazenar letras coletadas
collected_letters = []

# Dicionário para armazenar as respostas do jogador
player_answers = {i: "" for i in range(1, ROWS + 1)}

# Variável para armazenar a escolha do jogador
player_choice = None

# Distância entre a matriz e a área de entrada de texto
text_input_distance = 20

# Altura da caixa de letras coletadas
collected_box_height = 50

# Inicializar a entrada de texto
input_font = pygame.font.Font(None, 28)
input_text = ""

# Inicializar a variável de mensagem
message_text = ""

# Rodada atual do jogador
current_round = 1


# Função para reiniciar o jogo
def reset_game():
    global collected_letters, player_choice, input_text, message_text, current_round
    collected_letters = []
    player_choice = None
    input_text = ""
    message_text = "O jogo foi reiniciado"
    current_round = 1  # Reiniciar a rodada
    for i in range(1, ROWS + 1):
        player_answers[i] = ""

# Função para verificar se o jogador venceu
def check_victory():
    return collected_letters == ['B', 'A', 'L', 'Ã', 'O']

# Inicializar a matriz com a cor azul
matrix_colors = [[BLUE] * COLS for _ in range(ROWS)]

# Loop principal do jogo

while True:
    if game_started:

        # Inicializa o temporizador no início de cada tentativa de jogo
        tempo_inicial = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo do mouse
                if message_text.startswith("Resposta incorreta"):
                    # Sair do jogo se houver uma mensagem de resposta incorreta
                    pygame.quit()
                    sys.exit()
                for row in range(ROWS):
                    for col in range(COLS):
                        rect = pygame.Rect(start_x + col * CELL_SIZE, start_y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        if rect.collidepoint(event.pos):
                            # Verificar a restrição de escolha com base na rodada
                            valid_numbers = list(range((current_round - 1) * COLS + 1, current_round * COLS + 1))
                            if (row + 1) in valid_numbers:
                                player_choice = row + 1
                                input_text = ""  # Limpar o texto ao mudar de expressão
                                matrix_colors[row][col] = RED  # Mudar a cor para vermelho
                                print("Jogador escolheu linha:", player_choice)
                                print("Expressão correspondente:", line_expressions[player_choice])

            elif event.type == pygame.KEYDOWN and player_choice is not None:
                # Inicializar a variável de mensagem antes do bloco if
                message_text = ""

                if event.key == pygame.K_RETURN:
                    # O jogador pressionou Enter, salvar a resposta
                    player_answers[player_choice] = input_text

                    # Verificar se a resposta está correta e atribuir a letra correspondente
                    correct_answer = eval(line_expressions[player_choice])
                    if str(correct_answer) == player_answers[player_choice]:
                        letter = line_letters[player_choice]
                        if letter not in collected_letters:
                            collected_letters.append(letter)
                            message_text = f"Resposta correta! Letra coletada: {letter}"
                    else:
                        message_text = "Resposta incorreta! Pressione 'R' para reiniciar, \n'Q' para sair ou 'ESPAÇO' para jogar novamente."

                elif event.key == pygame.K_BACKSPACE:
                    # O jogador pressionou Backspace, remover um caractere
                    input_text = input_text[:-1]

                elif event.key == pygame.K_q:
                    # O jogador pressionou 'Q', sair do jogo
                    pygame.quit()
                    sys.exit()

                else:
                    # Adicionar o caractere pressionado à entrada de texto
                    input_text += event.unicode

    if check_victory():
        # Calcula o tempo total gasto pelo jogador
        tempo_final = (pygame.time.get_ticks() - tempo_inicial) / 1000  # Tempo em segundos
        tempo_total = (tempo_final - tempo_inicial) / 1000  # Convertendo milissegundos para segundos

        # Conta a quantidade de acertos
        quantidade_acertos = len(collected_letters)

        # Registrar estatísticas
        model.registrar_estatisticas(shared_data.nome_do_jogador, tempo_total, quantidade_acertos)
        # Registrar estatísticas
        '''statistics.registrar_estatisticas(shared_data.nome_do_jogador, tempo_final, quantidade_acertos)'''
        # Aqui você pode colocar o restante do código que lida com a situação de vitória

        # ... [código para registrar estatísticas] ...

        # Obter o ranking
        ranking = model.consultar_ranking()

        # Exibir o ranking na tela
        screen.fill(BLACK)  # Limpar a tela

        # Configuração de fonte para exibição do ranking
        ranking_font = pygame.font.Font(None, 28)

        # Coordenadas iniciais para exibir o ranking
        x = 50
        y = 50

        # Configuração de fonte para o título
        titulo_font = pygame.font.Font(None, 36)  # Fonte maior para o título
        titulo_surface = titulo_font.render("RANKING DE USUÁRIOS", True, RED)
        screen.blit(titulo_surface, (x, y))  # Desenhar o título na tela
        y += 50  # Aumentar o espaçamento após o título

        # Exibir cada entrada do ranking
        for posicao, (nome, tempo, acertos, data) in enumerate(ranking, start=1):
            linha_ranking = f"{posicao}. {nome} - Tempo: {tempo}s, Acertos: {acertos}, Data: {data}"
            ranking_surface = ranking_font.render(linha_ranking, True, WHITE)
            screen.blit(ranking_surface, (x, y))
            y += 30  # Aumentar y para a próxima linha

        pygame.display.flip()  # Atualizar a tela

        # Aguardar algum tempo ou um evento (por exemplo, uma tecla pressionada) para sair
        pygame.time.wait(20000)  # Espera 10 segundos antes de sair

        break  # Sair do loop do jogo

    # Limpar a tela
    screen.fill(BLACK)

    # Desenhar a matriz
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.draw.rect(screen, matrix_colors[row][col], (start_x + col * CELL_SIZE, start_y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            number = row * COLS + col + 1
            text_surface = font.render(str(number), True, WHITE)
            text_rect = text_surface.get_rect(center=(start_x + col * CELL_SIZE + CELL_SIZE // 2, start_y + row * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(text_surface, text_rect)

    # Exibir a expressão correspondente à escolha do jogador
    if player_choice is not None:
        expression_text = font.render(line_expressions[player_choice], True, WHITE)
        screen.blit(expression_text, (start_x, start_y - 80))

        # Exibir área de entrada de texto para a resposta do jogador
        input_rect = pygame.Rect(start_x, start_y + ROWS * CELL_SIZE + text_input_distance, WIDTH - start_x * 2, 30)
        pygame.draw.rect(screen, WHITE, input_rect, 2)

        # Renderizar a entrada de texto
        input_surface = input_font.render(input_text, True, WHITE)
        screen.blit(input_surface, (start_x + 5, start_y + ROWS * CELL_SIZE + text_input_distance + 5))

    # Exibir letras coletadas
    collected_text = ", ".join(collected_letters)
    collected_letters_surface = font.render(f"Letras Coletadas: {collected_text}", True, YELLOW)  # Alterado para amarelo
    screen.blit(collected_letters_surface, (start_x + 5, start_y - collected_box_height + 5))

    # Exibir caixa de letras coletadas
    collected_box_rect = pygame.Rect(start_x, start_y - collected_box_height, WIDTH - start_x * 2, collected_box_height)
    pygame.draw.rect(screen, BLACK, collected_box_rect, 2)

    # Verificar condição de vitória
    if check_victory():
        message_text = "Parabéns! Você venceu o jogo! Pressione 'R' para jogar novamente, 'Q' para sair."
        reset_game()
        player_choice = None  # Limpar a escolha do jogador para evitar múltiplas entradas

    # Exibir mensagens na tela
    message_surface = font.render(message_text, True, WHITE)
    screen.blit(message_surface, (start_x, start_y + ROWS * CELL_SIZE + text_input_distance + 40))

    # Atualizar a tela
    pygame.display.flip()

    # Sair do jogo
pygame.quit()
sys.exit()