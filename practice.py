

import random, os, time

import os, time, random
def add():
  os.system("clear")
  idea = input("Idea > ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  time.sleep(1)
  os.system("clear")
def show():
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")
while True:
  menu = input("1: Add idea\n2: Show a random idea\n> ")
  if menu == "1":
    add()
  else:
    show()

myEvents = {}

def prettyPrint ():
    for row in myEvents:
      print (f"{row[0] :15^}. {row[1] : 15^}")
    print()

while True:
    menu = input("1. Add Event\n2 Delete Event\n")
    if menu == "1":
       event = input("Enter Event: ")
       date = input("Enter Date: ")
       row = [date, event]
       myEvents.append(row)
       prettyPrint()
    else:
       criteria = input ("Enter event you want to delete")
       for row in myEvents:
           if criteria in row:
               myEvents.remove(row)

    f = open("events.txt","w")
    f.write(str(myEvents))
    f.close()