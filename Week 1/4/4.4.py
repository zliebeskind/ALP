# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)

print("Area and Perimeter of a Rectangle:")
print()
rectHeight = float(input("Height = "))
rectWidth = float(input("Width = "))
area = rectHeight * rectWidth
perimeter = (rectHeight + rectWidth) * 2
print()
print("Area = " + str(area))
print("Perimeter = " + str(perimeter))
print()
print()

print("Resteraunt Tip Calculator:")
print()
price = float(input("Price: $"))
tip = round(price * 0.2, 2)
totalPrice = round(price + tip, 2)
print()
print("Tip: $" + str(tip))
print("Total Price: $" + str(totalPrice))
print()
print()

print("Volume and Surface Area of a Cuboid:")
print()
cuboidHeight = float(input("Height = "))
cuboidWidth = float(input("Width = "))
cuboidLength = float(input("Length = "))
volume = cuboidHeight * cuboidWidth * cuboidLength
surfArea = ((cuboidHeight * cuboidWidth) + (cuboidWidth * cuboidLength) + (cuboidHeight * cuboidLength)) * 2
print()
print("Volume = " + str(volume))
print("Surface Area = " + str(surfArea))

'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''