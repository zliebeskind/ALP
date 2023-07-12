# Read the instructions to see what you need to do here!
from math import ceil
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def vig_encode(text, keyword):
  encoded = []
  for i in range(len(test)):
    num = alpha.index(text[i]) + alpha.index(keyword[i])
    encoded.append(alpha[num % len(alpha)])
  return "".join(encoded)

def vig_decode(text, keyword):
  decoded = []
  for i in range(len(test)):
    num = alpha.index(text[i]) - alpha.index(keyword[i])
    decoded.append(alpha[num % len(alpha)])
  return "".join(decoded)

test = input("Enter message to encode: ").upper()
vig_key = input("Enter keyword: ").upper()

keyList = []
for i in range(ceil(len(test) / len(vig_key))):
  keyList.append(vig_key)
vig_key = "".join(keyList)

enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!