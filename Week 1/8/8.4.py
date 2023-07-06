'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''
weapons = ["sword", "gun", "magic staff", "mace"]
zombieWeakness = weapons[2]
action = "none"
print("A zombie ambushed you! What would you like to do?")
while action != "1" and action.lower() != "attack":
  print("1. Attack")
  print("2. Run")
  action = input()
  if action == "2" or action.lower() == "run":
    print("You couldn't get away! What would you like to do?")
  elif action == "1" or action.lower() == "attack":
    print("How do you want to attack?")
  else:
    print("Sorry, that's not an option. What would you like to do?")
print("1. Choose weapon from list")
print("2. Use a different weapon")

choice = "none"
weaponChoice = "none"

while choice != "1" and choice.lower() != "choose weapon from list"  and choice != "2" and choice.lower() != "use a different weapon":
  choice = input()
  if choice == "1" or choice.lower() == "choose weapon from list":
    while weaponChoice.lower() != weapons[0] and weaponChoice.lower() != weapons[1] and weaponChoice.lower() != weapons[2] and weaponChoice.lower() != weapons[3]:
      print("Choose an attack from the list: " + str(weapons))
      weaponChoice = input()
      if weaponChoice.lower() != weapons[0] and weaponChoice.lower() != weapons[1] and weaponChoice.lower() != weapons[2] and weaponChoice.lower() != weapons[3]:
        print("That's not an option.")
  elif choice == "2" or choice.lower() == "use a different weapon":
    print("Type the name of the weapon you want to use:")
    weaponChoice = input()
    if weaponChoice.lower() != weapons[0] or weaponChoice.lower() != weapons[1] or weaponChoice.lower() != weapons[2] or weaponChoice.lower() != weapons[3]:
     weapons.append(weaponChoice)
  else:
    print("That's not an option. How do you want to attack?")
    print("1. Choose weapon from list")
    print("2. Use a different weapon")

if weaponChoice.lower() == zombieWeakness:
  print("You won!")
else:
  print("You lost.")