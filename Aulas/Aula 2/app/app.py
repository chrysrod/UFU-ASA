from flask import Flask, url_for, request, json, jsonify, abort
from user import User

app = Flask(__name__)
myUser = []

@app.route('/')
def api_root():
    return "Seja bem vindo!!"

@app.route('/hello', methods = ['GET'])
def api_hello():
    if 'nome' in request.args:
        return 'Hello ' + request.args['nome']
    else:
        return 'Hello John Doe'

@app.route('/api/adduser', methods = ['POST'])
def api_newuser():
    global myUser
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    new_user = User(id, nome, idade, cidade)
    myUser.append(new_user)
    res = {'status' : 'ok'}
    return jsonify(res)

@app.route('/api/getuser', methods = ['GET'])
def api_getuser():
    global myUser
    user_data = request.get_json()
    print(user_data)
    codUser = user_data['codigo']
    print(codUser)
    print(myUser[0].getUserNome())
    res = {'status' : 'usuário não encontrado'}
    for elem in myUser:
        if(int(codUser) == elem.getUserId()):
            res = {'nome' : elem.getUserNome()}

    return jsonify(res)

@app.route('/api/createusers')
def api_createusers():
    global myUser
    myUser.append(User(1, "João", 12, "São Paulo"))
    myUser.append(User(2, "Pedro", 13, "São Tomé"))
    myUser.append(User(3, "Jorge", 14, "São Bernardo"))
    myUser.append(User(4, "Valdir", 11, "São Roque"))
    myUser.append(User(5, "Antonio", 10, "São Cristóvão"))
    res = {'status' : 'ok'}
    return jsonify(res)

@app.route('/api/listusers', methods = ['GET'])
def api_listusers():
    global myUser
    payload = []
    content = {}

    for elem in myUser:
        content = {'id' : str(elem.getUserId()), '[nome]' : elem.getUserNome(),
        '[idade]' : str(elem.getUserIdade()), '[cidade]' : elem.getUserCidade()}
        payload.append(content)
        content = {}

    res = json.dumps(payload)

    return jsonify(UserList = res)


@app.route('/echo', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return 'Seja bem vindo Alexandre da Silva\n'

    elif request.method == 'POST':
        return 'ECHO: POST\n'

    elif request.method == 'PUT':
        return 'ECHO: PUT\n'

    elif request.method == 'DELETE':
        return 'ECHO: DELETE\n'

if __name__ == 'main':
    app.run()
