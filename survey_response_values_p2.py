#create the list
responses = [5, 7, 3, 8]

#append 0 to the end of the list
responses.append(0)

#insert 6 between 7 and 3
responses.insert(2, 6)

#print the updated list
print(responses)

# Create the original list again
responses = [5, 7, 3, 8]

# Add 0 to the end using +
responses = responses + [0]

# Insert 6 between 7 and 3 using slicing
responses = responses[:2] + [6] + responses[2:]

# Print the updated list
print(responses)