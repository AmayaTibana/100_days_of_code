"""import random, os, time

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

"""

import time, os
score = {}
while True:
  add = input("Add a new score? (y/n): > ")
  if add == "n":
    break
  f = open("score.txt", "a+")
  user_initials = input("Enter user initials: > ").upper()
  userscore = input("Enter user score: >  ")
  f.write(f"{user_initials} {userscore}\n")
  f.close()
  print("ADDED")
  time.sleep(1)
  os.system("clear")

