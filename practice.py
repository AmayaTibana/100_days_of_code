<<<<<<< HEAD
""" # Rock, Paper, Scissors Game first project ever.
from getpass import getpass as input
=======
# Rock, Paper, Scissors Game first project ever.
"""from getpass import getpass as input
>>>>>>> da81bb08edb0f20ff772ae8baa51f0bf62615016
"""
print("Rock, Paper, Scissors, Game!")
print()
print("Select your move Rock, Paper, Scissors")

player1_score = 0
player2_score = 0

while True:
    player1_move = input("Player 1, make your move: ")
    player2_move = input("Player 2, make your move: ")

    if (player1_move == "Rock"):
        if (player2_move == "Rock"):
            print("It's a tie!")
        elif (player2_move == "Paper"):
            print("Player 1 loss and Player 2 win! Rock is covered by Paper")
            player2_score += 1
        elif (player2_move == "Scissors"):
            print("Player 1 wins and Player 2 loss! Rock breaks Scissors")
            player1_score += 1
    elif (player1_move == "Paper"):
        if (player2_move == "Paper"):
            print("It's a tie!")
        elif (player2_move == "Scissors"):
            print("Player 1 loss and Player 2 win! Paper is cut by Scissors")
            player2_score += 1
        elif (player2_move == "Rock"):
            print("Player 1 wins and Player 2 loss! Paper covers Rock")
            player1_score += 1
    elif (player1_move == "Scissors"):
        if (player2_move == "Scissors"):
            print("It's a tie!")
        elif (player2_move == "Rock"):
            print("Player 1 loss and Player 2 win! Scissors is broken by Rock")
            player2_score += 1
        elif (player2_move == "Paper"):
            print("Player 1 wins and Player 2 loss! Scissors cuts Paper")
            player1_score += 1
        # This should be the gam now have to print the score
    print("Player 1 score: ", player1_score)
    print("Player 2 score: ", player2_score)
    if (player1_score == 3 or player2_score == 3):
        print("Thanks for playing!")
    else:
        continue """

<<<<<<< HEAD



"""#practice with strings
mystring = "Hello there my friend"
print (mystring.split()[0:5:1])


myString = "Hello there my friend."
print(myString[0:11:1]) """ 
#This code will print everything in reverse
""" myString = "Hello there my friend."
print(myString[::-1])

#This code will print each word as a seperate string and not single characters, split() will make it work this way

 myString = "Hello there my friend!"
print(myString.split()) 

#Start Wars Name Generator (Project 1 ) it could land to some errors if the user inputs less than 4 words

 print ("Start Wars Name Generator")

all = input("Enter your first name, last name, mum's maiden name and city of birth: ").split()

first = all[0]
second= all[1]
maiden = all[2]
city = all[3]

name = f"{first[:3].title()} {second[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}") 

#Another solution to the problem could be this

 print ("start wars name generator")
=======
#Todo List Small project

import os, time, sys, random

print (" Welcome to the to do list!")

myList = []
def printList():
  print()
  for item in myList:
    print(item)
  print()

while True:
   print()
   menu = input ("view, add or edit the list:  ")
   if menu == "view":
     printList()
     time.sleep(2)
     os.system("clear")
   elif menu == "add":
     item = input("What do you want to add?: ")
     myList.append(item)
     time.sleep(2)
     os.system("clear")
   elif menu == "edit":
    item = input ("What do you want to remove?: ")
    if item in myList:
      myList.remove(item)
      time.sleep(2)
      os.system("clear")
    else:
      print(f"{item} was not in the list") """

#Another solution to the problem could be this
""""
print ("start wars name generator")
>>>>>>> da81bb08edb0f20ff772ae8baa51f0bf62615016

first = input("Enter your first name: ").strip()
second = input("Enter your last name: ").strip()
maiden = input("Enter your mum's maiden name: ").strip()
city = input("Enter your city of birth: ").strip()

name = f"{first[:3].title()} {second[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print (f"Your Star Wars name is {name}") """

#This is the end of the project startwars name generator 
<<<<<<< HEAD
#hello world 
=======

>>>>>>> da81bb08edb0f20ff772ae8baa51f0bf62615016
"""
print ("Start Wars Name Generator")

all = input("Enter your first name, last name, mum's maiden name and city of birth: ").split()

first = all[0]
second = all[1]
maiden = all[2]
city = all[3]

all= f"{first[:3].title()} {second[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"your Star Wars name is {all}")

# Hangman Game
# Hangman Game
# Hangman Game
import random, os, time

listOfWords = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
lettersGuessed = []
lives = 6

word = random.choice(listOfWords)

while True:
    time.sleep(2)
    os.system("clear")
    letter = input("Guess a letter: ").lower()

    if letter in lettersGuessed:
        print("You already guessed that letter!")
        continue

    lettersGuessed.append(letter)

    if letter in word:
      print ("Correct! you guessed a letter!")
    else:
      print ("Incorrect! you lost a life!")
      lives -= 1

    allLetters = True
    print ()
    for i in word:
        if i in lettersGuessed:
            print (i, end="")
        else:
            print ("_", end="")
            allLetters = False
    print ()

    if allLetters:
        print (f"you won with {lives} lives remaining!")
        break
    if lives <= 0:
        print (f"You ran out of lives! The word was {word}")
        break
    else:
        print (f"You have {lives} lives remaining!")

myUser = { "name": "Amaya", "age": 30, "city": "New York"}


myUser["name"] = "The Legedary Amaya"
print(myUser["name"])

name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}
"""print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")
print(f"your Star Wars name is {all}")"""
""" # This is the end of the Hangman Game

