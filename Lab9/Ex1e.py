#Open the files names.txt and read its contents and print the number of names.

import os
print("Current working directory:", os.getcwd())
file_object = open("Lab9/names.txt")
contents_list = file_object.readlines()
print(contents_list)
print(f"Number of names: {len(contents_list)}")
file_object.close()