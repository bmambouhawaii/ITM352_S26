first= input ("Enter your first name: ")
middle= input ("Enter your middle initial: ")
last= input ("Enter your last name: ")

#a)concantenation
print (first + " " + middle + ". " + last)

#b)using f-strings
print (f"{first} {middle}. {last}")

#c) % operator
print ("%s %s. %s" % (first, middle, last))

#d) format() method
print ("{} {}. {}".format(first, middle, last))

#e) join() method
print (" ".join([first, middle + ".", last]))

#f) format with unpacking
print ("{} {}. {}".format(first, middle, last))

