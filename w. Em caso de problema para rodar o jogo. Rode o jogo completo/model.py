from datetime import datetime

# Caminho do arquivo de estatísticas
ARQUIVO_ESTATISTICAS = "estatisticas.txt"


def registrar_estatisticas(nome_usuario, tempo_total, quantidade_acertos):
    data_jogo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"{nome_usuario},{-tempo_total},{quantidade_acertos},{data_jogo}\n"

    # Tenta abrir o arquivo, se não existir, cria um novo
    with open(ARQUIVO_ESTATISTICAS, "a") as arquivo:
        arquivo.write(linha)


# Lê o arquivo de estatísticas e retorna uma lista de entradas
def ler_estatisticas():
    try:
        with open(ARQUIVO_ESTATISTICAS, "r") as arquivo:
            estatisticas = [linha.strip().split(",") for linha in arquivo]
        return estatisticas
    except FileNotFoundError:
        return []  


def gerar_ranking():
    estatisticas = ler_estatisticas()
    if not estatisticas:
        return "Ainda não há estatísticas para mostrar."


    estatisticas.sort(key=lambda x: float(x[1]))  # Ordena pelo tempo total
    return estatisticas


def imprimir_ranking():
    ranking = gerar_ranking()
    if isinstance(ranking, str):
        print(ranking)
    else:
        for posicao, (nome, tempo, acertos, data) in enumerate(ranking, start=1):
            print(f"{posicao}. {nome} - Tempo: {tempo}s, Acertos: {acertos}, Data: {data}")
def consultar_ranking():
    return gerar_ranking()