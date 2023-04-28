from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import os
import webbrowser

class Interface:

    def __init__(self):
        self.interface_1()

    def link_diretoria_ensino(self): webbrowser.open('https://deosasco.educacao.sp.gov.br')
    def link_sed(self): webbrowser.open('https://sed.educacao.sp.gov.br')
    def link_sei(self): webbrowser.open('https://sei.prefeitura.sp.gov.br')
    def link_email_microsoft(self): webbrowser.open('https://outlook.office.com/mail')
    def link_email_google(self): webbrowser.open('https://mail.google.com/mail')
    def excel(self): os.system('start excel')
    def word(self): os.system('start winword')
    def mensagem(self): messagebox.showinfo(title='Desenvolvedor',message='Leandro Lima')

    def interface_1(self):
        # Window
        self.janela_1 = Tk() # declaração
        self.janela_1.title('Terminal Administrativo') # titulo
        self.janela_1.geometry('800x500+450+250') # largura x altura, esq + topo
        self.janela_1.configure(bg='lightblue') # cor

        self.menu_barra = Menu(self.janela_1)

        # Menu 1
        self.menu_arquivo = Menu(self.menu_barra, tearoff=0)
        self.menu_arquivo.add_command(label='Site da DE', command=self.link_diretoria_ensino)
        self.menu_arquivo.add_command(label='Site da SED', command=self.link_sed)
        self.menu_arquivo.add_command(label='Site da SEI', command=self.link_sei)
        self.menu_arquivo.add_separator()
        self.menu_arquivo.add_command(label='Email da Microsoft', command=self.link_email_microsoft)
        self.menu_arquivo.add_command(label='Email da Google', command=self.link_email_google)
        self.menu_arquivo.add_separator()
        self.menu_arquivo.add_command(label='Consulta de Escolas', command=self.interface_2)
        self.menu_arquivo.add_separator()
        self.menu_arquivo.add_command(label='Sair', command='exit')
        self.menu_barra.add_cascade(label='Acessos',menu=self.menu_arquivo)

        # Menu 2
        self.menu_programa = Menu(self.menu_barra, tearoff=0)
        self.menu_programa.add_command(label='Microsoft Excel', command=self.excel)
        self.menu_programa.add_command(label='Microsoft Word', command=self.word)
        self.menu_barra.add_cascade(label='Programas',menu=self.menu_programa)

        # Menu 3
        self.menu_autor = Menu(self.menu_barra, tearoff=0)
        self.menu_autor.add_command(label='Sobre o Autor', command=self.mensagem)
        self.menu_barra.add_cascade(label='Sobre',menu=self.menu_autor)

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
