#Create a first simple visualization
import matplotlib.pyplot as plt

# a. Define x and y values
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# d. Second set of values
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

# b. Line graph
plt.plot(x, y)

# c. Scatter plot
plt.scatter(x, y)

# d. Add second line
plt.plot(x2, y2)

# e. Title and labels
plt.title("Simple Visualization")
plt.xlabel("X values")
plt.ylabel("Y values")

# Show the graph
plt.show()