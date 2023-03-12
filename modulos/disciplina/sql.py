class SQLDisciplina:
    _NOME_TABELA = 'disciplina'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}('\
                           f'id serial primary key,'\
                           f'descricao VARCHAR)'
    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(descricao)'\
                     f'values(%s) RETURNING id'
                     
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s' 
    _SELECT_BUSCA = "SELECT * FROM {} where descricao ILIKE '%{}%'"
    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET descricao=%s'\
                    f'WHERE id=%s'

    
    