import psycopg2
from modulos.aluno.sql import SQLAluno
from modulos.disciplina.sql import SQLDisciplina
from modulos.turma.sql import SQLTurma

class ConnectDataBase:
    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database="faculdadebd",
            user="postgres",
            password="123456"
        )

    def getInstance(self):
        return self._connect
    
    def init_table(self):
        cursor = self._connect.cursor()
        cursor.execute(SQLAluno._SCRIPT_CREATE_TABLE)
        cursor.execute(SQLDisciplina._SCRIPT_CREATE_TABLE)
        cursor.execute(SQLTurma._SCRIPT_CREATE_TABLE)
        self._connect.commit()

    def sql_new(self):
        return
        