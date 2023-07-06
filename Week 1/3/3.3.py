name = input("What's your name? ") #changed name = "Billy" to an input command to ask for the user's name
print()
print("We want to know if you like progamming!")
print()
answer = input("Do you like programming, " + name + "? ") #combined the "Do you like programming" and answer = input() lines into one input command
print("Great, " + name + "! You said " + answer + "!") #added the name variable to the sentence so it reads: "Great, name! You said answer!" replacing name and answer with their values
print("Let's learn some Python today")