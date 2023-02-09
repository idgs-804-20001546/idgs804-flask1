from flask import Flask, request, render_template, redirect, session
import datetime
from practica_4_utils import get_questions, calculate_age, get_zodiac


app = Flask(__name__)
app.secret_key = "my-scret-key"

@app.get("/")
def index():
    return render_template("exam/index.html")


@app.post("/")
def save_data():
    action = request.form.get("action")

    if action == "clear":
        return redirect("/")

    student = {
        "name": request.form.get("name"),
        "middlename": request.form.get("middlename"),
        "lastname": request.form.get("lastname"),
        "day": int(request.form.get("day", "")),
        "month": int(request.form.get("month", "")),
        "year": int(request.form.get("year", "")),
        "gender": request.form.get("gender"),
    }

    session["student"] = student
    return redirect("/questions")


@app.get("/questions")
def questions():
    questions = get_questions()
    return render_template("exam/questions.html", questions=questions)


@app.post("/check")
def check():
    correct_anwsers = [
        question
        for question in get_questions()
        if question["correct"] == int(request.form.get(f"question-{question['id']}"))
    ]

    if not session.get("student"):
        return redirect("/")

    student = session.get("student") or {}
    student["result"] = len(correct_anwsers)
    session["student"] = student

    return redirect("/results")


@app.get("/results")
def results():
    student = session.get("student") or {}

    birthdate = datetime.date(student["year"], student["month"], student["day"])
    age = calculate_age(birthdate)
    zodiac = get_zodiac(student["year"], student["month"], student["day"])

    return render_template("/exam/results.html", student=student, age=age, zodiac=zodiac)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
