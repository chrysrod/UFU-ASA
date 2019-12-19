from flask import Flask, render_template, request, json, jsonify
import flask_bootstrap

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route("/signUp")
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user = request.form['username']
    password = request.form['password']
    print(user, password)
    return json.dumps({'status': 'OK', 'user': user, 'pass': password})

@app.route('/showMessage', methods=['POST'])
def show_message():
    return json.dumps({'status':'OK', 'message':'Funcionou!!!'})
    #return jsonify(dict(redirect='/success'))

@app.route('/success')
def success():
    return render_template('sucess.html')

if __name__ == "__main__":
    app.run()