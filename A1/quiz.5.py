# Quiz game. Fifth version
# Name: Beverly Mambou
# Date: Feb, 24,2026
# Make a a list with the questions and the correct answers.
#Make QUESTIONS a dictionary, to include answer options and the correct choice.
#Alow the user to select the correct answer by label
#Improve look and usability. Keep track of correct answers.

from string import ascii_lowercase
ascii = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


ascii = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr? ": ["12", "10", "15", "8"],
    "What is the capital of Texas? ": ["Austin", "Dallas", "Houston", "San Antonio"],
    "The last supper was painted by which artist? ": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}



num_correct = 0
for num, (questions, options) in enumerate(QUESTIONS.items(), start=1):
    print(f"Question {num}:")
    print(questions)
    correct_answer = options [0] #The first option is the correct answer
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(options)))
    for label,  alternative in labeled_alternatives.items():
        print(f" {label}: {alternative}")   

answer_label = input("Choice? ")
answer = labeled_alternatives.get (answer_label)
if answer == correct_answer:
    print("Correct!")
    num_correct += 1
else:
    print(f"The answer is {correct_answer!r} not {answer!r}")

print(f"You got {num_correct} out of {len(QUESTIONS)} correct.")


    
