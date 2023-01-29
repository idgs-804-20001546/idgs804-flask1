from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def suma():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        operation = request.form.get("operation")
        result = 0

        if operation == "suma":
            result = num1 + num2

        if operation == "resta":
            result = num1 - num2

        if operation == "multi":
            result = num1 * num2

        if operation == "division":
            result = num1 / num2

        return "<h1>El resultado de la {} es: {}</h1>".format(operation, result)
    else:
        return """
            <form action='/' method='POST'>

                <input type="radio" name="operation" value="suma"> <label>Suma: </label>
                <input type="radio" name="operation" value="resta"> <label>Resta: </label>
                <input type="radio" name="operation" value="multi"> <label>Multiplicacion: </label>
                <input type="radio" name="operation" value="division"> <label>Division: </label><br> <br>

                <label>N1: </label> 
                <input type="text" name="num1"> <br>
                
                <label>N2: </label> 
                <input type="text" name="num2">

                <input type="submit" value="Calcular">
            </form>
        """
    

if __name__ == '__main__':
    app.run(debug=True, port=3000)
