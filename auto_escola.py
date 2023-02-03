import PySimpleGUI as pg
class AutoEscola:
    def __init__(self):
        self.cara_layout = [
            [pg.Text('Qual a sua idade?')],
            [pg.Input(size=(10,0),key='Validacao')],
            [pg.Button('Validar!'),pg.Button('Sair')],
            [pg.Output(size=(40,15))]]
        self.cara_janela = pg.Window('Auto Escola', layout = self.cara_layout)

    def iniciar(self):
        while True:
            self.eventos, self.valores = self.cara_janela.Read()
            if self.eventos == 'Validar!':
                try:
                    self.idade = int(self.valores['Validacao'])
                    if self.idade < 18:
                        print('Você é menor de idade e não pode tirar a CNH')
                    elif self.idade >= 18 and self.idade <= 65:
                        print('Parabéns, Você está habilitado a tirar a CNH!')
                    elif self.idade > 65:
                        print('Você está acima da idade permitida!')
                except:
                    print('Digite apenas números!')
            else:
                return False
x = AutoEscola()
x.iniciar()