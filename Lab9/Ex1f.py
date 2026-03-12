# Open the file names.txt, read its contents, and print the number of names
# Append a new name at the end of the file.

file_path = "Lab9/names.txt"

# Read and print initial contents
with open(file_path, "r") as file_object:
    contents_list = file_object.readlines()
    print("Initial file contents:")
    print(contents_list)
    print(f"Number of names: {len(contents_list)}")

# Append a new name
with open(file_path, "a") as file_object:
    print("Appending a new name to the file...")
    file_object.write("Beverly Mambou\n")

# Read and print contents after appending
with open(file_path, "r") as file_object:
    updated_contents = file_object.readlines()
    print("\nFile contents after appending:")
    print(updated_contents)
    print(f"Number of names: {len(updated_contents)}")
