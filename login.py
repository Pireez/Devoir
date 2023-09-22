from tkinter import *

class Application():
    def __init__(self,janela=None):
        self.janela = janela
        self.janela.title("Login")
        self.janela.geometry("400x400")


        self.frame = Frame(self.janela)
        self.frame.pack(side=TOP)

        self.e1 = Entry(self.frame, font="arial",width=10)
        self.e1.grid(row=0,column=0)
        self.e2 = Entry(self.frame, font="arial",width=10)
        self.e2.grid(row=1,column=0)

        self.btn = Button(self.frame,text="OK",width=3)
        self.btn.grid(row=2,column=0)


app = Tk()
Application(janela=app)
app.mainloop()












# class JanelaLogin:
#     def __init__(self,janela):
#         self.janela = janela
#         self.janela.geometry("500x400")
#         self.janela.title("Login")
#         self.janela.minsize(400, 400) 
#         self.janela.maxsize(400, 400)
# class BtnLogin:
#     def __init__(self,janela):
#         self.janela = janela
#         self.btnLog = Button(app,text="Okay")
#         self.btnLog.pack()

# class lblLoginUsuario:
#     def __init__(self,janela):
#         self.janela = janela 
#         self.lblUsuario = Text(app, height=1)
#         self.lblUsuario.grid(column=1,row=0)

# class txtLogin: 
#     def __init__(self,janela):
#          self.janela = janela
#          self.txtUsuario = Label(app,text="Usuário: ")
#          self.txtUsuario.grid(column=0,row=0)


# janela_login = JanelaLogin(app)
# lbl = lblLoginUsuario(app)
# btn_login = BtnLogin(app)

# ctrl + ; - comenta as linhas

