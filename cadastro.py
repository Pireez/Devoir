from tkinter import *
import mysql.connector
import customtkinter
from naocomerciante import tela_cadastro_comerciante

def telacadastro():
    janela = customtkinter.CTk()
    def dimensaojanela():
        # dimensoes da janela
        largura = 600
        altura = 300
        #resolucao do nosso sistema
        largura_screen = janela.winfo_screenwidth()
        altura_screen = janela.winfo_screenheight()
        # posicao da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        #definir a geomatry
        janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
    
    def fechacadastro():
        janela.destroy()
    
    
    dimensaojanela()
    texto = customtkinter.CTkLabel(janela,font=("Arial",15), text="Cadastro")
    texto.pack(padx=10,pady=10)

    comerciante = customtkinter.CTkButton(janela, text="Sou comerciante", width=135,height=100,command=lambda: [fechacadastro(),tela_cadastro_comerciante()])
    comerciante.pack(padx=10,pady=10)

    naocomerciante = customtkinter.CTkButton(janela, text="Não sou comerciante", width=100,height=100)
    naocomerciante.pack(padx=10,pady=10)

    janela.mainloop()