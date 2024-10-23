# Importa a classe Usuarios do módulo Usuarios (presumivelmente, um módulo que você criou para manipular dados de usuário)
from Usuarios import Usuarios

# Importa tkinter, uma biblioteca para criar interfaces gráficas (GUI) em Python
import tkinter as tk
from tkinter import *
import os

# Limpa o terminal ao iniciar o programa
os.system('cls')

# Define a classe Application, que cria a interface gráfica e manipula os dados do usuário
class Application:
    def __init__(self, master=None):
        """
        Método construtor da classe Application. Este método cria a interface gráfica e organiza os componentes em containers.
        Ele define os componentes visuais como rótulos (Labels), caixas de texto (Entries) e botões (Buttons).
        """
        self.fonte = ("Verdana", "8")  # Define a fonte padrão dos textos

        # Define e organiza os containers (áreas onde os widgets serão agrupados)
        self.container1 = Frame(master)
        self.container1["pady"] = 10  # Padding (espaçamento vertical) entre este container e o topo
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20  # Padding horizontal
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        # Título da interface
        self.titulo = Label(self.container1, text="Preencha as Informações:")
        self.titulo["font"] = ("Calaibri", "9", "bold")
        self.titulo.pack()

        # Campo e botão para buscar um usuário pelo ID
        self.lblidusuario = Label(self.container2, text="idUsuario: ", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        # Campos para exibir e inserir informações do usuário (Nome, Telefone, Email, etc.)
        self.lblnome = Label(self.container3, text="Nome: ", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone: ", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 10
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail: ", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 10
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(self.container6, text="Usuario: ", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 10
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha: ", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 10
        self.txtsenha["show"] = "*"  # Oculta o conteúdo do campo senha
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        # Botões para inserir, alterar e excluir usuário
        self.btnInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.btnInsert["command"] = self.inserirUsuario
        self.btnInsert.pack(side=LEFT)

        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterarUsuario
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluirUsuario
        self.btnExcluir.pack(side=LEFT)

        # Mensagem de status (exibida após uma ação como inserir, alterar ou excluir)
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    # Função para inserir um novo usuário
    def inserirUsuario(self):
        """
        Coleta os dados inseridos nos campos de texto, valida-os e chama a função insertUser() da classe Usuarios
        para inserir um novo registro no banco de dados.
        """
        user = Usuarios()

        # Captura os valores inseridos nos campos de entrada
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        # Validações simples para garantir que os campos não estejam vazios
        if not user.nome:
            self.lblmsg["text"] = "Nome não pode estar vazio"
            return
        if not user.telefone:
            self.lblmsg["text"] = "Telefone não pode estar vazio."
            return
        if not user.email:
            self.lblmsg["text"] = "E-mail não pode estar vazio."
            return
        if not user.usuario:
            self.lblmsg["text"] = "Campo precisa de um nome de Usuario"
            return
        if not user.senha:
            self.lblmsg["text"] = "Campo precisa de uma Senha de Usuario"
            return

        # Insere o usuário no banco de dados
        self.lblmsg["text"] = user.insertUser()

        # Limpa os campos após a inserção
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    # Função para alterar os dados de um usuário existente
    def alterarUsuario(self):
        """
        Altera os dados de um usuário existente, após validar os novos dados inseridos nos campos de entrada.
        """
        user = Usuarios()

        # Captura os valores dos campos de entrada
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        # Validações simples para garantir que os campos não estejam vazios
        if not user.nome:
            self.lblmsg["text"] = "Nome não pode estar vazio"
            return
        if not user.telefone:
            self.lblmsg["text"] = "Telefone não pode estar vazio."
            return
        if not user.email:
            self.lblmsg["text"] = "E-mail não pode estar vazio."
            return
        if not user.usuario:
            self.lblmsg["text"] = "Campo precisa de um nome de Usuario"
            return
        if not user.senha:
            self.lblmsg["text"] = "Campo precisa de uma Senha de Usuario"
            return

        # Atualiza os dados do usuário no banco de dados
        self.lblmsg["text"] = user.updateUser()

        # Limpa os campos após a alteração
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    # Função para excluir um usuário pelo ID
    def excluirUsuario(self):
        """
        Exclui o usuário com base no ID inserido.
        """
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        # Exclui o usuário no banco de dados
        self.lblmsg["text"] = user.deleteUser()

        # Limpa os campos após a exclusão
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    # Função para buscar um usuário pelo ID
    def buscarUsuario(self):
        """
        Busca os dados de um usuário pelo ID e preenche os campos da interface gráfica com as informações encontradas.
        """
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        # Busca o usuário no banco de dados e exibe as informações nos campos de entrada
        self.lblmsg["text"] = user.selectUser(user.idusuario)

        # Preenche os campos da interface com os dados encontrados
        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.telefone)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)

        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, user.senha)


# Inicializa a aplicação Tkinter
root = Tk()
Application(root)
root.mainloop()
