# Read the instructions to see what you need to do here!

alphaU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaL = "abcdefghijklmnopqrstuvwxyz"

def caesar_encode(text, n):
  encoded = []
  for letter in text:
    if letter not in alphaU and letter not in alphaL:
      encoded.append(letter)
    elif letter in alphaL:
      pos = alphaL.index(letter)
      pos += n
      pos %= 26
      encoded.append(alphaL[pos])
    else:
      pos = alphaU.index(letter)
      pos += n
      pos %= 26
      encoded.append(alphaU[pos])
  return "".join(encoded)


def caesar_decode(text, n):
  decoded = []
  for letter in text:
    if letter not in alphaU and letter not in alphaL:
      decoded.append(letter)
    elif letter in alphaL:
      pos = alphaL.index(letter)
      pos -= n
      pos %= 26
      decoded.append(alphaL[pos])
    else:
      pos = alphaU.index(letter)
      pos -= n
      pos %= 26
      decoded.append(alphaU[pos])
  return "".join(decoded)


test = input("Text to encode: ")
shift = int(input("Shift: "))
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print("Encoded: " + enc)
print("Decoded: " + dec)
# If this worked, dec should be the same as test!