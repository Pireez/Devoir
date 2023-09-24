from tkinter import *
import mysql.connector

con = mysql.connector.connect(host='localhost', database='devoir',user='root',password='elco478780') 

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao servidor MySQL versão",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("conectado ao banco de dados",linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("conexão ao MySQL foi encerrada")


        # cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters


app = Tk()

# Chama as funções da classe, calculos etc..
class Funcs():
    def resultado_soma(self):
        self.a=int(self.e1.get())
        self.b=int(self.e2.get())
# Roda o Aplicativo
class Application(Funcs):
    def __init__(self):
        self.app = app

        self.frames_da_tela()
        self.lblApp()
        self.criando_widgets()
        self.tela()
        app.mainloop()

    def tela(self):
        self.app.title("Login")
        self.app.geometry("410x410")
        self.app.configure(background="black")
        self.app.resizable(True,True)
        self.app.maxsize(width=510,height=510)
        self.app.minsize(width=510,height=510)
    def frames_da_tela(self):
        # Criando um quadrado ne tela para inserir as informações
        self.frame_cima = Frame(self.app, bd=4,bg=co2,highlightbackground="#777777",highlightthickness=5)
        self.frame_cima.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.60)
    def criando_widgets(self):
        # entrada de texto
        self.e1 = Entry(self.frame_cima,font="arial",width=20,relief=SOLID,)
        self.e1.grid(row=0,column=1)


        self.e2 = Entry(self.frame_cima, font="arial",width=20,relief=SOLID)
        self.e2.grid(row=1,column=1)
        # btn confirmar
        self.btn = Button(self.frame_cima,text="Entrar",width=5,command=self.resultado_soma)
        self.btn.grid(row=2,column=1)
    def lblApp(self):
        # Lbl Usuario e senha
        self.txtUsuario = Label(self.frame_cima,text="Usuario")
        self.txtUsuario.grid(row=0,column=0)
        self.txtsenha = Label(self.frame_cima,text="Senha")
        self.txtsenha.grid(row=1,column=0)
        # Txt resultado do login
        self.label = Label(self.frame_cima,text="Resultado")
        self.label.grid(row=3,column=1)
      
Application()


