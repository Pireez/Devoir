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

        self.e1 = Entry(self.app,font="arial",width=20,relief=SOLID,)
        self.e1.grid(row=0,column=1)
        self.e2 = Entry(self.app, font="arial",width=20,relief=SOLID)
        self.e2.grid(row=1,column=1)        

    def funcaoInsert(self):
        self.con = mysql.connector.connect(host='localhost', database='devoir',user='root',password='elco478780') # adicionando as conexções com o banco de dados
        self.cursor = self.con.cursor()
        self.comando = f'INSERT INTO tbllogin (usuario, senha) VALUES ("{self.e1.get()}", "{self.e2.get()}")' # Escreva o comando em SQL
        self.btn = Button(self.app,text="Cadastrar",width=10,command=self.cursor.execute(self.comando))
        
        self.con.commit()
        self.btn.grid(row=3,column=1)
        self.cursor.close()       
        self.con.close()
        

      

Aplicativo()