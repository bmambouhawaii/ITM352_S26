celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd")

new_value = input("Enter a new celebrity: ")

try:
    celebs.append(new_value)
except Exception as e:
    print("An attempt was made to append a value to the tuple.")
    print("Error:", e)