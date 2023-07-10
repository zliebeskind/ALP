# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encode(text, n):
  encoded = []
  for letter in text:
    pos = alpha.index(letter)
    if pos < (26 - n):
      encoded.append(alpha[pos + n])
    else:
      encoded.append(alpha[(pos - 26) + n])
  return "".join(encoded)


def caesar_decode(text, n):
  decoded = []
  for letter in text:
    pos = alpha.index(letter)
    if pos > (n - 1):
      decoded.append(alpha[pos - n])
    else:
      decoded.append(alpha[(pos + 26) - n])
  return "".join(decoded)


test = input("Text to encode (in all CAPS with no spaces): ")
shift = int(input("Shift (1 to 25): "))
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print("Encoded: " + enc)
print("Decoded: " + dec)
# If this worked, dec should be the same as test!