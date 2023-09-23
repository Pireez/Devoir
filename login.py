from tkinter import *

app = Tk()

# Chama as funções da classe, calculos etc..
class Funcs():
    def resultado_soma(self):
        self.a=int(self.e1.get())
        self.b=int(self.e2.get())
        self.c = self.a + self.b
        self.label["text"] = self.c

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
        self.app.geometry("700x500")
        self.app.configure(background="black")
        self.app.resizable(True,True)
        self.app.maxsize(width=900,height=700)
        self.app.minsize(width=800,height=600)
    def frames_da_tela(self):
        # Criando um quadrado ne tela para inserir as informações
        self.frame1 = Frame(self.app, bd=4,bg="white",highlightbackground="#777777",highlightthickness=5)
        self.frame1.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)
    def criando_widgets(self):
        # entrada de texto
        self.e1 = Entry(self.frame1,font="arial",width=10)
        self.e1.grid(row=0,column=1)
        self.e2 = Entry(self.frame1, font="arial",width=10)
        self.e2.grid(row=1,column=1)
        # btn confirmar
        self.btn = Button(self.frame1,text="Entrar",width=5,command=self.resultado_soma)
        self.btn.grid(row=2,column=1)
    def lblApp(self):
        # Lbl Usuario e senha
        self.txtUsuario = Label(self.frame1,text="Usuario")
        self.txtUsuario.grid(row=0,column=0)
        self.txtsenha = Label(self.frame1,text="Senha")
        self.txtsenha.grid(row=1,column=0)
        # Txt resultado do login
        self.label = Label(self.frame1,text="Resultado")
        self.label.grid(row=3,column=1)
      
Application()



# ctrl + ; - comenta as linhas

