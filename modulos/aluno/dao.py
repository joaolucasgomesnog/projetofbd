from flask import Response

from database.connect import ConnectDataBase
from modulos.aluno.modelo import Aluno
from modulos.aluno.sql import SQLAluno

class DaoAluno():
    def __init__(self):
        self.connect = ConnectDataBase().getInstance()

    def get_alunos(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLAluno._SELECT_BUSCA.format(SQLAluno._NOME_TABELA,busca) if busca else SQLAluno._SELECT_ALL

        cursor.execute(sql)
        alunos = []
        columns_name = [desc[0] for desc in cursor.description]
        for aluno in cursor.fetchall():
            data = dict(zip(columns_name, aluno))
            alunos.append(Aluno(**data).get_json())
        return alunos
    
    def salvar(self, aluno):
        cursor = self.connect.cursor()
        cursor.execute(SQLAluno._SCRIPT_INSERT, (aluno.matricula, aluno.nome, aluno.genero, aluno.endereco, aluno.telefone))
        self.connect.commit()
        id = cursor.fetchone()[0]
        aluno.id = id
        return aluno
    
    def get_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLAluno._SELECT_ID, (str(id)))
        aluno = cursor.fetchone()
        if not aluno:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name,aluno))
        return Aluno(**data)
    
    def atualizar(self, aluno):
        cursor = self.connect.cursor()
        cursor.execute(SQLAluno._UPDATE_BY_ID, aluno.matricula, aluno.nome, aluno.genero, aluno.endereco. aluno.telefone)
        self.connect.commit()
        return True