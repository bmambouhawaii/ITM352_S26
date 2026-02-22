celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Angelina Jolie")
ages = (36, 38, 36, 61, 50)

#Convert tuples to lists directly
celebs_list = list(celebs)
ages_list = list(ages)

#create dictionary
celebs_dict = {"celebrities": celebs_list, "ages": ages_list}

print(celebs_dict)
