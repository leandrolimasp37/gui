
# simulador de dado
# simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    # configurações iniciais
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]        
        ]

    # iniciar aplicação
    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Ok, saindo...')
            else: 
                print('Favor digitar sim ou nao')
        except:
            print('Ocorreu algum erro inesperado!')

    # gerar numero aleatorio de 1 a 6
    def GerarValorDoDado(self):
        print('o numero gerado é:', random.randint(self.valor_minimo, self.valor_maximo))


# instanciar(chamar) a classe
simulador = SimuladorDeDado()
simulador.Iniciar()