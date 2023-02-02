from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/operasbas")
def operations():
    return render_template("operasbas.html")

@app.route("/result", methods = ['POST'])
def result():
    val1 = int(request.form.get("val1"))
    val2 = int(request.form.get("val2"))
    result = val1 * val2
    return render_template("result.html", result = result)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
