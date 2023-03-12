class Aluno:
    def __init__(self, matricula, nome, genero, endereco, telefone, id=None):
        self.matricula = matricula
        self.nome = nome
        self.genero = genero
        self.endereco = endereco
        self.telefone = telefone
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - Matricula: {self.matricula} - Nome: {self.nome} - Genero: {self.genero} - endereco: {self.endereco} - telefone: {self.telefone}'
    
    def get_json(self):
        return {
            'id': self.id,
            'matricula': self.matricula,
            'nome': self.nome,
            'genero': self.genero,
            'endereco': self.endereco,
            'telefone': self.telefone,
        }
    
    def get_sql_insert(self):
        return