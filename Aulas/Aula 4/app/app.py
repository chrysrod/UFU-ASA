from flask import Flask, url_for, request, json, jsonify, abort
from dbUtils import DbUtils

app = Flask(__name__)
myUser = []

@app.route('/')
def api_root():
    return "Server running!"

@app.route('/createdbuser')
def api_createuserdb():
    dbUtils = DbUtils()
    if(dbUtils.createTable()):
        result = {"result": "Tabela de usuários criada!"}
    else:
        result = {"result": "Problemas para criar a tabela de usuários!"}
    return jsonify(result)

@app.route('/adduserdb', methods=['POST'])
def api_adduserdb():
    if not request.json:
        abort(400)
    
    req_data = request.get_json()

    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']

    dbUtils = DbUtils()

    if(dbUtils.addNovoUsuario(nome, idade, cidade)):
        result = {"result": "Usuário inserido com sucesso!"}
    else:
        result = {"result": "Problemas!"}
    return jsonify(result)


if __name__ == 'main':
    app.run()