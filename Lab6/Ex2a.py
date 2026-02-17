#Create a list with different values
my_list = [1, 2, 3, 4, 5, 6]

def check_list_length(lst):
    if len(lst) < 5:
        return "Fewer than 5"
    elif 5 <= len(lst) <= 10:
        return "Between 5 and 10"
    else:
        return "More than 10"

# Test cases
test_lists = [
    [1, 2],
    [1, 2, 3, 4, 5],
    list(range(12))
]

for lst in test_lists:
    print(f"{len(lst)} elements: {check_list_length(lst)}")