#day 40

""" myUser = { "name": "Amaya", "age": 30, "city": "New York"}


myUser["name"] = "The Legedary Amaya"
print(myUser["name"])

myUser = { "name": "Amaya", "age": 30, "city": "New York"}

print(f"My name is {myUser['name']}") 

myUser = {"name":"Andy" ,"age": 129}
print {myUser["name"]} """

#contact card using a dictionary
print ("Contact card using a dictionary")
print ()

name = input ("Enter your name: ").strip().capitalize()
date = input ("Enter your date of birth: ").strip()
phone = input ("Enter your phone number: ").strip()
email = input ("Enter your email: ").strip()
address = input ("Enter your address: ")

contact = {"name": name, "date": date, "phone": phone, "email": email, "address": address}

print ()
print (f"""Name: {contact["name"]}""")
print (f"""Phone: {contact["phone"]}""")
print(f"""Address: {contact["address"]}""")
print(f"""Date of Birth: {contact["date"]}""")
print(f"""Email: {contact["email"]}""")

#dictionary practice
print ("Dictionary practice")
myDictionary = {"name": "John", "age": 30, "city": "New York"}
myDictionary["name"] = "Amaya"

for name, value in myDictionary.items():
    print(f"{name}: {value}")
    if value == "Amaya":
        print("Hello Amaya")
print ()

myDictionary2 = {"name": "John", "age": 30, "city": "New York"}
for x, y in myDictionary2.items():
  print(f"{x}, {y}") 

print () # blank line
myDictionary3 = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
for name, value in myDictionary3.items():
  print(f"{name}, {value}")


## Website Rating Program

website = {"name": None, "url": None, "desc": None, "rating": None}
for name in website.keys():
  website[name] = input(f"{name}: ")
print()
for name, value in website.items():
  print(f"{name}: {value}")

# MokeBeast Project game 
import time, os, sys, random 
print("MokeBeast")

MokeBeast = {"Beast Name": None,
             "Beast Type": None,
            "Special ability": None,
             "HP":None,
             "MP": None
            }
print()

for name, value in MokeBeast.items():
    MokeBeast[name] = input(f"Enter {name}:\t ").strip().title()
  
if MokeBeast["Beast Type"] == "water" or MokeBeast ["Beast Type"] == "Water":
  print ("\033[47m" , end="")

elif MokeBeast ["Beast Type"] == "fire" or MokeBeast["Beast Type"] == "Fire":
  print ("\033[41m" , end="")
elif MokeBeast ["Beast Type"] == "earth" or MokeBeast ["Beast Type"] == "Earth":
  print ("\033[42m" , end="")
elif MokeBeast ["Beast Type"] == "air" or MokeBeast["Beast Type"] == "Air":
  print ("\033[43m" , end="")
else:
  print ("\033[33m" , end="")
  
print()
for name, value in MokeBeast.items():
    print(f"{name} : {value}")

# This is the end of the MokeBeast Project game

#Bingo Game project 

"""#practice
my2DList = [[3,2,5],
            [2,3,4],
            [1,44,23]]

print (my2DList[0][2])

#practice 2
List = [["Amaya, 30, Mac"],
        ["Natalia, 29, Windows"],
        ["Lalatina, 1, Playstation"]]

List[0] = "Brownie"

print (List[0:2])"""

#fix code 

"""my2DList = [["Johnny", 21, "Mac"],
            ["Sian" , 19, "PC"],
            ["Gethin", 17, "PC"]]


print(my2DList[0][1])
"""

import random
bingo = []

def ran():
    number = random.randint(1, 90)
    return number

def prettyPrint():
    for row in bingo:
        print(row)

numbers = []
for i in range (8):
  numbers.append(ran())

numbers.sort()
bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]
prettyPrint() 

#List of winners 

listOfWinners = []

def prettyPrint():
   print()
   for row in listOfWinners:
     for item in row:
      print(f"{item:^10}", end=" |")
     print()
   print()


while True :
   name = input("Enter a name: ")
   age = input("Enter age: ")
   pref = input("Enter your system of preference: ")
   row = (name, age, pref)
   listOfWinners.append(row)
   exit = input("Do you want to exit? (y/n): ")
   if (exit.strip().lower()[0] == "y"):
      break

