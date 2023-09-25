from tkinter import *
import mysql.connector
import customtkinter
from cadastro import telacadastro


customtkinter.set_appearance_mode("Dark")
janela = customtkinter.CTk()

def dimensaojanela():
    # dimensoes da janela
    largura = 600
    altura = 400
    #resolucao do nosso sistema
    largura_screen = janela.winfo_screenwidth()
    altura_screen = janela.winfo_screenheight()
    # posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    #definir a geomatry
    janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

dimensaojanela()
texto = customtkinter.CTkLabel(janela,font=("Arial",20,'bold'), text="DEVOIR",bg_color="black",width=500)
texto.pack(padx=10,pady=10)
texto = customtkinter.CTkLabel(janela,font=("Arial",15), text="Fazer Login")
texto.pack(padx=10,pady=10)

def clique():
    print("Login realizado com sucesso")

def fechalogin():
    janela.destroy()

usuario = customtkinter.CTkEntry(janela,width=200, placeholder_text="usuario")
usuario.pack(padx=10,pady=10)
senha = customtkinter.CTkEntry(janela,width=200,placeholder_text="senha",show="*")
senha.pack(padx=10,pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Salvar Login", font=("Arial",10))
checkbox.pack(padx=10,pady=5)

login = customtkinter.CTkButton(janela,text="Login",command=clique)
login.pack(padx=10,pady=15)


cadastro = customtkinter.CTkButton(janela,text="Não tenho login",command=lambda:[fechalogin(),telacadastro()])
cadastro.pack(padx=1,pady=1)
naosei = customtkinter.CTkLabel(janela,text="Esqueci minha senha",width=20,height=20, text_color="blue",cursor="hand2")
naosei.pack(padx=1,pady=2)

janela.mainloop()













# app = Tk()

# class Aplicativo():
#     def __init__(self):
#         self.app = app
#         self.Tela()
#         self.CaixaTexto()
#         self.funcaoInsert()
#         app.mainloop()

#     def Tela (self):
#         self.app.title('Login')
#         self.app.geometry("410x410")

#     def CaixaTexto (self):

#         self.e1 = Entry(self.app,font="arial",width=20,relief=SOLID)
#         self.e1.grid(row=0,column=1)
#         self.e2 = Entry(self.app, font="arial",width=20,relief=SOLID)
#         self.e2.grid(row=1,column=1)
#         self.btn = Button(self.app,text="Cadastrar",width=10)   
#         self.btn.grid(row=3,column=1)
#     def funcaoInsert(self):
#         self.con = mysql.connector.connect(host='localhost', database='devoir', user='root', password='elco478780')
#         self.cursor = self.con.cursor()
    
#         # Obtenha os valores dos campos de entrada
#         usuario = self.e1.get()
#         senha = self.e2.get()

#         # Use os valores dos campos de entrada na consulta SQL
#         self.comando = f'INSERT INTO tbllogin (usuario, senha) VALUES ("{usuario}", "{senha}")'

#         try:
#             self.cursor.execute(self.comando)
#             self.con.commit()
#             self.cursor.close()
#             self.con.close()
#             print("Registro inserido com sucesso!")
#         except mysql.connector.Error as e:
#             print(f"Erro ao inserir registro: {e}")          

# Aplicativo()