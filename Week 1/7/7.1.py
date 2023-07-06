# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?") # prints the text
answer = input() # asks for user input and sets it as variable answer

while answer != "Paris": # tells the computer to repeat this code until answer = "Paris"
  print("Incorrect! Try again.") # if the user gets the question wrong, it displays this text
  answer = input("What is the capital of France?") # asks the question again if the user gets it wrong

print("Correct!") # if the user gets the question correct, it displays this text

# Example code 2

counter = 1 # assigns variable counter to 1

while counter < 5: # tells the computer to repeat this code until counter is 5
  print("This code is inside the loop") # prints text if counter is less than 5
  counter += 1 # increases counter by 1