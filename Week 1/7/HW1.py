'''
Task Instructions
You are going to write a program called "Time Reminder"

The user has to enter a number between 0 and 23
If the number is less than 8 display a message saying "too early to get up"
If the number is less than 12 display a message saying "Good morning"
If the number is less than 14 display a message saying "Lunch time!"
If the number is less than 18 display a message saying "Good afternoon"
If the number is equal to 18 display a message saying "Tea Time"
If the number is less than 19 display a message saying "Good evening"
If the number is less than 22 display a message saying "Nearly bedtime"
If the number is 23 display a message saying "Good night!"
Any other number is met with the response “Sorry, I don’t recognise that”


You are free to use any of the methods that we have learned in class.
'''
#Start coding below this line
time = float(input("Enter a number from 0 to 23: "))
if time < 8 and time >= 0:
  print("too early to get up")
elif time < 12 and time >= 0:
  print("Good morning")
elif time < 14 and time >= 0:
  print("Lunch time!")
elif time < 18 and time >= 0:
  print("Good afternoon")
elif time == 18:
  print("Tea Time")
elif time < 19 and time >= 0:
  print("Good evening")
elif time <= 22 and time >= 0:
  print("Nearly bedtime")
elif time == 23:
  print("Good night!")
else:
  print("Sorry, I don't recognize that")