def get_character_frequencies (input_string):
    frequencies = {}
    
    for char in input_string:
        char = char.lower() #Convert to lowercase for case-sensitive counting
        if char in frequencies:
            frequencies[char] += 1
            print ("Got a new character:"+ char)
        else:
            frequencies[char] = 1
            
    return frequencies

mydict = get_character_frequencies("Snow white and the Seven Dwarfs")
print(mydict)
sorted_by_keys = dict(sorted(mydict.items()))
print("Sorted by keys:", sorted_by_keys)
