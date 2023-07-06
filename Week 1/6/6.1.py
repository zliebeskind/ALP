# Example code 1

number = 7 # sets variable number to 7
print("I have thought of a number between 1 and 10") # prints the text "I have throught of a number between 1 and 10"
guess = int(input("Can you guess what it is?")) # prints the text "Can you guess what it is?" and asks for input which it sets as the variable guess

if guess == number: # checks if the variable guess and the variable number are the same
  print("Correct!") # if the previous condition is true, it prints "Correct!"
elif guess < number: # checks if guess is less than number
  print("Too Low!") # if the previous condition is true, it prints "Too Low!"
else:
  print("Too High!") # if none of the previous conditions are true, it prints "Too High!"

# Example code 2

number1 = int(input("Please enter a number")) # prompts the user to input a number and stores it as number1
number2 = int(input("Please enter another number")) # prompts the user to input a number and stores it as number2

if number1 > number2: # checks if number1 is bigger tham number2
  print("Number 1 is bigger than number 2") # if the previous condition is true, it prints "Number 1 is bigger than number 2"
elif number2 > number1: # checks if number2 is bigger tham number1
  print("Number 2 is bigger than number 1") # if the previous condition is true, it prints "Number 2 is bigger than number 1"
else:
  print("Both numbers are the same") # if none of the above conditions are true, it prints "Both numbers are the same"

