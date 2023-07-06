### Example Code 1

fName = "Mr"
lName = "Colley"

print(fName)

# Identify a variable in the code
 # Answer: fName and lName

# Identify a string in the code
 # Answer: "Mr" and "Colley"

# Line 4 is changed to lName = "Thorpe".  How does this affect the output?
 #Answer: It doesn't, because the output only prints fName, not lName

# Line 3 is changed to fName = "Mrs". How does this affect the output?
 # Answer: It will cahgne the output from Mr to Mrs


### Example Code 2

num1 = 20
num2 = 5

total1 = num1 + 15
total2 = num2 * 2
total3 = num1 - num2

print(total3)

# What will be output by the program?
 # Answer: 15


### Example Code 3

name1 = "Ross" 
name2 = "Monica" 
name3 = "Joey" 
name4 = "Rachel" 
name5 = "Chandler" 
 
print(name1 + " and " + name4) 
print(name3) 
 
name3 = "Phoebe" 


# How many variables are used in the program?
 # Answer: 5

# What would be the impact of changing  print(name1, " and ", name4) to print(name1, " and ", name5) ?
 # Answer: Instead of outputing Ross and Rachel, it will output Ross and Chandler

# What is the purpose of the '+' symbol in  print(name1, " and ", name4) 
 # Answer: It tells the computer to print name1, the word and, and name4

# The line  print(name3) is added to the end of the code.  Explain what it will do.
 # Answer: It will print Phoebe, because name3 is changed to Phoebe.

yourName = input("What is your name? ")
print("Hello, " + yourName + ".")