class SQLAluno:
    _NOME_TABELA = 'aluno'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}('\
                           f'id serial primary key,'\
                           f'matricula integer unique,'\
                           f'nome VARCHAR,'\
                           f'genero VARCHAR,'\
                           f'endereco VARCHAR,'\
                           f'telefone VARCHAR)'
    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(matricula, nome, genero, endereco, telefone)'\
                     f'values(%s,%s,%s,%s,%s) RETURNING id'
                     
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s' 
    _SELECT_BUSCA = "SELECT * FROM {} where matricula ILIKE '%{}%'"
    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET matricula=%s, nome=%s, genero=%s, endereco=%s, telefone=%s,'\
                    f'WHERE id=%s'

    
    