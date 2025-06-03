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
print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")
print(f"your Star Wars name is {all}")
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

