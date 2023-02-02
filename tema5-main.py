from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/users")
def users():
    return render_template("users.html")
   
@app.route("/pupils")
def pupils():
    return render_template("pupils.html")
 

if __name__ == '__main__':
    app.run(debug=True, port=3000)
