# Quiz game. Second version
# Name: Beverly Mambou
# Date: Feb, 24,2026
# Make a a list with the questions and the correct answers.

QUESTIONS = [
    ("What is the airspeed of an unladen swallow in miles/hr? ", "12"),
    ("What is the capital of Texas? ", "Austin"),
    ("The last supper was painted by which artist? ", "Da Vinci"),
]
for question, correct_answer in QUESTIONS:
    answer = input(question + ": ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r} not {answer!r}")
