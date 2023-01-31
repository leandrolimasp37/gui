import random

class ChuteNumero:

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
    
    def iniciar(self):
        self.gerarValorAleatorio()
        self.pedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo')
                    self.pedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto')
                    self.pedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('PARABÉNS, VOCÊ ACERTOU !')
        except:
            print('Digite apenas numeros!')

    def pedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def gerarValorAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteNumero()
chute.iniciar()
