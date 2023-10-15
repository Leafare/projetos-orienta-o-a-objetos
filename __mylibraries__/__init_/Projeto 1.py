
# Projeto 1 de Orientacao a objetos
# Pseudocodigo

# Inicio
# Criando a classe Quadrado
# definindo os atributos da classe Quadrado
class Quadrado():
    def __init__(self,lado):
        self.lado = lado
# definindo os metodos da classe quadrado
    def calcularArea(self):
        return self.lado**2

# Criando uma instancia da classe Quadrado com um lado de 5
quadrado = Quadrado(5)

# Calculando a area do quadrado
area = quadrado.calcularArea()

# Imprimindo a figura do quadrado
for _ in range(quadrado.lado):
    print('* ' * quadrado.lado)

print("Área do quadrado:", area)



# Criando a classe Retangulo
class Retangulo():
#definindo os atributos da classe Retangulo

# definindo os metodos da classe Retangulo
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura


    def calcularArea(self):
        return self.comprimento*self.largura

retangulo = Retangulo(4, 6)

for i in range(retangulo.largura):
    for j in range(retangulo.comprimento):
        print('* ', end='')  
    print()  

# Imprimindo a area
print("Área do retângulo:", area)
# Criando a classe ponto

class Ponto():
  # definindo os atributos da classe Ponto como uma coordenada (x,y) e raio como um numero positivo
    def __init__(self,x,y):
        self.x = x
        self.y = y

# definindo os metodos da classe Ponto
    def mover(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y 

# Criando uma instância de Ponto
ponto = Ponto(3, 5)  

# Imprimindo a figura do ponto
print("Coordenadas do ponto:", ponto.x, ponto.y)


# Criando a classe circulo
#utilizando o conceito de heranca e herdar os atributos e metodos da classe Ponto

class Circulo(Ponto):
    def __init__(self, x, y, raio):
        super().__init__(x, y)  
        self.raio = raio

# Criando uma instancia de Circulo com centro (3, 5) e raio 2
circulo = Circulo(3, 5, 2)  

# Imprimindo a figura do circulo
print("Centro do circulo (coordenadas x, y):", circulo.x, circulo.y)
print("Raio do circulo:", circulo.raio) 

