# Crie um classe chamada pessoa com os atributos: nome, idade, peso, gênero

class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

# Uso da classe Pessoa
pessoa1 = Pessoa('Jão Grilo', 33, 60, 'Masculino')
print('Nome', pessoa1.nome)
print('Nome', pessoa1.idade)
print('Nome', pessoa1.peso)
print('Nome', pessoa1.genero)