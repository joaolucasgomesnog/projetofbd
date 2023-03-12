class Disciplina:
    def __init__(self, descricao, id=None):
        self.descricao = descricao
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - Descricao: {self.descricao}'
    
    def get_json(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
        }
    
    def get_sql_insert(self):
        return