prettyPrint()



# This is the end of the Bingo Game project 


import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
ħ = 1.0     # Reduced Planck constant
m = 1.0     # Particle mass

# Space and time settings
N = 1000             # Number of spatial points
L = 100.0            # Spatial domain length
dx = L / N
x = np.linspace(-L/2, L/2, N)
dt = 0.005           # Time step
steps = 1000         # Time steps to simulate

# Potential (e.g., infinite square well or barrier)
V = np.zeros(N)
V[np.abs(x) > 20] = 1e6  # Infinite walls

# Initial wave packet (Gaussian)
x0 = -10.0               # Initial center
k0 = 5.0                 # Initial momentum
sigma = 1.0              # Width
psi0 = (1 / (np.pi * sigma**2)**0.25) * np.exp(1j * k0 * x) * np.exp(-(x - x0)**2 / (2 * sigma**2))
psi = psi0.copy()

# Normalize
def normalize(ψ):
    return ψ / np.sqrt(np.sum(np.abs(ψ)**2) * dx)

psi = normalize(psi)

# Crank–Nicolson matrices
main_diag = 1 + 1j * ħ * dt / (2 * m * dx**2) + 1j * dt * V / (2 * ħ)
off_diag = -1j * ħ * dt / (4 * m * dx**2) * np.ones(N - 1)

A = sp.diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csr')
B = sp.diags([-off_diag, 1 - main_diag, -off_diag], [-1, 0, 1], format='csr')

# Setup plot
fig, ax = plt.subplots()
line, = ax.plot(x, np.abs(psi)**2, lw=2)
ax.set_xlim(-L/2, L/2)
ax.set_ylim(0, 0.5)
ax.set_title("Time Evolution of $|\psi(x,t)|^2$")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")

def update(frame):
    global psi
    rhs = B @ psi
    psi = spla.spsolve(A, rhs)
    psi = normalize(psi)
    line.set_ydata(np.abs(psi)**2)
    return line,

ani = FuncAnimation(fig, update, frames=steps, interval=50)
plt.show()



# this is the end of the Quantum Mechanics Simulation project

# Function decorator that times execution
from time import time

def timer(func):
    # Nested wrapper function
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Duration: {end-start}")
    return 


list = [[]for _ in range(4)]
list[-1].append(4)
print(list)


list = [[] for _ in range(6)]
list[2].append(4)
print(list)


list = [[] for _ in range(4)]
list[3].append(4)
print(list)


list = [[] for _ in range(6)]
list[2].append(5)
print(list)

name = "beethoven"
letters = list(name)
letters

#commited by Amaya
def timer(func):
    # Nested wrapper function
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Duration: {end-start}")
    return wrapper

listOfWinners = []

def prettyPrint():
   print()
   for row in listOfWinners:
     for item in row:
      print(f"{item:^10}", end=" |")
     print()
   print()


while True :
   name = input("Enter a name: ")
   age = input("Enter age: ")
   pref = input("Enter your system of preference: ")
   row = (name, age, pref)
   listOfWinners.append(row)
   exit = input("Do you want to exit? (y/n): ")
   if (exit.strip().lower()[0] == "y"):
      break

prettyPrint() 

#small practice with dictionaries 

pet_info = { 'Name': 'Charlie', 
             'Species': 'Dog'}
pet_info.get(0)

s1 = set (range(3))
print (s1)


s2= set(range(5))

s3 = set([1, 2, 3, 4, 5])
s3


listOfWinners = []
def prettyPrint():
    print()
    for row in listOfWinners:
        for item in row:
          print(f"{item:^10}", end=" | ")
        print() 
    print()

while True:
   name = input("Who is the winner? ")
   age = input("What is their age? ")
   pref = input("What is their computer platform? ")
   row = [name,age, pref]
   print()
   
   listOfWinners.append(row)
   exit = input("Would you like to exit? ")
   if (exit.strip().lower()[0] == "y"):
      break
   
prettyPrint()
# This is the end of the practice.py file



listOfShame = [] 

menu = input("Add or Remove?") 

if(menu.strip().lower()[0]=="a"): 
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    row = [name, age, pref] 
    listOfShame.append(row) 
else: 
    name = input("What is the name of the record to delete?") 

    if name in listOfShame: 
      for row in name:
        listOfShame.remove(row) # remove the whole row if name is in it

print(listOfShame)


# This is the end of the practice.py file


import random, os, time
bingo = []
def ran():
  number = random.randint(1,90)
  return number
def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()
def createCard():
  global bingo
  numbers = []
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())

  numbers.sort()

  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BG", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]
createCard()
while True:
  prettyPrint()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        bingo[row][item] = "X"
  exes = 0
  for row in bingo:
    for item in row:
      if item=="X":
        exes+=1
  if exes == 8:
    print("You have won")
    break
  time.sleep(1)
  os.system("clear")