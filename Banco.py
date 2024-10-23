# Banco.py
import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('usuarios.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        
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
        self.conexao.commit()
        c.close()
