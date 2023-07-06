number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = int(input())
print("You guessed it!")

# Give the line number where iteration starts.
  # Answer: 4

# What does '!=' mean?
  # Answer: not equal to

# How many variables are there in the code?
  # Answer: 2

# How can you tell which lines of code are inside the loop?
  # Answer: they are indented

# How many times will the loop repeat?
  # Answer: until the user guesses it correctly

# What has to happen to make the program run the last line of code?
  # Answer: the user has to guess the number correctly

# Task 3
secret = 5
guess = int(input("I'm thinking of a number between 1 and 10, can you guess it? "))
while guess != secret:
  print("Incorrect! Try again!")
  guess = int(input())
print("That was it, congratulations!")