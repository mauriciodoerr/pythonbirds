class Pessoa:
    def __init__(self, *filhos, nome: str = None, idade: int = 0):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}, você possui {self.idade} anos de idade.'


if __name__ == '__main__':
    p = Pessoa(nome='Teste')
    print(p.cumprimentar())
    p.nome = 'Teste2'
    print(p.cumprimentar())

    p2 = Pessoa(nome='TesteIdade', idade=10)
    print(p2.cumprimentar())

    p3 = Pessoa(nome='Pessoa Filho')
    p4 = Pessoa(p3, nome='Pessoa Pai')

    for filho in p4.filhos:
        print(filho.nome)

    # Criando atributo dinâmico
    p.sobrenome = 'Sobrenome'
    print(p.__dict__)
    print(p2.__dict__)

    # Removendo atributo dinâmico
    del p.sobrenome
    print(p.__dict__)
