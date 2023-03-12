from flask import Response

from database.connect import ConnectDataBase
from modulos.disciplina.modelo import Disciplina
from modulos.disciplina.sql import SQLDisciplina

class DaoDisciplina():
    def __init__(self):
        self.connect = ConnectDataBase().getInstance()

    def get_disciplinas(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLDisciplina._SELECT_BUSCA.format(SQLDisciplina._NOME_TABELA) if busca else SQLDisciplina._SELECT_ALL

        cursor.execute(sql)
        disciplinas = []
        columns_name = [desc[0] for desc in cursor.description]
        for discplina in cursor.fetchall():
            data = dict(zip(columns_name,discplina))
            disciplinas.append(Disciplina(**data).get_json())
        return disciplinas
    
    def salvar(self, disciplina):
        cursor = self.connect.cursor()
        cursor.execute(SQLDisciplina._SCRIPT_INSERT, (disciplina.descricao))
        self.connect.commit()
        id = cursor.fetchone()[0]
        return id
    
    def get_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLDisciplina._SELECT_ID, (str(id)))
        disciplina = cursor.fetchone()
        if not disciplina:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, disciplina))
        return Disciplina(**data)
    
    def atualizar(self, disciplina):
        cursor = self.connect.cursor()
        cursor.execute(SQLDisciplina._UPDATE_BY_ID, disciplina.descricao)
        self.connect.commit()
        return True