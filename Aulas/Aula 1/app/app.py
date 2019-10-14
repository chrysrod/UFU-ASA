from flask import Flask, url_for, request, json

app = Flask(__name__)
@app.route('/')
def api_root():
    return "Seja bem vindo!!"

@app.route('/hello', methods = ['GET'])
def api_hello():
    if 'nome' in request.args:
        return 'Olá ' + request.args['nome']
    else:
        return 'Olá desconhecido!!!'

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
