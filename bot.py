import pyautogui as pg
import time
class Bot:
    '''
    --------------------------
     Bot para Noticias do SPFC 
    --------------------------
    '''
    def __init__(self):
        pg.PAUSE = 1
    def iniciar(self):
        print (Bot.__doc__)
        pg.press('win')
        pg.write('executar')
        pg.press('enter')
        pg.write('chrome.exe')
        pg.press('enter')
        pg.write('https://ge.globo.com/')
        pg.press('enter')
        time.sleep(1)
        '''
        pg.position()
        print(pg.position())
        '''
        pg.click(x=286,y=173)
        pg.click(x=348,y=493)
x = Bot()
x.iniciar()