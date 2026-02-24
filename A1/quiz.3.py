# Quiz game. Third version
# Name: Beverly Mambou
# Date: Feb, 24,2026
# Make a a list with the questions and the correct answers.
#Make QUESTIONS a dictionary, to include answer options and the correct choice

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr? ": ["12", "10", "15", "8"],
    "What is the capital of Texas? ": ["Austin", "Dallas", "Houston", "San Antonio"],
    "The last supper was painted by which artist? ": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

for questions, options in QUESTIONS.items():
    correct_answer = options [0] #The first option is the correct answer
    for alternative in sorted(options):
        print(f" - {alternative}")

    answer = input(questions + ": ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r} not {answer!r}")
        