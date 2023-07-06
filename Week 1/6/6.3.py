# Starter Code

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
number3 = int(input("Please enter another number"))

if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
else:
  print("Numbers 1 and 2 are the same")

if number1 > number3:
  print("Number 1 is bigger than number 3")
elif number3 > number1: 
  print("Number 3 is bigger than number 1")
else:
  print("Numbers 1 and 3 are the same")

if number2 > number3:
  print("Number 2 is bigger than number 3")
elif number3 > number2: 
  print("Number 3 is bigger than number 2")
else:
  print("Numbers 2 and 3 are the same")