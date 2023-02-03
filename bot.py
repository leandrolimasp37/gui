import pyautogui as pg
import time
class Bot:
    '''
    --------------------
     Bot para automação 
    --------------------
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
        pg.write('http://leandrolima.rf.gd')
        pg.press('enter')
        time.sleep(3)
        pg.position()
        print(pg.position())
        pg.click(x=1323, y=128)
x = Bot()
x.iniciar()