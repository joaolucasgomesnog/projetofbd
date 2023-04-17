class SQLTurma:
    _NOME_TABELA = 'turma'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}('\
                           f'id serial primary key,'\
                           f'codigo VARCHAR,'\
                           f'turno VARCHAR,'\
                           f'professor VARCHAR,'\
                           f'disciplina_id int  references disciplina(id))'
    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(codigo, turno, professor)'\
                     f'values(%s,%s,%s,%s) RETURNING id'
                     
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s' 
    _SELECT_BY_DISCIPLINA_ID = f'SELECT * FROM {_NOME_TABELA} WHERE disciplina_id=%s' 
    _SELECT_BUSCA = "SELECT * FROM {} where codigo ILIKE '%{}'"
    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET codigo=%s, turno=%s, professor=%s, disciplina_id=%s'\
                    f'WHERE id=%s'

    
    