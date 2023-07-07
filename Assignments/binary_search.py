low = 1 # sets the low value to 1
high = 100 # sets the high value to 100
answer = "none" # answer variable assigned a placeholder value to avoid an error when it's are called for the first time

def low_or_high():
  print("Was my guess:")
  print("1. too high?")
  print("2. too low?")
  position = input()
  if position == "1":
    global high # using global high and low variables allows them to be used outside of this subroutine
    high = (guess - 1) # if the guess was too high, the new highest possible value is the guess minus 1
  elif position == "2":
    global low
    low = (guess + 1) # if the guess was too low, the new lowest possible value is the guess plus 1
  else:
    print("Invalid input.")
    low_or_high() # if the user inputs something other than "1" or "2", the program displays "Invalid input." and restarts the low_or_high() function

def guess_num():
  print("Is your number " + str(guess) + "? (Y/N)")
  global answer # using a global answer variable allows it to be used outside of this subroutine
  answer = input()
  if answer.lower() == "y": # answer.lower() converts answer into all lowercase, meaning this if statement will accept both "y" and "Y"
    print("I knew it!")
  elif answer.lower() == "n":
    global position
    low_or_high() # if the computer was wrong on its guess, it calls the low_or_high() subroutine
  else:
    print("Invalid input.")
    guess_num() # if the user inputs something other than "Y" or "N", the program displays "Invalid input." and restarts the guess_num() function

print("Think of a whole number between 1 and 100. I can guess it in 7 guesses or less.")
while answer.lower() != "y": # this block of code repeats until the program guesses correctly
  guess = (low + high) // 2 # sets guess (mid) to be inbetween low and high, using floor division to not output decimal values
  guess_num() # calls the guess_num() subroutine

