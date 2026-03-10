# Open a text file and print its type

import os
print("Current working directory:", os.getcwd())
file_object = open("Lab9/names.txt")

print(type(file_object))
file_object.close()