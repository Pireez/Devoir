from tkinter import *
import mysql.connector
import customtkinter

cor_vermelho = "#cd5c5c"
cor_cinza = "#d3d3d3"
cor_preta = "black"
widget_padrao = 430
height_padrao = 30


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
def cxFrame():
    Frame1 = customtkinter.CTkFrame(janela,width=430,height=30,fg_color=cor_vermelho).place(x=30,y=20)

texto = customtkinter.CTkLabel(cxFrame(),font=("Arial",25,'bold'), text="Cadastro",fg_color=cor_vermelho,text_color="black").place(x=50,y=20)

nome = customtkinter.CTkEntry(janela, 
                              placeholder_text="Nome e Sobrenome",
                              width=widget_padrao,
                              height=height_padrao).place(x=30,y=100)

cpf = customtkinter.CTkEntry(janela, 
                             placeholder_text="CPF: XXX.XXX.XXX-XX",
                             width=widget_padrao,
                             height=height_padrao).place(x=30,y=150)

telefone = customtkinter.CTkEntry(janela, 
                                  placeholder_text="Telefone: XX XXXXX-XXXX",
                                  width=widget_padrao,
                                  height=height_padrao).place(x=30,y=200)

data_nascimento = customtkinter.CTkEntry(janela, 
                                         placeholder_text="Nascimento: DD/MM/AAAA",
                                         width=widget_padrao,
                                         height=height_padrao).place(x=30,y=250)

email = customtkinter.CTkEntry(janela, 
                               placeholder_text="Seu E-mail",
                               width=widget_padrao,
                               height=height_padrao).place(x=30,y=300)

janela.mainloop()
