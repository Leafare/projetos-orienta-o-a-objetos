from mylibraries.Projeto1 import *
# definindo as operações de visualização das formas 

def visualizar_formas(formas):
    for forma in formas:
        forma.visualizar()


# criando instancia das formas

quadrado = Quadrado(5)
retangulo = Retangulo(4, 6)
ponto = Ponto(3, 5)
circulo = Circulo(3, 5, 2)

#adicionando as formas a uma lista
formas = [quadrado, retangulo, ponto, circulo]

visualizar_formas(formas)


## Definindo operações de inserção e remoção das formas

class interacao_formas:
    def __init__ (self):
        self.formas = []

# inserção
    def inserir_formas(self, forma):
        self.append.formas(formas)

# remoção
    def remover_formas(self, forma):
        if formas in self.formas:
            self.formas.remove(formas)

    def remover_forma_por_numero(self, numero):
        formas_a_remover = [forma for forma in self.formas if forma.numero == numero]
        for formas in formas_a_remover:
            self.remover_forma(forma)

    def listar_formas(self):
        return self.formas
    
# criando instancias das formas com numeros

quadrado = Quadrado(5, "1")
retangulo = Retangulo(4, 6, "2")
ponto = Ponto(3, 5, "3")
circulo = Circulo(3, 5, 2, "4")
    
# criando um gerenciador de formas 
gerenciador = InteracaoFormas()

# adicionando as formas ao gerenciador

gerenciador.adicionar_forma(quadrado)
gerenciador.adicionar_forma(retangulo)
gerenciador.adicionar_forma(ponto)
gerenciador.adicionar_forma(circulo)

gerenciador.remover_formmas_por_numero()

# listando todas as formas que restaram
formas = gerenciador.listar_formas()

# visualizando as formas restantes
visualizar_formas(formas)


