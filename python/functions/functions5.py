# Exercise: Implement a function that
#  calculates the area of a rectangle

# Write a function called 
# calculate_rectangle_area() 
# that takes two parameters, 
# width and height.
#
# Inside the function, write the 
# necessary code to calculate the
#  area of a rectangle, which is 
# width * height.
# Return the calculated area.

# Write a function called 
# get_user_input() that takes 
# no parameters.
# Inside the function, prompt 
# the user to enter the width 
# and height of the rectangle
# Use the input() function to 
# get the user's input and store
# it in two variables.
# Convert the user input to integers.

# Call the get_user_input() function
#  and store the returned values in 
# variables width_input and height_input.
# Call the calculate_rectangle_area() 
# function with width_input and 
# height_input as arguments.
# Store the returned result in
# a variable called area.
# Print the calculated area using 
# the print() function and provide 
# a suitable message.

# Test your code by running the program 
# and entering different values for 
# width and height.

# Write the two required functions here.
# Hint: Return two values with: return x, y
#  Two values can be assigned:
#  alice, bob = call_function()


# Call the get_user_input() function and
# store the returned values in variables
# width_input and height_input
width_input, height_input = get_user_input()

# Call the calculate_rectangle_area() 
# function with width_input and 
# height_input as arguments
# Store the returned result in 
# a variable called area
area = calculate_rectangle_area(width_input, height_input)

# Print the calculated area using the
# print() function and provide a 
# suitable message
print("The area of the rectangle is:", area)
