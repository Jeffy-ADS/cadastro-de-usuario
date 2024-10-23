from Banco import Banco

class Usuarios(object):
    def __init__(self, idusuario =0, nome ="", telefone="", email="", usuario="", senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome= nome
        self.telefone= telefone
        self.email= email
        self.usuario= usuario
        self.senha= senha

#   FUNÇAO INSERIR USUARIO. CADASTRO E VALIDAR DADOS

    def insertUser(self):
        banco = Banco()
#       VALIDAÇÃO DE DADOS
        if self.nome =='' or self.telefone=='' or self.email=='' or self.usuario=='' or self.senha=='':
            return " Preencha todas informações."
       
       
       
        
        try:
            c= banco.conexao.cursor()
            c.execute("insert into usuarios(nome, telefone, email, usuario, senha) values ('" + self.nome+"', '"+ self.telefone +"', '" + self.email +"', '"+ self.usuario +"','"+ self.senha +"')")
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

#   FUNÇÃO  ATUALIZAR USUARIO      
    def updateUser(self):
        banco = Banco()
#       VALIDAÇÃO DE DADOS
        if self.nome =='' or self.telefone=='' or self.email=='' or self.usuario=='' or self.senha=='':
            return " Preencha todas informações."
        try:
            c = banco.conexao.cursor()
            c.execute("update usuarios set nome = '"+self.nome+
                        "', telefone='"+self.telefone+
                        "', email='"+self.email+
                        "', Usuario='"+self.usuario+
                        "', senha='"+self.senha+
                        "' where idusuario='"+self.idusuario+"'")
            banco.conexao.commit()
            c.close()
            return "Usuario atualizado com sucesso!"
        except:
            return "Ocorreu um erro na atualização de usuário"


# FUNÇÃO EXCLUIR USUARIO
    def deleteUser(self):
        banco = Banco()
      

        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM usuarios WHERE idusuario = "+self.idusuario+ " ")
            banco.conexao.commit()
            c.close()
            return "Usuario excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão de usuário"

#FUNÇÃO SELECIONAR USUARIO
    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(" select * from usuarios where idusuario =" +self.idusuario)
            for linha in c:
                self.idusuario= linha[0]
                self.nome= linha[1]
                self.telefone= linha[2]
                self.email= linha[3]
                self.usuario= linha[4]
                self.senha= linha[5]
           
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca de usuário"
        
        



