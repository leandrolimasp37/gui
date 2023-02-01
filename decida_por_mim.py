
# Faça uma pergunta e o programa de dará uma resposta
import random

class DecidaPorMim:

    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso',
            'Não sei, você que sabe',
            'Não faz isso Não!',
            'Acho que tá na hora certa!'
        ]

    def iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

    
a = DecidaPorMim()
a.iniciar()