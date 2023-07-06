'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''
name = input("What's your name? ")
print()
food = input("Hi, " + name + ", nice to meet you. What's your favorite food? ")
print("I like " + food + " too, " + name + "!")
print()
activity = input("What do you like to do in your free time? ")
print("That sounds like fun, " + name + ".")
print()
color = input("What's your favorite color? ")
print("That's a nice color, " + name + ".")
print()
print(name + ", your favorite food is " + food + ", you like to")
print(activity + " in your free time, and your favorite color is " + color + ".")