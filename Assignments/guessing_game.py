# Players have to guess the correct number within 7 attempts
import random
answer = random.randrange(1, 100)
guess = None
tries = 0
name = input("Enter your name: ")
while guess != answer:
  guess = int(input("Guess a number between 1 and 100: "))
  if guess > answer and guess <= 100:
    print("Too high!")
    tries += 1
  elif guess < answer and guess >=1:
    print ("Too low!")
    tries += 1
  elif guess < 1 or guess > 100:
    print("Invalid number input.")
print("Congratulations, " + name + ", you guessed the number in " + str(tries + 1) + " guesses!")