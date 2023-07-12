# Read the instructions to see what you need to do here!
from random import shuffle

alpha = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "

def sub_encode(text, codebet):
  encoded = []
  for letter in text:
    encoded.append(codebet[alpha.index(letter)])
  return "".join(encoded)

def sub_decode(text, codebet):
  decoded = []
  for letter in text:
    decoded.append(alpha[codebet.index(letter)])
  return "".join(decoded)

print("What do you want to do?")
print("1. Encode")
print("2. Decode")
choice = input()

if choice == "1":
  print("1. Encode with key")
  print("2. Use random key")
  choice = input()
  
  if choice == "1":
    test = input("Text to encode: ")
    cipher_alphabet = input("Key: ")
    
  elif choice == "2":
    test = input("Text to encode: ")
    cipher_alphabet = list(alpha)
    shuffle(cipher_alphabet)
    cipher_alphabet = "".join(cipher_alphabet)

  enc = sub_encode(test, cipher_alphabet)
  dec = sub_decode(enc, cipher_alphabet)
  print("Encoded: " + enc)
  print("Decoded: " + dec)
  if choice == "2":
    print ("Key: " + cipher_alphabet)

elif choice == "2":
  test = input("Text to decode: ")
  cipher_alphabet = input("Key: ")
  dec = sub_decode(test, cipher_alphabet)
  print("Decoded: " + dec)
# If this worked, dec should be the same as test!