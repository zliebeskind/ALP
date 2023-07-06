'''
Cubes Cubes Cubes
------------------

The cubed number sequence starts: 1, 8, 27, 64, 125...
Write a program that:
		 	 	 		
Asks the user to input a number.
Display N numbers in the cubed sequence according to user input. 
				
You may use any of the methods taught in class. The promt is quite brief so there is room for interpretation as to how to accomplish this task. 

'''
#Start coding below this line
n = int(input("Enter a number: "))
counter = 1
while counter < (n + 1):
  print(counter**3)
  counter += 1