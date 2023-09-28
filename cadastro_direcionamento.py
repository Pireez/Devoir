from tkinter import *
import mysql.connector
import customtkinter

largura_btn = 460 
altura_btn = 200

janela = customtkinter.CTk()

def dimensaojanela():
    # dimensoes da janela
    largura = 500
    altura = 500
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

def tela_nao_comerciante():
    janela.destroy()
    import nao_comerciante_cadastro
    

dimensaojanela()
janela.title("CADASTRO")
btn_nao_comerciante=customtkinter.CTkButton(janela,
                                            width=largura_btn,
                                            height=altura_btn,
                                            text="Não comerciante",
                                            font=("Arial",20,'bold'),
                                            command=tela_nao_comerciante).place(x=20,y=40)

btn_sou_comerciante=customtkinter.CTkButton(janela,
                                            width=largura_btn,
                                            height=altura_btn,
                                            text="Sou comerciante",
                                            font=("Arial",20,'bold')).place(x=20,y=270)

janela.mainloop()