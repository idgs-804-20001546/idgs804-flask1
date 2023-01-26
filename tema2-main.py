from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola Mundo¡ de cuyo nombre"

@app.route("/hola")
def hola():
    return "¡Hola Mundo¡ de cuyo nombre"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
