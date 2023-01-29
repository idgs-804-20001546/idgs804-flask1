from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola Mundo¡ de cuyo nombre"

@app.route("/suma", methods = ["GET", "POST"])
def suma():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        return "<h1>La Suma es: {}</h1>".format(num1 + num2)
    else:
        return """
            <form action='/suma' method='POST'>
                <label>N1: </label> 
                <input type="text" name="num1"> <br>
                
                <label>N2: </label> 
                <input type="text" name="num2">

                <input type="submit" value="Calcular">
            </form>
        """
    

if __name__ == '__main__':
    app.run(debug=True, port=3000)
