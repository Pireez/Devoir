
from tkinter import *

janela = Tk()
janela.title("Cotação atual das moedas")
texto_orientacao = Label(janela,text="Clique no butão para ver as contações das moedas")
texto_orientacao.grid(column=0,row=0)
checkbtn = Checkbutton(janela,text="butão")
checkbtn.grid(column=4,row=4)

janela.mainloop()

