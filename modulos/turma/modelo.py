class Turma:
    def __init__(self, codigo, turno, professor, disciplina_id, id=None):
        self.codigo = codigo
        self.turno = turno
        self.professor = professor
        self.disciplina_id = disciplina_id
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - Codigo: {self.codigo} - Turno: {self.turno} - Professor: {self.professor} - Disciplina_ID: {self.disciplina_id}'
    
    def get_json(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'turno': self.turno,
            'professor': self.professor,
            'disciplina_id': self.disciplina_id,
        }
    
    def get_sql_insert(self):
        return