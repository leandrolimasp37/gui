import random

class ChuteNumero:

    def __init__(self):
        self.num_aleatorio = random.randint(1,100)
        self.msg = 'Digite um numero de 1 a 100: '

    def iniciar(self):
        try:
            while True:
                self.chute = int(input(self.msg))
                if self.chute < self.num_aleatorio:
                    print('Chute um valor MAIS ALTO')
                elif self.chute > self.num_aleatorio:
                    print('Chute um valor MAIS BAIXO')
                else:
                    print('VOCÊ ACERTOU !')
                    return False
        except:
            print('Ops, algo deu errado...')

x = ChuteNumero()
x.iniciar()
