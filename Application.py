from Usuarios import Usuarios
import tkinter as tk
from tkinter import *
import os

os.system('cls')

class Application:
    def __init__(self, master=None):
        self.fonte=("Verdana", "8")
#   CONTAINERS
        self.container1 = Frame(master)
        self.container1["pady"] =10
        self.container1.pack()
        
        self.container2 = Frame(master)
        self.container2["padx"] =20
        self.container2["pady"] =5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] =20
        self.container3["pady"] =5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] =20
        self.container4["pady"] =5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] =20
        self.container5["pady"] =5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] =20
        self.container6["pady"] =5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] =20
        self.container7["pady"] =5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] =20
        self.container8["pady"] =5
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] =15
        self.container9.pack()

#   TITULOS 
        self.titulo = Label(self.container1, text=" Preencha as Informações: ")
        self.titulo["font"] = ("Calaibri", "9", "bold")
        self.titulo.pack()

#   BUTÃO DE FAZER BUSCA DE USUARIO
        self.lblidusuario = Label(self.container2, text="idUsuario: ", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario= Entry(self.container2)
        self.txtidusuario["width"]=10
        self.txtidusuario["font"]= self.fonte
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar= Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"]= self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

#   EXIBIR INFORMAÇÃO E RECEBER TEXTO DO USUARIO
##  CONTAINER 3 - NOME:
        self.lblnome= Label(self.container3, text="Nome: ", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome= Entry(self.container3,)
        self.txtnome["width"]=25
        self.txtnome["font"]= self.fonte
        self.txtnome.pack(side=LEFT)

##  CONTAINER 4 - TELEFONE:
        self.lbltelefone= Label(self.container4, text="Telefone: ", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone= Entry(self.container4,)
        self.txttelefone["width"]=10
        self.txttelefone["font"]= self.fonte
        self.txttelefone.pack(side=LEFT)

## CONTAINER 5 - EMAIL:
        self.lblemail= Label(self.container5, text="E-mail: ", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail= Entry(self.container5,)
        self.txtemail["width"]=10
        self.txtemail["font"]= self.fonte
        self.txtemail.pack(side=LEFT)

##  CONTAINER 6 - USUARIO:
        self.lblusuario= Label(self.container6, text="Usuario: ", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario= Entry(self.container6,)
        self.txtusuario["width"]=10
        self.txtusuario["font"]= self.fonte
        self.txtusuario.pack(side=LEFT)

## CONTAINER 7 - SENHA:
        self.lblsenha= Label(self.container7, text="Senha: ", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha= Entry(self.container7,)
        self.txtsenha["width"]=10
        self.txtsenha["show"]="*"
        self.txtsenha["font"]= self.fonte
        self.txtsenha.pack(side=LEFT)

#   BUTÃO: INSERIR, ALTERAR E EXCLUIR
##  CONTAINER 8
        self.btnInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.btnInsert["command"]= self.inserirUsuario
        self.btnInsert.pack(side= LEFT)

        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"]= self.alterarUsuario
        self.btnAlterar.pack(side= LEFT)

        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"]= self.excluirUsuario
        self.btnExcluir.pack(side= LEFT)

#   MENSAGENS DE AVISO
##  CONTAINER 9

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"]= ("Verdana", "9", "italic") 
        self.lblmsg.pack()

#   FUNÇÃO INSERIR USUARIO
    def inserirUsuario(self):
        user = Usuarios()

        user.idusuario=  self.txtidusuario.get()
        user.nome= self.txtnome.get()
        user.telefone= self.txttelefone.get()
        user.email= self.txtemail.get()
        user.usuario= self.txtusuario.get()
        user.senha= self.txtsenha.get()

#       VALIDAÇÃO DE DADOS
        if not user.nome:
            self.lblmsg["text"] = "Nome não pode estar vazio"
            return
        if not user.telefone:
            self.lblmsg["text"]= "Telefone não pode estar vazio."
            return
        if not user.email:
            self.lblmsg["text"]= "E-mail não pode estar vazio."
            return
        if not user.usuario:
            self.lblmsg["text"]= "Campo precisa de um nome de Usuario"
            return
        if not user.senha:
            self.lblmsg["text"]= "Campo precisa de uma Senha de Usuario"


        
        self.lblmsg["text"]= user.insertUser()

        self.txtidusuario.delete(0,END)
        self.txtnome.delete(0,END)
        self.txttelefone.delete(0,END)
        self.txtemail.delete(0,END)
        self.txtusuario.delete(0,END)
        self.txtsenha.delete(0,END)         


#   FUNÇÃO ALTERAR USUARIO
    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario=  self.txtidusuario.get()
        user.nome= self.txtnome.get()
        user.telefone= self.txttelefone.get()
        user.email= self.txtemail.get()
        user.usuario= self.txtusuario.get()
        user.senha= self.txtsenha.get()

        #       VALIDAÇÃO DE DADOS
        if not user.nome:
            self.lblmsg["text"] = "Nome não pode estar vazio"
            return
        if not user.telefone:
            self.lblmsg["text"]= "Telefone não pode estar vazio."
            return
        if not user.email:
            self.lblmsg["text"]= "E-mail não pode estar vazio."
            return
        if not user.usuario:
            self.lblmsg["text"]= "Campo precisa de um nome de Usuario"
            return
        if not user.senha:
            self.lblmsg["text"]= "Campo precisa de uma Senha de Usuario"

        self.lblmsg["text"]= user.updateUser()

        
        self.txtidusuario.delete(0,END)
        self.txtnome.delete(0,END)
        self.txttelefone.delete(0,END)
        self.txtemail.delete(0,END)
        self.txtusuario.delete(0,END)
        self.txtsenha.delete(0,END)


#   FUNÇÃO EXCLUIR USUARIO
    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario= self.txtidusuario.get()

        self.lblmsg["text"]= user.deleteUser()

        self.txtidusuario.delete(0,END)
        self.txtnome.delete(0,END)
        self.txttelefone.delete(0,END)
        self.txtemail.delete(0,END)
        self.txtusuario.delete(0,END)
        self.txtsenha.delete(0,END)

#   FUNÇÃO BUSCAR USUARIO
    def buscarUsuario(self):
        user = Usuarios()

        user.idusuario= self.txtidusuario.get()

        self.lblmsg["text"]= user.selectUser(user.idusuario)

        self.txtidusuario.delete(0,END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0,END)
        self.txtnome.insert(INSERT, user.nome)

        self.txttelefone.delete(0,END)
        self.txttelefone.insert(INSERT, user.telefone)

        self.txtemail.delete(0,END)
        self.txtemail.insert(INSERT, user.email)

        self.txtusuario.delete(0,END)
        self.txtusuario.insert(INSERT, user.usuario)

        self.txtsenha.delete(0,END)
        self.txtsenha.insert(INSERT, user.senha)

root= Tk()
Application(root)
root.mainloop()




