import time
import os

# -----------------------------
# QUIZ QUESTIONS. Stored my questions in alist of dictionaries for easy access and scalability.
# -----------------------------
questions = [
    {
        "song": "Love Yourself",
        "options": ["A. Justin Bieber", "B. Drake", "C. Shawn Mendes", "D. The Weeknd"],
        "answer": "A"
    },
    {
        "song": "One Dance",
        "options": ["A. Bruno Mars", "B. Drake", "C. Ed Sheeran", "D. Justin Timberlake"],
        "answer": "B"
    },
    {
        "song": "Work",
        "options": ["A. Beyonce", "B. Ariana Grande", "C. Rihanna", "D. Adele"],
        "answer": "C"
    },
    {
        "song": "Closer",
        "options": ["A. The Chainsmokers", "B. Maroon 5", "C. Coldplay", "D. Imagine Dragons"],
        "answer": "A"
    },
    {
        "song": "Cheap Thrills",
        "options": ["A. Katy Perry", "B. Lady Gaga", "C. Sia", "D. Pink"],
        "answer": "C"
    }
]

# -----------------------------
# LOAD USERS FROM FILE
# -----------------------------
def load_users():
    users = {}

    if os.path.exists("users.txt"): #All users and their high scores are stored in a file called users.txt. When the quiz starts, it checks if this file exists and loads the data into a dictionary for easy access during the quiz.
        with open("users.txt", "r") as file:
            for line in file:
                username, score = line.strip().split(",")
                users[username] = int(score)

    return users


# -----------------------------
# SAVE USERS BACK TO FILE
# -----------------------------
def save_users(users):
    with open("users.txt", "w") as file: #This function saves all users and their high scores to a file. The .txt file loads existing users and their high scores.
        for username in users:            #"w" means write mode, which will overwrite the entire file with updated data. 
            file.write(f"{username},{users[username]}\n")


# -----------------------------
# LOGIN SYSTEM
# -----------------------------
def login(users):
    username = input("Enter your username: ").lower()

    if username in users:
        print("Welcome back,", username) #If the username already exists, it welcomes the user back and shows their previous high score. If it's a new username, it creates a new entry in the users dictionary with a starting score of 0.
        print("Your high score is:", users[username])
    else:
        print("New user created!")
        users[username] = 0

    return username


# -----------------------------
# GET GRAND CHAMPION
# -----------------------------
def get_grand_champion(users): #This function finds the user with the highest score across all users and returns their username and score. It uses the max() function with a key argument to find the user with the highest score.
    if not users:
        return None, 0

    champion = max(users, key=users.get)
    return champion, users[champion]


# -----------------------------
# MAIN QUIZ FUNCTION
# -----------------------------
def run_quiz():
    users = load_users()
    username = login(users) #This function handles the main flow of the quiz. It loads users, manages the login process, runs through each quiz question, tracks the score, and updates the user's high score if they achieve a new personal best. It also displays the grand champion at the end.

    score = 0

    print("\n🎵 2016 Top Pop Songs Quiz 🎵")
    print("--------------------------------")

    for question in questions:
        print(f"\nWho sang '{question['song']}'?")

        for option in question["options"]:
            print(option)

        start_time = time.time() #I used this function to track how long it takes for the user to answer each question. If they answer within 5 seconds, they get a bonus!
    

        answer = input("Enter A, B, C, or D: ").upper()

        end_time = time.time()
        time_taken = end_time - start_time

        if answer == question["answer"]:
            print("Correct!")
            score += 10

            if time_taken <= 5:
                print("⚡ Fast bonus! +5 points")
                score += 5
        else:
            print("Wrong!")

    print("\nYour final score:", score)

    # Update personal high score
    if score > users[username]:  #This checks if the current score is higher than their previous best, and if so, it updates their high score in the users dictionary.
        print("🎉 New personal high score!")
        users[username] = score

    # Save updated users
    save_users(users)

    # Show grand champion
    champion, champ_score = get_grand_champion(users) #This function finds the user with the highest score across all users and returns their username and score. It uses the max() function with a key argument to find the user with the highest score.
    print("\n🏆 Grand Champion:", champion)
    print("Highest Score Ever:", champ_score)


# Run the quiz
run_quiz()
