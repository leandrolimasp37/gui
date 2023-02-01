
# Faça uma pergunta e o programa de dará uma resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:

    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso',
            'Não sei, você que sabe',
            'Não faz isso Não!',
            'Acho que tá na hora certa!'
        ]

    def iniciar(self):
        # layout
        layout = [
            [sg.Text('Faça sua pergunta: ')], # label
            [sg.Input(size=(50,0))],          # entrada de dados
            [sg.Output(size=(50,10))],        # resposta do random
            [sg.Button('OK',size=(5,2))],     # botão
            [sg.Button('Sair',size=(5,2))]    # botão
        ]

        # janela
        self.janela = sg.Window('Programa de Decisão !', layout=layout)
        while True:
            # valores
            self.eventos, self.valores = self.janela.Read()
            # condição
            if self.eventos == 'OK':
                print(random.choice(self.respostas))
            elif self.eventos == 'Sair':
                return self.janela.Close()
            else:
                return False
    
a = DecidaPorMim()
a.iniciar()