from flask import Flask, render_template
from flask import request
from math import sqrt

app = Flask(__name__)

@app.route("/")
def operations():
    return render_template("practica-2.html")

@app.route("/result", methods = ['POST'])
def result():
    x1 = float(request.form.get("x1"))
    x2 = float(request.form.get("x2"))
    y1 = float(request.form.get("y1"))
    y2 = float(request.form.get("y2"))

    result = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return render_template("result.html", result = result)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
