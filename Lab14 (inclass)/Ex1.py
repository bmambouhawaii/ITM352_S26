import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 3, 3, 3.5, 4]

#Plot these values as a line graph
plt.plot(x_values, y_values)
plt.scatter(x_values, y_values, color='red') #Add red dots to the graph

# Now add in a second set of x,y values
other_x= [1, 2, 3, 4]
other_y= [2, 4, 6, 8]
plt.plot(other_x, other_y, color='green') #Add a green line to the graph

plt.show()