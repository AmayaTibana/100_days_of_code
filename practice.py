# Rock, Paper, Scissors Game first project ever.
"""from getpass import getpass as input

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

#Todo List Small project

""" import os, time, sys, random

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
      print(f"{item} was not in the list")"""

#Another solution to the problem could be this

"""print ("start wars name generator")

first = input("Enter your first name: ").strip()
second = input("Enter your last name: ").strip()
maiden = input("Enter your mum's maiden name: ").strip()
city = input("Enter your city of birth: ").strip()

name = f"{first[:3].title()} {second[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print (f"Your Star Wars name is {name}") """

#This is the end of the project startwars name generator