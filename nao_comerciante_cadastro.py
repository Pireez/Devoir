from tkinter import *
import mysql.connector
import customtkinter

cor_vermelho = "#cd5c5c"
cor_cinza = "#d3d3d3"
cor_preta = "black"
widget_padrao = 440
height_padrao = 30
cor_azulescuro = "#483d8b"
cor_branca = "#ffffff"
distancia_x_tela = 10
distancia_y_tela = 20

customtkinter.set_appearance_mode("Dark")

janela = customtkinter.CTk()

con = mysql.connector.connect(host='localhost', database='devoir',user='root',password='elco478780') # adicionando as conexções com o banco de dados
cursor = con.cursor()

def telasucesso():
    dimensaojanela()
    customtkinter.CTkLabel(janela,text="Cadastro realizado com sucesso").pack()

def dimensaojanela():
    # dimensoes da janela
    largura = 500
    altura = 500
    #resolucao do nosso sistema
    largura_screen = janela.winfo_screenwidth()
    altura_screen = janela.winfo_screenheight()
    # posicao da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/2 - altura/2
    #definir a geomatry
    janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
    janela.minsize(largura,altura)
    janela.maxsize(largura,altura)


dimensaojanela()
janela.title("CADASTRO")
texto_cadastro = customtkinter.CTkLabel(janela,font=("Calibri",25,'bold'),
                                        text="Cadastro",
                                        text_color_disabled=None,
                                        width=500,
                                        text_color=cor_branca).place(x=0,y=20)

label_senha = customtkinter.CTkLabel(janela,text="Dados Gerais",font=("Arial",15,'bold'),width=0).place(x=35,y=65)
frame2 = customtkinter.CTkFrame(janela,width=widget_padrao,height=5,fg_color=cor_vermelho).place(x=30,y=90)

entry_nome = customtkinter.CTkEntry(janela, 
                              placeholder_text="Nome e Sobrenome",
                              width=widget_padrao,
                              height=height_padrao)
entry_nome.place(x=30,y=100)

entry_cpf = customtkinter.CTkEntry(janela, 
                             placeholder_text="CPF: XXX.XXX.XXX-XX",
                             width=widget_padrao,
                             height=height_padrao)
entry_cpf.place(x=30,y=140)

entry_telefone = customtkinter.CTkEntry(janela, 
                                  placeholder_text="Telefone: XX XXXXX-XXXX",
                                  width=widget_padrao,
                                  height=height_padrao)
entry_telefone.place(x=30,y=180)

entry_data_nascimento =  customtkinter.CTkEntry(janela, 
                                         placeholder_text="Nascimento: DD/MM/AAAA",
                                         width=widget_padrao,
                                         height=height_padrao)
entry_data_nascimento.place(x=30,y=220)

entry_email = customtkinter.CTkEntry(janela, 
                               placeholder_text="Seu E-mail",
                               width=widget_padrao,
                               height=height_padrao)
entry_email.place(x=30,y=260)

label_senha = customtkinter.CTkLabel(janela,text="Senha",width=0,font=("Arial",15,'bold')).place(x=35,y=300)
frame3 = customtkinter.CTkFrame(janela,width=widget_padrao,height=5,fg_color=cor_vermelho).place(x=30,y=325)

senha_entry = customtkinter.CTkEntry(janela,placeholder_text="Senha",width=widget_padrao)
senha_entry.place(x=30,y=335)
confirma_senha_entry = customtkinter.CTkEntry(janela,placeholder_text="Confirmar Senha",width=widget_padrao)
confirma_senha_entry.place(x=30,y=370)

def insert():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    data_nascimento = entry_data_nascimento.get()
    email = entry_email.get()
    cursor.execute("INSERT INTO tblcomerciante (nome,cpf,telefone,data_nascimento,email) VALUES ('"+nome+"','"+cpf+"','"+telefone+"','"+data_nascimento+"','"+email+"')")
    con.commit()
    print("Registro salvo")

btn_cadastrar = customtkinter.CTkButton(janela,width=widget_padrao,
                                        height=50,
                                        font=("Arial",15,"bold"),
                                        text="CADASTRAR",
                                        hover_color=cor_vermelho,command=insert).place(x=30,y=420)

janela.mainloop()

