# Importa o módulo sqlite3, que fornece uma interface para bancos de dados SQLite em Python
import sqlite3

# Define a classe Banco, que gerencia a conexão com o banco de dados e cria a tabela de usuários
class Banco:
    def __init__(self):
        """
        Método construtor da classe Banco.
        Inicializa a conexão com o banco de dados 'usuarios.db' e chama o método createTable para garantir que a tabela de usuários seja criada.
        """
        # Estabelece a conexão com o banco de dados 'usuarios.db'. Se o arquivo não existir, ele será criado automaticamente.
        self.conexao = sqlite3.connect('usuarios.db')
        
        # Chama o método createTable para criar a tabela de usuários, se ainda não existir
        self.createTable()

    def createTable(self):
        """
        Método responsável por criar a tabela 'usuarios' no banco de dados, caso ela ainda não exista.
        A tabela contém cinco colunas:
        - idusuario: identificador único do usuário (chave primária, autoincrementada).
        - nome: nome do usuário (campo obrigatório).
        - telefone: número de telefone do usuário (campo obrigatório).
        - email: endereço de e-mail do usuário (campo obrigatório).
        - usuario: nome de usuário para login (campo obrigatório).
        - senha: senha do usuário (campo obrigatório).
        """
        # Cria um cursor, que permite executar comandos SQL no banco de dados
        c = self.conexao.cursor()
        
        # Executa o comando SQL para criar a tabela 'usuarios', se ela não existir
        c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
        """)
        
        # Confirma a execução do comando no banco de dados
        self.conexao.commit()
        
        # Fecha o cursor após o uso
        c.close()
