celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd")

new_value = input("Enter a new celebrity: ")

celebs_list = list(celebs)   # Convert to list
celebs_list.append(new_value)

celebs = tuple(celebs_list)  # Convert back to tuple

print("Updated tuple:", celebs)