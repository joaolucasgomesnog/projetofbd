from flask import Response

from database.connect import ConnectDataBase
from modulos.turma.modelo import Turma
from modulos.turma.sql import SQLTurma

class DaoTurma():
    def __init__(self):
        self.connect = ConnectDataBase().getInstance()

    def get_turmas(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLTurma._SELECT_BUSCA.format(SQLTurma._NOME_TABELA) if busca else SQLTurma._SELECT_ALL

        cursor.execute(sql)
        turmas = []
        columns_name = [desc[0] for desc in cursor.description]
        for turma in cursor.fetchall():
            data = dict(zip(columns_name, turma))
            turmas.append(Turma(**data).get_json())
        return turmas
    
    def salvar(self, turma):
        cursor = self.connect.cursor()
        cursor.execute(SQLTurma._SCRIPT_INSERT,(turma.codigo, turma.turno, turma.professor, turma.disciplina_id))
        self.connect.commit()
        id = cursor.fetchone()[0]
        return id
    
    def get_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLTurma._SELECT_ID, (str(id)))
        turma = cursor.fetchone()
        if not turma:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, turma))
        return Turma(**data)
    
    def get_por_disciplina(self, disciplina_id):
        cursor = self.connect.cursor()
        sql = SQLTurma._SELECT_BY_DISCIPLINA_ID
        cursor.execute(sql, (str(disciplina_id)))
        turmas = []
        columns_name = [desc[0] for desc in cursor.description]
        for disciplina in cursor.fetchall():
            data = dict(zip(columns_name, disciplina))
            turmas.append(data)

        return turmas
        

    def atualizar(self, turma):
        cursor = self.connect.cursor()
        cursor.execute(SQLTurma._UPDATE_BY_ID, turma.codigo, turma. turno, turma.professor)
        self.connect.commit()
        return True