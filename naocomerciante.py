from tkinter import *
import mysql.connector
import customtkinter


#def tela_cadastro_comerciante():





janela = customtkinter.CTk()
def dimensaojanela():
        # dimensoes da janela
        largura = 600
        altura = 500
        #resolucao do nosso sistema
        largura_screen = janela.winfo_screenwidth()
        altura_screen = janela.winfo_screenheight()
        # posicao da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        #definir a geomatry
        janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
    
dimensaojanela()
qtdcaracteres = 11

def limitar_catacteres(*args):
        if len(entry.get()) > qtdcaracteres:
            entry.set(entry.get()[:qtdcaracteres])

entry = customtkinter.StringVar()
entry.trace_add("write",limitar_catacteres)

texto = customtkinter.CTkLabel(janela,font=("Arial",15), text="Cadastro")
texto.pack(padx=10,pady=10)

nome = customtkinter.CTkEntry(janela,width=200, placeholder_text="Digite seu Nome")
nome.pack(padx=10,pady=10)

cpflabel = customtkinter.CTkLabel(janela,text="Digite seu CPF")
cpflabel.pack(padx=0,pady=0)

cpf = customtkinter.CTkEntry(janela,width=200, textvariable=entry, placeholder_text="Digite seu CPF")
cpf.pack(padx=10,pady=10)

telefone = customtkinter.CTkEntry(janela,width=200, placeholder_text="Digite seu Telefone")
telefone.pack(padx=10,pady=10)

data_nascimento = customtkinter.CTkEntry(janela, width=200, placeholder_text="Digite sua Data de nascimento")
data_nascimento.pack(padx=10,pady=10)

email = customtkinter.CTkEntry(janela, width=200, placeholder_text="Digite seu e-mail")
email.pack(padx=10,pady=10)

cadastrar = customtkinter.CTkButton(janela,text="CADASTRAR")
cadastrar.pack(padx=10,pady=15)

    
    
janela.mainloop()

