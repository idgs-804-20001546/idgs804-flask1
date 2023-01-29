from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola Mundo¡ de cuyo nombre"

# string param
@app.route("/user/<string:user>")
def user(user):
    return "Hello " + user

# int param
@app.route("/number/<int:n>")
def number(n):
    return "Number: {}".format(n)

# multi params
@app.route("/multi/<int:n>/<string:username>")
def multi(n, username):
    return "Number: {} and Userame: {}".format(n, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1 + n2)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
