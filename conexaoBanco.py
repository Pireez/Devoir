from tkinter import *
import mysql.connector

janela = Tk()

janela.geometry("500x500")
con = mysql.connector.connect(host='localhost', database='devoir',user='root',password='elco478780') # adicionando as conexções com o banco de dados
cursor = con.cursor()
label1 = Label(janela,text="nome").place(x=10,y=10)
entrynome = Entry(janela)
entrynome.place(x=50,y=10)

label2 = Label(janela,text="idade").place(x=10,y=30)
entryidade = Entry(janela)
entryidade.place(x=50,y=30)


def save():
    nome=entrynome.get()
    idade=entryidade.get()
    cursor.execute("INSERT INTO tblteste (nome,idade) VALUES ('"+nome+"','"+idade+"')")
    con.commit()
    print("Record save")

btn = Button(janela, text="Salvar", command=save).place(x=50,y=60)


janela.mainloop()