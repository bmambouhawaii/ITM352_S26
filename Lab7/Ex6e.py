celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd")

new_value = input("Enter a new celebrity: ")

celebs = (*celebs, new_value)

print("Updated tuple:", celebs)