from flask import Flask, make_response, jsonify, request, Response
from database.connect import ConnectDataBase
from modulos.aluno.dao import DaoAluno
from modulos.aluno.modelo import Aluno
from modulos.disciplina.dao import DaoDisciplina
from modulos.disciplina.modelo import Disciplina
from modulos.turma.dao import DaoTurma
from modulos.turma.modelo import Turma

app = Flask(__name__)
ConnectDataBase().init_table()
dao_aluno = DaoAluno()
dao_disciplina = DaoDisciplina()
dao_turma = DaoTurma()

@app.route('/alunos/', methods=['GET'])
def alunos():
    parametros = request.args
    busca = parametros.get('busca', None)
    alunos = dao_aluno.get_alunos(busca)
    return make_response(jsonify(alunos))

@app.route('/aluno/add/', methods = ['POST'])
def add_aluno():
    data_aluno = dict(request.form)
    aluno = Aluno(**data_aluno)
    aluno = dao_aluno.salvar(aluno)
    return make_response(aluno.get_json(),202)

@app.route('/aluno/<int:id>/', methods = ['GET'])
def aluno_id(id: int):
    aluno = dao_aluno.get_by_id(id)
    if not aluno:
        return Response({}, status=404)
    return make_response(jsonify(aluno.get_json()))

@app.route('/aluno/<int:id>/', methods=['PUT'])
def atualizar_aluno(id: int):
    data_aluno = dict(request.form)
    aluno = dao_aluno.get_by_id(id)
    aluno.matricula = data_aluno.get('matricula')
    aluno.nome = data_aluno.get('nome')
    aluno.genero = data_aluno.get('genero')
    aluno.endereco = data_aluno.get('endereco')
    aluno.telefone = data_aluno.get('telefone')
    if dao_aluno.atualizar(aluno):
        return make_response(jsonify(aluno.get_json()))
    return Response({}, status=404)


@app.route('/disciplinas/', methods=['GET'])
def disciplinas():
    parametros = request.args
    busca = parametros.get('busca', None)
    disciplina = dao_disciplina.get_disciplinas(busca)
    return make_response(jsonify(disciplina))

@app.route('/disciplina/add/', methods = ['POST'])
def add_disciplina():
    data_disciplina = dict(request.form)
    disciplina = Disciplina(**data_disciplina)
    disciplina = dao_disciplina.salvar(disciplina)
    return make_response(disciplina.get_json(),202)

@app.route('/disciplina/<int:id>/', methods = ['GET'])
def disciplina_id(id: int):
    disciplina = dao_disciplina.get_by_id(id)
    if not disciplina:
        return Response({}, status=404)
    return make_response(jsonify(disciplina.get_json()))

@app.route('/disciplina/<int:id>/', methods=['PUT'])
def atualizar_disciplina(id: int):
    data_disciplina = dict(request.form)
    disciplina = dao_disciplina.get_by_id(id)
    disciplina.descricao = data_disciplina.get('descricao')
    if dao_aluno.atualizar(disciplina):
        return make_response(jsonify(disciplina.get_json()))
    return Response({}, status=404)

@app.route('/disciplina/<int:id>/turmas/', methods=['GET'])
def disciplina_turmas(id: int):
    disciplina = dao_disciplina.get_by_id(id)
    if not disciplina:
        return Response({}, status=404)
    turmas = dao_turma.get_por_disciplina(disciplina.id)
    return make_response(jsonify(turmas))

@app.route('/disciplina/<int:id>/turma/add/', methods=['POST'])
def add_turma(id: int):
    disciplina = dao_disciplina.get_by_id(id)
    if not disciplina:
        return Response({}, status=404)
    data_turma = dict(request.form)
    turma = Turma(disciplina=disciplina, **data_turma)
    id = dao_turma.salvar(turma)
    turma.id = id
    return make_response(jsonify(turma.get_json()))






app.run()