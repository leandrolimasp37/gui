
#simulador de dado
#simular o uso de um dado, gerando um valor de 1 até 6
import random

class SimuladorDeDado:
    #configurações iniciais
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.msg = 'Você gostaria de gerar um novo valor para o dado? '
    
    #iniciar aplicação
    def Iniciar(self):
        #receber dados do usuario
        resposta = input(self.msg) 
        #tratamento de erros
        try:
            if resposta == 'sim' or resposta =='s':
                self.GerarValorDoDado()
            elif resposta == 'nao' or resposta =='n':
                print('Ok, saindo...')
            else:
                print('Favor digitar sim ou nao')
        except:
            print('Ocorreu algum erro inesperado!')

    #gerar numero aleatorio de 1 a 6
    def GerarValorDoDado(self):
        print('o numero gerado é:', random.randint(self.valor_minimo, self.valor_maximo))


#instanciar(chamar) a classe
simulador = SimuladorDeDado()
simulador.Iniciar()