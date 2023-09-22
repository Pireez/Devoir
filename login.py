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

        self.btn = Button(self.frame,text="Entrar",width=5)
        self.btn.grid(row=2,column=0)

app = Tk()
Application(janela=app)
app.mainloop()

# ctrl + ; - comenta as linhas

