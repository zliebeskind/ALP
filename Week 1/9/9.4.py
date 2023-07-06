def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2

options = ["add", "subtract", "multiply", "divide"]
operations = ["plus", "minus", "times", "divided by"]
print("Input a number for the corresponding operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input())
print("Input two numbers to " + options[choice - 1] + ":")
input1 = float(input("1: "))
input2 = float(input("2: "))
if choice == 1:
  print(str(input1) + " " + operations[choice - 1] + " " +     str(input2) + " equals " + str(add(input1, input2)) + ".")
if choice == 2:
  print(str(input1) + " " + operations[choice - 1] + " " +     str(input2) + " equals " + str(subtract(input1, input2)) + ".")
if choice == 3:
  print(str(input1) + " " + operations[choice - 1] + " " +     str(input2) + " equals " + str(multiply(input1, input2)) + ".")
if choice == 4:
  print(str(input1) + " " + operations[choice - 1] + " " +     str(input2) + " equals " + str(divide(input1, input2)) + ".")