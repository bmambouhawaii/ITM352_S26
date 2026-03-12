#Open the files names.txt and read its contents and print the number of names.

with open("Lab9/names.txt") as file_object:
    while(line := file_object.readline()):
        print(line.strip()) #use strip to remove the newline character at the end of each line

