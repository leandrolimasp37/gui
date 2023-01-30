import random


class ChuteNumero:

    def __init__(self):
        self.num_aleatorio = random.randint(1,100)
        self.msg = 'Escolha um numero de 1 a 100: '

    def chutar(self):
        print('Numero certo:', self.num_aleatorio)
        while True:
            try:
                chute = int(input(self.msg))

                if chute < self.num_aleatorio:
                    print('Chute um valor MAIS ALTO')
                elif chute > self.num_aleatorio:
                    print('Chute um valor MAIS BAIXO')
                else:
                    print('VOÇÊ ACERTOU !')
                    return False
            except:
                print('Algo deu errado... ')

x = ChuteNumero()
x.chutar()

