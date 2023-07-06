'''
Task - Which Room?
----------------------

Write a program that asks the user for their name and which subject they are studying.
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to).  You should include at least 3 subjects and have a message such as 'I don't know which room that class is in' for any you don't include.
 Example - an input of 'Ben' and 'Computing' might get an output of 'Hi Ben, go to room 401 for Computing'


You may use any method taught in class that is appropriate for this task. There is room for interpretation.

'''
#Start coding below
name = input("What is your name? ")
subject = input("What subject are you studying? ")
if subject == "Math" or subject == "math":
  print(name + ", go to room 201 for " + subject + " class.")
elif subject == "English" or subject == "english":
  print(name + ", go to room 306 for " + subject + " class.")
elif subject == "Science" or subject == "science":
  print(name + ", go to room 223 for " + subject + " class.")
elif subject == "History" or subject == "history":
  print(name + ", go to room 411 for " + subject + " class.")
else:
  print("Sorry, " + name + ", I don't know where that class is.")