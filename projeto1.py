#  Projeto 1 de Orientação a objetos
# Pseudocódigo

# Início
# Criar a classe quadrado
class quadrado():

# definir os atributos da classe quadrado
#Lado 
# definir os métodos da classe quadrado
 def__init__(self,Lado)
 self.Lado = Lado


def calcularArea(self):
  return ( self.lado**2)



# Criar a classe retangulo
class retangulo():
#definir os atributos da classe retangulo
#cumprimento = 
#largura = 

# definir os métodos da classe retangulo
 def__init__(self, comprimento, largura)
 self.comprimento = comprimento
 self.largura = largura


def_clacularArea(self)
self.area = ( self.comprimento*self.largura)


# Criar a classe ponto

class ponto():
  # definir os atributos da classe ponto como uma coordenada (x,y) e raio como um número positivo
  def__init__(self,x,y)
  self.x = x
  self.y = y

# definir os métodos da classe ponto
  def mover(self, delta_x, delta_y):
    self.x += delta_x
    self.y += delta_y 


# Criar a classe círculo

class circulo(ponto):
  #utilizar o conceito de herança e herdar os atributos e métodos da classe ponto

  def mover(self, delta_x, delta_y):
    self.x += delta_x
    self.y += delta_y 


# Tendo criado as quatro classes principais vamos buscar a interação com o usuário 
print('Olá, seja bem vindo!')
#perguntar ao usuário o tipo de figura que ele gostaria que fosse desenhada e as dimensoes em números inteiros
# representar as figuras e apresentar os métodos ao ususario