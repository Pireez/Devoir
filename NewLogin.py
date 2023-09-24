from tkinter import *
import mysql.connector

app = Tk()

class Aplicativo():
    def __init__(self):
        self.app = app
        self.Tela()
        self.CaixaTexto()
        self.funcaoInsert()
        app.mainloop()

    def Tela (self):
        self.app.title('Login')
        self.app.geometry("410x410")

    def CaixaTexto (self):

        self.e1 = Entry(self.app,font="arial",width=20,relief=SOLID)
        self.e1.grid(row=0,column=1)
        self.e2 = Entry(self.app, font="arial",width=20,relief=SOLID)
        self.e2.grid(row=1,column=1)
        self.btn = Button(self.app,text="Cadastrar",width=10,command=self.funcaoInsert())   
        self.btn.grid(row=3,column=1)
    def funcaoInsert(self):
        self.con = mysql.connector.connect(host='localhost', database='devoir', user='root', password='elco478780')
        self.cursor = self.con.cursor()
    
        # Obtenha os valores dos campos de entrada
        usuario = self.e1.get()
        senha = self.e2.get()

        # Use os valores dos campos de entrada na consulta SQL
        self.comando = f'INSERT INTO tbllogin (usuario, senha) VALUES ("{usuario}", "{senha}")'

        try:
            self.cursor.execute(self.comando)
            self.con.commit()
            self.cursor.close()
            self.con.close()
            print("Registro inserido com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao inserir registro: {e}")          

Aplicativo()