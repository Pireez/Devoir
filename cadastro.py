from tkinter import *
import mysql.connector
import customtkinter
cadastro = customtkinter.CTk()

def telacadastro():
    
    cadastro.geometry("400x350")
    texto = customtkinter.CTkLabel(cadastro,font=("Arial",15), text="Cadastro")
    texto.pack(padx=10,pady=10)

    comerciante = customtkinter.CTkButton(cadastro, text="Sou comerciante", width=135,height=100)
    comerciante.pack(padx=10,pady=10)

    naocomerciante = customtkinter.CTkButton(cadastro, text="Não sou comerciante", width=100,height=100)
    naocomerciante.pack(padx=10,pady=10)

telacadastro()
cadastro.mainloop()