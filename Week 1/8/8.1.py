'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",] # sets the variable Sentence to the list
print(Sentence) # prints Sentence, which is the list
print(Sentence[1]) # prints the first item in the list
Sentence.append("life") # adds "life" to the end of the list
Sentence[4] = "sunny" # changes the item with index 4 from bright to sunny
print(Sentence[4]) # prints the item with index 4 in the list, which is sunny
print(Sentence[0] + " " + Sentence[3]) # prints item with index 0, a space, and item with index 3
print(Sentence) # prints the list with life added and bright replaced with sunny