
from tkinter import *
import mysql.connector
import customtkinter

customtkinter.set_appearance_mode("Dark")

janela = customtkinter.CTk()

def dimensaojanela():
    # dimensoes da janela
    largura = 400
    altura = 400
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

def fechalogin():
    janela.destroy()
    import cadastro_direcionamento 
    

dimensaojanela()
texto = customtkinter.CTkLabel(janela,font=("Arial",20,'bold'), text="DEVOIR",fg_color="#cd5c5c",width=400)
texto.pack(padx=10,pady=10)
texto = customtkinter.CTkLabel(janela,font=("Arial",20), text="Fazer Login")
texto.pack(padx=10,pady=10)   
usuario = customtkinter.CTkEntry(janela,width=200, placeholder_text="usuario")
usuario.pack(padx=10,pady=10)
senha = customtkinter.CTkEntry(janela,width=200,placeholder_text="senha",show="*")
senha.pack(padx=10,pady=10)
checkbox = customtkinter.CTkCheckBox(janela, text="Salvar Login", font=("Arial",10),checkbox_width=20,checkbox_height=20)
checkbox.pack(padx=10,pady=0)
login = customtkinter.CTkButton(janela,text="Entrar",width=150,fg_color="#cd5c5c")
login.pack(padx=10,pady=10)
cadastro = customtkinter.CTkButton(janela,text="Não tenho login",command=fechalogin)
cadastro.pack(padx=1,pady=10)
naosei = customtkinter.CTkLabel(janela,text="Esqueci minha senha",width=20,height=20, text_color="blue",cursor="hand2")
naosei.pack(padx=1,pady=0)

janela.mainloop()

# class iBanco():
#     def inBanco(self):
#         self.con = mysql.connector.connect(host='localhost', database='devoir',user='root',password='elco478780') # adicionando as conexções com o banco de dados
#         self.cursor = self.con.cursor()
#         self.cursor.close()       
#         self.con.close()
