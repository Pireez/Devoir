from tkinter import *

app = Tk()

class Funcs():
    def resultado_soma(self):
        self.a=int(self.e1.get())
        self.b=int(self.e2.get())
        self.c = self.a + self.b
        self.label["text"] = self.c


class Application(Funcs):
    def __init__(self):
        self.app = app

        self.tela()
        app.mainloop()

    def tela(self):
        self.app.title("Login")
        self.app.geometry("400x300")

        self.e1 = Entry(self.app, font="arial",width=10)
        self.e1.grid(row=0,column=0)
        self.e2 = Entry(self.app, font="arial",width=10)
        self.e2.grid(row=1,column=0)

        self.btn = Button(self.app,text="Entrar",width=5,command=self.resultado_soma)
        self.btn.grid(row=2,column=0)


        self.label = Label(self.app,text="Resultado")
        self.label.grid(row=3,column=0)

        

Application()



# ctrl + ; - comenta as linhas

