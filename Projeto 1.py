
#  Projeto 1 de Orientacao a objetos
# Pseudocodigo

# Inicio
# Criar a classe quadrado
# definir os atributos da classe quadrado
class quadrado():
  def __init__(self,lado):
      self.lado = lado


# definir os metodos da classe quadrado

def calcularArea(self):
  return ( self.lado**2)

# Criar uma instancia da classe quadrado com um lado de 5
quadrado = quadrado(5)

# Calcular a area do quadrado
area = quadrado.calcularArea()

# Imprimir a figura do quadrado
for _ in range(quadrado.lado):
    print('* ' * quadrado.lado)

print("Área do quadrado:", area)



# Criar a classe retangulo
class retangulo():
#definir os atributos da classe retangulo

# definir os metodos da classe retangulo
 def __init__(self, comprimento, largura):
  self.comprimento = comprimento
  self.largura = largura


def cacularArea(self):
 self.area = ( self.comprimento*self.largura)

retangulo = retangulo(4, 6)

for i in range(retangulo.largura):
    for j in range(retangulo.comprimento):
        print('* ', end='')  
    print()  

# Imprimir a area
print("Área do retângulo:", area)
# Criar a classe ponto

class ponto():
  # definir os atributos da classe ponto como uma coordenada (x,y) e raio como um numero positivo
  def __init__(self,x,y):
   self.x = x
   self.y = y

# definir os metodos da classe ponto
  def mover(self, delta_x, delta_y):
    self.x += delta_x
    self.y += delta_y 

# Criar uma instância de Ponto
ponto = ponto(3, 5)  # Por exemplo, um ponto com coordenadas (3, 5)

# Imprimir a figura do ponto
print("Coordenadas do ponto:", ponto.x, ponto.y)


# Criar a classe circulo
#utilizar o conceito de heranca e herdar os atributos e metodos da classe ponto

class circulo(ponto):
  def __init__(self, x, y, raio):
        super().__init__(x, y)  
        self.raio = raio

  def mover(self, delta_x, delta_y):
    self.x += delta_x
    self.y += delta_y 

# Criar uma instancia de Circulo
circulo = circulo(3, 5, 2)  # Por exemplo, um circulo com centro (3, 5) e raio 2

# Imprimir a figura do circulo
print("Centro do circulo (coordenadas x, y):", circulo.x, circulo.y)
print("Raio do circulo:", circulo.raio) 
