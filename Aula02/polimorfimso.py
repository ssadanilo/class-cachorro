class Animal():
  def __init__(self, nome):
    self.nome = nome

  def fazerSom(self):
    pass

class Cachorro(Animal):
  def fazerSom(self):
    return 'Au Au!'

class Gato(Animal):
  def fazerSom(self):
    return 'Miau!'
  
class Petista(Animal):
    def fazerSom(self):
      return 'Pruuu!'

def fazerAnimalFalar(Cachorro):
  return Cachorro.fazerSom()

def fazerAnimalFalar(Gato):
  return Gato.fazerSom()

def fazerAnimalFalar(Petista):
  return Petista.fazerSom()

ypioca = Cachorro('Ypioca')
fuleiro = Gato('Fuleiro')
silva = Petista('Silva')

print(ypioca.nome, 'faz som', ypioca.fazerSom())
print(fuleiro.nome, 'faz som', fuleiro.fazerSom())
print(silva.nome, 'faz som', silva.fazerSom())