class Pessoa:
    # Atributos de classe
    olhos = 2

    # Atributos de instância
    def __init__(self, *filhos, nome: str = None, idade: int = 0):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}, você possui {self.idade} anos de idade.'

    # Acesso de forma estática
    @staticmethod
    def metodo_estatico():
        return 42

    # Acesso de forma estática e acessa os atributos da classe
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'Classe {cls} - {cls.olhos}'


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

    print(p.metodo_estatico())
    print(Pessoa.metodo_estatico())

    # Mesmo alterando o atributo de classe, ao acessar via classmethod apresente o atributo de classe e não de instância
    p.olhos = 3
    print(p.__dict__)
    print(p.nome_e_atributos_de_classe())
    print(Pessoa.nome_e_atributos_de_classe())
