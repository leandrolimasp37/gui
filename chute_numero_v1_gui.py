import random
import PySimpleGUI as sg

class ChuteNumero:

    def __init__(self):
        self.num_aleatorio = random.randint(1,100)

    def iniciar(self):
        # layout
        layout = [
            [sg.Text('Seu Chute',size=(39,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))]
        ]
        # janela
        self.janela = sg.Window('Chute o numero!',layout=layout)

        try:
            while True:
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Chutar!':
                    self.chute = self.valores['ValorChute']

                    while True:
                        if int(self.chute) < self.num_aleatorio:
                            print('Chute um valor MAIS ALTO')
                            break
                        elif int(self.chute) > self.num_aleatorio:
                            print('Chute um valor MAIS BAIXO')
                            break
                        elif int(self.chute) == self.num_aleatorio:
                            print('VOCÊ ACERTOU !')
                            break
                        else:
                            print('OPS, algo deu errado...')
                            return False
                else:
                    return False
        except:
            print('Favor digitar apenas números!')
            self.iniciar()

x = ChuteNumero()
x.iniciar()

