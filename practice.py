clue = {}

def PrettyPrint():
  print()
  for keys, values in clue.items():
    print(keys, end=": ")
    for subkey, subvalue in values.items():
      print (subkey, subvalue, end = " | ")
    print()

while True:
  name = input("Enter a name: ")
  location = input("Enter a location: ")
  weapon = input("Enter a weapon: ")
  clue[name] = {"location":location, "weapon":weapon}

  PrettyPrint()