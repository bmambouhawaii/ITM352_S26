# AI USAGE (Assignment Requirement)
# ChatGPT was used to assist with debugging, structuring, and improving this Flask application.
# Key areas included:
# - Fixing question/answer mismatch caused by random shuffling (using session storage)
# - Resolving Flask session errors ("working outside request context")
# - Implementing login/logout functionality with Flask sessions
# - Debugging Jinja template loops and form handling
# - Loading quiz data dynamically from a JSON file
#
# Example prompts used:
# "Flask quiz answers not matching after shuffle"
# "Working outside request context Flask session fix"
# "How to implement login and logout using Flask sessions"

from flask import Flask, render_template, request, redirect, session, url_for
import json
import random #I asked AI what this is and it explained that it's a built-in Python module that provides functions for generating random numbers and shuffling data, which is useful for randomizing quiz questions.

app = Flask(__name__)
app.secret_key = "secret123" #I asked AI about this line and it explained that the secret key is used by Flask to securely sign session cookies, which allows the application to store user-specific data (like login status) across requests. It's important to keep this key secret in a real application.


# Load questions from JSON
def load_questions():
    with open("ASSIGNMENTS/questions.json") as f: #Same questions as Assignment 1, but now stored in a JSON file. This function reads the questions from the JSON file and returns them as a list of dictionaries.
        return json.load(f)


# LOGIN PAGE

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST": #post method means the form has been submitted. It retrieves the username from the form, stores it in the session, and redirects to the home page. The session allows us to keep track of the logged-in user across different pages of the application.
        username = request.form.get("username")
        session["user"] = username
        return redirect(url_for("home"))

    return render_template("login.html")



# QUIZ PAGE (HOME)

@app.route("/")
def home():
    # force login first
    if "user" not in session:
        return redirect(url_for("login"))

    questions = load_questions()
    random.shuffle(questions)

    # save shuffled questions in session (IMPORTANT FIX)
    session["questions"] = questions #this is where i had trouble because the questions were being shuffled on every page load, which caused the answers to not match. By saving the shuffled questions in the session, we ensure that the same order of questions is used when the user submits their answers.

    return render_template("quiz.html", questions=questions, user=session["user"])


# SUBMIT ANSWERS

@app.route("/submit", methods=["POST"])
def submit():
    # get SAME questions order from session
    questions = session.get("questions")

    score = 0
    results = []

    for i, q in enumerate(questions):
        user_answer = request.form.get(f"q{i}")
        correct = user_answer == q["answer"]

        if correct:
            score += 1

        results.append({
            "question": q["question"],
            "your_answer": user_answer,
            "correct_answer": q["answer"],
            "correct": correct
        })

    # save score to file (Requirement 9)
    username = session.get("user")
    with open("scores.txt", "a") as f:
        f.write(f"{username},{score}\n")

    return render_template("result.html", score=score, total=len(questions), results=results)

#Logout route
@app.route("/logout") #I used this route because initially, the site does not allow me to relogin as a different user. So, I added an option for the user to logout after getting results.
def logout():
    session.clear()
    return redirect(url_for("login"))


# RUN APP

if __name__ == "__main__":
    app.run(debug=True, port=5001)