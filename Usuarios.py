# Importa a classe Banco, que gerencia a conexão com o banco de dados SQLite
from Banco import Banco

# Define a classe Usuarios, responsável por gerenciar operações CRUD (Create, Read, Update, Delete) para os usuários
class Usuarios(object):
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        """
        Método construtor da classe Usuarios.
        Inicializa os atributos de um objeto da classe Usuarios, representando um usuário do sistema.

        Parâmetros:
        - idusuario (int): Identificador único do usuário (padrão = 0).
        - nome (str): Nome do usuário (padrão = string vazia).
        - telefone (str): Número de telefone do usuário (padrão = string vazia).
        - email (str): Endereço de e-mail do usuário (padrão = string vazia).
        - usuario (str): Nome de usuário para login (padrão = string vazia).
        - senha (str): Senha do usuário (padrão = string vazia).
        """
        # Dicionário para armazenar informações do usuário
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    # FUNÇÃO INSERIR USUÁRIO: Cadastro e validação de dados
    def insertUser(self):
        """
        Insere um novo usuário no banco de dados, validando os dados antes da inserção.
        
        Retorna:
        - Mensagem de sucesso ou erro na inserção do usuário.
        """
        banco = Banco()
        
        # Validação para garantir que todos os campos estejam preenchidos
        if self.nome == '' or self.telefone == '' or self.email == '' or self.usuario == '' or self.senha == '':
            return "Preencha todas as informações."
        
        try:
            # Insere os dados do usuário na tabela 'usuarios'
            c = banco.conexao.cursor()
            c.execute(f"INSERT INTO usuarios(nome, telefone, email, usuario, senha) "
                      f"VALUES ('{self.nome}', '{self.telefone}', '{self.email}', '{self.usuario}', '{self.senha}')")
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    # FUNÇÃO ATUALIZAR USUÁRIO: Atualização de dados do usuário
    def updateUser(self):
        """
        Atualiza as informações de um usuário existente no banco de dados, validando os dados antes da atualização.

        Retorna:
        - Mensagem de sucesso ou erro na atualização do usuário.
        """
        banco = Banco()
        
        # Validação para garantir que todos os campos estejam preenchidos
        if self.nome == '' or self.telefone == '' or self.email == '' or self.usuario == '' or self.senha == '':
            return "Preencha todas as informações."
        
        try:
            # Atualiza os dados do usuário na tabela 'usuarios'
            c = banco.conexao.cursor()
            c.execute(f"UPDATE usuarios SET nome = '{self.nome}', telefone = '{self.telefone}', "
                      f"email = '{self.email}', Usuario = '{self.usuario}', senha = '{self.senha}' "
                      f"WHERE idusuario = '{self.idusuario}'")
            banco.conexao.commit()
            c.close()
            
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na atualização do usuário"

    # FUNÇÃO EXCLUIR USUÁRIO: Excluir um usuário do banco de dados
    def deleteUser(self):
        """
        Exclui um usuário do banco de dados com base no ID do usuário.

        Retorna:
        - Mensagem de sucesso ou erro na exclusão do usuário.
        """
        banco = Banco()

        try:
            # Deleta o usuário da tabela 'usuarios' com base no 'idusuario'
            c = banco.conexao.cursor()
            c.execute(f"DELETE FROM usuarios WHERE idusuario = {self.idusuario}")
            banco.conexao.commit()
            c.close()
            
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    # FUNÇÃO SELECIONAR USUÁRIO: Buscar um usuário específico no banco de dados
    def selectUser(self, idusuario):
        """
        Busca as informações de um usuário no banco de dados com base no ID do usuário.
        
        Parâmetros:
        - idusuario (int): O identificador único do usuário a ser buscado.

        Retorna:
        - Mensagem de sucesso ou erro na busca do usuário.
        """
        banco = Banco()

        try:
            # Seleciona o usuário na tabela 'usuarios' com base no 'idusuario'
            c = banco.conexao.cursor()
            c.execute(f"SELECT * FROM usuarios WHERE idusuario = {self.idusuario}")
            
            # Atribui os dados do usuário encontrado aos atributos da instância
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
            
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
