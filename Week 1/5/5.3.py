# Starter Code

number = 5 # Sets the variable number to 5
print("I have thought of a number between 1 and 10") # prints the text on screen
guess = int(input("Can you guess what it is?")) # asks the player to guess the number, takes input, and assigns the input as an integer to the variable guess


if guess < number: # checks if the number guessed is too low
  print("Too Low!") # if the previous condition is true, it will print "Too Low!"
if guess > number: # checks if the number guessed is too high
  print("Too High!") # if the previous condition is true, it will print "Too High!"

