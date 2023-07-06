# Example Code 1

def say_hi():
  print("Why hello there!") # defines say_hi() to print "Why hello there!"

def offer_drink():
  print("Would you care for a spot of tea?") # defines offer_drink() to print "Would you care for a spot of tea?"

def offer_food():
  print("Biscuit?") # defines offer_food() to print "Buscuit?"

def say_bye():
  print("Cheerio then.") # defines say_bye() to print "Cheerio then."


offer_drink() # calls the offer_drink() subroutine
say_hi() # calls the say_hi() subroutine
offer_food() # calls the offer_food() subroutine

# Example code 2
def maths1():
  num1 = 50 # assigning variable
  num2 = 5 # assigning variable
  return num1 + num2 # tells the subroutine to return num1 + num2

def maths2():
  num1 = 50 # assigning variable
  num2 = 5 # assigning variable
  return num1 - num2 # tells the subroutine to return num1 - num2

def maths3():
  num1 = 50 # assigning variable
  num2 = 5 # assigning variable
  return num1 * num2 # tells the subroutine to return num1 * num2

outputNum = maths2() # assigns variable outputNum to the value returned by maths2()
print(outputNum) # prints outputNum

# Example Code 3
def location(country): # defines subroutine location with argument country
  print("I am from " + country) # tells the subroutine to print "I am from " plus the argument

location("Brazil") # runs the location subroutine with argument "Brazil"

