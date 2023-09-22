from tkinter import *



class JanelaLogin:
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry("500x400")
        self.janela.title("Login")
        self.janela.minsize(400, 400) 
        self.janela.maxsize(400, 400)

class BtnLogin:
    def __init__(self,janela):
        self.janela = janela
        self.btnLog = Button(app,text="Okay")
        self.btnLog.pack()
        
app = Tk()
janela_login = JanelaLogin(app)
btn_login = BtnLogin(app)
app.mainloop()