import json

Questions = [
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

filename = "questions.json"

with open(filename, "w") as jsonfile:
    json.dump(Questions, jsonfile)