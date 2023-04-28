from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import os

class Interface:

    def __init__(self):
        pass

    def notepad(self): os.system('notepad')
    def mensagem(self): messagebox.showinfo(title='Creator',message='Leandro Lima')

    def interface_1(self):
        # Window
        self.janela_1 = Tk() # declaração
        self.janela_1.title('Terminal Administrativo') # titulo
        self.janela_1.geometry('800x500+450+250') # largura x altura, esq + topo
        self.janela_1.configure(bg='lightblue') # cor

        self.menu_barra = Menu(self.janela_1)

        # Menu 1
        self.menu_arquivo = Menu(self.menu_barra, tearoff=0)
        self.menu_arquivo.add_command(label='Escolas', command=self.interface_2)
        self.menu_arquivo.add_command(label='Bloco de Notas', command=self.notepad)
        self.menu_arquivo.add_separator()
        self.menu_arquivo.add_command(label='Sair', command='exit')
        self.menu_barra.add_cascade(label='Pesquisar',menu=self.menu_arquivo)

        # Menu 2
        self.menu_programa = Menu(self.menu_barra, tearoff=0)
        self.menu_programa.add_command(label='Nada Ainda', command='')
        self.menu_programa.add_command(label='Nada Ainda', command='')
        self.menu_barra.add_cascade(label='Programas',menu=self.menu_programa)

        # Menu 3
        self.menu_ajuda = Menu(self.menu_barra, tearoff=0)
        self.menu_ajuda.add_command(label='Ajuda', command='')
        self.menu_ajuda.add_command(label='Sobre', command=self.mensagem)
        self.menu_barra.add_cascade(label='Ajuda',menu=self.menu_ajuda)

        # Start
        self.janela_1.config(menu=self.menu_barra)
        self.janela_1.mainloop()

    def interface_2(self):
        # window
        self.janela_2 = Tk()
        self.janela_2.title('Consulta de Escolas')
        self.janela_2.geometry('800x500')
        self.janela_2.configure(bg='lightblue')

        # File
        self.abrir_arquivo = []
        with open('data.txt','r') as arquivo:
            self.abrir_arquivo = [linha for linha in arquivo]

        # Layout
        self.texto_titulo = Label(self.janela_2, text='Janela de Consultas', bg='lightblue', font='arial 25')
        self.texto_titulo.place(x=100,y=10)

        # ComboBox
        self.selecionar_opcao = Combobox(self.janela_2, values=self.abrir_arquivo, font='arial 20')
        self.selecionar_opcao.grid(padx=60,pady=80)
        self.selecionar_opcao['state'] = 'readonly'

        # Button
        self.botao_ok = Button(self.janela_2, text='PESQUISAR', font='arial 20', bg='white', fg='#0D2A7C', command='')
        self.botao_ok.place(x=450,y=70)
        self.botao_sair = Button(self.janela_2, text='SAIR', font='arial 20', bg='white' ,fg='#0D2A7C', command=self.janela_2.destroy)
        self.botao_sair.place(x=650,y=70)
        
        # Start
        self.janela_2.mainloop()

x = Interface()
x.interface_1()

