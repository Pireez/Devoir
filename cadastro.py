from tkinter import *
import mysql.connector
import customtkinter

customtkinter.set_appearance_mode("Dark")

janela = customtkinter.CTk()

def dimensaojanela():
    # dimensoes da janela
    largura = 500
    altura = 700
    #resolucao do nosso sistema
    largura_screen = janela.winfo_screenwidth()
    altura_screen = janela.winfo_screenheight()
    # posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    #definir a geomatry
    janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
    janela.minsize(largura,altura)
    janela.maxsize(largura,altura)

dimensaojanela()
texto = customtkinter.CTkLabel(janela,font=("Arial",20,'bold'), text="Cadastro",bg_color="blue",width=500)
texto.pack(padx=10,pady=10)

nome_comerciante = customtkinter.CTkEntry(janela, placeholder_text="Escreva seu nome",width=430).place(x=30,y=100)
idade_comerciante = customtkinter.CTkEntry(janela, placeholder_text="Idade",width=430).place(x=30,y=150)

janela.mainloop()
