test = int(input("Enter a test mark between 0 and 100: "))
print("")
if test < 40 and test >= 0:
  fail = "True"
  print("Grade: U")
if test >= 40 and test < 70:
  fail = "False"
  print("Grade: C")
if test >= 70 and test < 80:
  fail = "False"
  print("Grade: B")
if test >= 80 and test < 100:
  fail = "False"
  print("Grade: A")
if test == 100:
  fail = "False"
  print("Grade: Perfect!")
if test < 0 or test > 100:
  print("Invalid grade input.")
  fail = "Unknown"

if fail == "True":
  print("FAIL, Retake Required")
else:
  if fail == "False":
    print("PASS")
  else:
    print("")