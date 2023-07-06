# Example code 1

age = 18 
 
if age > 18: 
 print("You are old enough to drive") # if the value of the age variable is greater than 18, it will say: "You are old enough to drive" Because the condition is false, it will display nothing.

# Example code 2

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") # if the value of num1 is equal to 10, it will say "This text is output because the condition was true", but if not, it will say "This tect is output because the condition was false". Because the condition is false, it will display the second message

# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
# the program asks the user to guess the variable number and uses branches to display different messages if different conditions are met. If the guess is too low, it will say "Too Low!" If it is too high, it will say "Too High!" If it is correct, it will say "Correct!"