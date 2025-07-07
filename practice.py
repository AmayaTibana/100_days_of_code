import random, os, time

mokedex = {}

def prettyPrint():
  print()
  for keys, values in mokedex.items():
    print(keys, end= ": ")
    for subkey, subvalue in values.items():
      print(subkey, subvalue, end= " | ")
    print()

while True:
  name = input("Enter the beast's name: ")
  element = input("Enter the beast's element: ")
  move = input("Enter the beast's move: ")
  hp = input("Enter the beast's HP: ")
  mp = input("Enter the beast's MP: ")
  mokedex[name] = {"element":element, "move":move, "hp":hp, "mp":mp}
  
  prettyPrint()

