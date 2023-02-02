from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/datos")
def datos():
    name = "John Doe"
    products = ["Pc", "Macbook", "iphone"]
    return render_template("datos.html", products = products, name = name)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
