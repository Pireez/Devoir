from tkinter import *
import mysql.connector

# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

class iBanco():
    def inBanco(self):
        self.con = mysql.connector.connect(host='localhost', database='devoir',user='root',password='elco478780') # adicionando as conexções com o banco de dados
        self.cursor = self.con.cursor()

app = Tk()

class Application(iBanco):
    def __init__(self):
        self.app = app
        
        self.frames_da_tela()
        self.criando_widgets()
        self.lblApp()
        self.conexcaoBanco()
        self.tela()
        app.mainloop()    

    def tela(self):
        self.app.title("Login")
        self.app.geometry("410x410")
        self.app.maxsize(width=510,height=510)
        self.app.minsize(width=510,height=510)
    def frames_da_tela(self):
        # Criando um quadrado ne tela para inserir as informações
        self.frame_cima = Frame(self.app, bd=4,bg=co2,highlightbackground="#777777",highlightthickness=5)
    def criando_widgets(self):
        # entrada de texto
        self.e1 = Entry(self.app,font="arial",width=20,relief=SOLID,)
        self.e1.grid(row=0,column=1)

        self.e2 = Entry(self.app, font="arial",width=20,relief=SOLID)
        self.e2.grid(row=1,column=1)
    def conexcaoBanco (self):
        #Execurtar os comandos das funções
        self.a = (self.e1.get())
        self.b = (self.e2.get())
        self.comando = f'INSERT INTO tblLogin (usuario, senha) VALUES ({self.a},{self.b})' # Escreva o comando em SQL
        #cursor.execute(comando) # Manda executar a linha de comando
        #con.commit() # se o comando for de edição - edita o banco de dados
        #cursor.fetchall()# se o comando for de leitura - le o banco de dados
        # Fechandoas conexções
        # btn confirmar
    def lblApp(self):
        # Lbl Usuario e senha
        self.txtUsuario = Label(self.app,text="Usuario")
        self.txtUsuario.grid(row=0,column=0)
        self.txtsenha = Label(self.app,text="Senha")
        self.txtsenha.grid(row=1,column=0)


class btnCadastrar(Application,iBanco):
    def btnCadastrar1(self):
        self.btn = Button(self.app,text="Cadastrar",width=10, command=self.cursor.execute(self.comando))
        self.btn.grid(row=3,column=2)

class fBanco(iBanco):
    def fcBanco(self):
        self.cursor.close()       
        self.con.close()
  
Application()


