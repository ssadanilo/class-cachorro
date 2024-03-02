# Crie um classe chamada cachorro com os atributos: nome, raça, idade

class Cachorro:
    def  __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

# Uso da classe Cachorro
cachorro1 = Cachorro('Furico', 'Vira-Lata', 3)
print('Nome', cachorro1.nome)
print('Raça', cachorro1.raca)
print('Idade', cachorro1.idade)