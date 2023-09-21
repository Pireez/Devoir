
from tkinter import *

janela = Tk()
# Criação dp tamanho da janela
janela.geometry("400x400") 
# Deixando ela limitada ao tamanho Altura e Largura
janela.minsize(400, 400) 
janela.maxsize(400, 400)
# Titulo da tela
janela.title("Login")
# Criação da Label
textoUsuario = Label(janela,text="Digite seu usuário: ")
textoUsuario.grid(column=0,row=0)
# Criação no texboxte
textExample= Text(janela, height=1)
textExample.grid(column=3,row=1)
# Criação do botão
botao = Button(janela,text="Ok")
botao.grid(column=0,row=1)
janela.mainloop()

