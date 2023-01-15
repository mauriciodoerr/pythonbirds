"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1- Motor
2- Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1- Atributo de dado velocidade
2- Método acelerar, que deverá incrementar a velocidade de uma unidade
3- Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1- Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2- Método girar_a_direita
3- Método girar_a_esquerda

  N
O   L
  S

    Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'


class Direcao:
    bussola = [NORTE, LESTE, SUL, OESTE]

    def __init__(self):
        self.valor = 'Norte'

    def girar_a_direita(self):
        virar_para = self.bussola.index(self.valor)
        if virar_para < 3:
            virar_para += 1
        else:
            virar_para = 0
        self.valor = self.bussola[virar_para]

    def girar_a_esquerda(self):
        virar_para = self.bussola.index(self.valor)
        if virar_para > 0:
            virar_para -= 1
        else:
            virar_para = 3
        self.valor = self.bussola[virar_para]


class Carro:
    def __init__(self, direcao=Direcao, motor=Motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        pass

    def calcular_direcao(self):
        pass


if __name__ == '__main__':
    direcao = Direcao()
    print(f'Testando Direção: {direcao.valor}')
    print()
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)
    print()
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)
    direcao.girar_a_esquerda()
    print(direcao.valor)

    print()

    motor = Motor()
    print(f'Testando Motor: {motor.velocidade}')
    print()
    print(motor.acelerar())
    print(motor.velocidade)
    print(motor.acelerar())
    print(motor.velocidade)
    print(motor.acelerar())
    print(motor.velocidade)
    print(motor.frear())
    print(motor.velocidade)
    print(motor.frear())
    print(motor.velocidade)

    print()

    carro = Carro()
    print(carro.calcular_velocidade())
