from flask import Flask, request, render_template, redirect, session
from datetime import datetime
from questions import get_questions
from student import Student


app = Flask(__name__)
app.config('')


@app.get("/")
def index():
    return render_template("exam/index.html")


@app.post("/")
def save_data():
    action = request.form.get("action")

    if action == "clear":
        return redirect("/")

    student = Student(
        name=request.form.get("name"),
        middlename=request.form.get("middlename"),
        lastname=request.form.get("lastname"),
        born_at=request.form.get("born_at"),
        gender=request.form.get("gender"),
    )

    session["student"] = "hello"

    return redirect("/questions")


@app.get("/questions")
def questions():
   
    questions = get_questions()
    return render_template("exam/questions.html", questions=questions)


@app.post("/check")
def check():
    correct_anwsers = [question for question in get_questions() if question["correct"] == int(request.form.get(f"question-{question['id']}"))]

    if not session["student"]:
        return redirect("/")

    student = session["student"] 
    print(student.name)

    return redirect("/questions")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
