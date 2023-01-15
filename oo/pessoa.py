class Pessoa:
    def __init__(self, nome: str = None, idade: int = 0):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}, você possui {self.idade} anos de idade.'


if __name__ == '__main__':
    p = Pessoa('Teste')
    print(p.cumprimentar())
    p.nome = 'Teste2'
    print(p.cumprimentar())

    p2 = Pessoa('TesteIdade', 10)
    print(p2.cumprimentar())

    p3 = Pessoa(idade=30)
    print(p3.cumprimentar())
