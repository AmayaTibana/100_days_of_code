
import os, time, sys

inventory = []
try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
    print("No inventory file found. Creating new inventory file.")

def add_item():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
  
    item = input("Enter item name: ").capitalize()
    inventory.append(item)
    print(f"{item} added to inventory.")
    
    
def viewItem():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  seen = []
  for item in inventory:
    if item not in seen:
      print(f"{item} {inventory.count(item)}")
      seen.append(item)

  time.sleep(2)
def remove_item():
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    item = input("Enter item name: ").capitalize()
    if item in inventory:
        inventory.remove(item)
        print(f"{item} removed from inventory.")
    else:
        print(f"{item} not found in inventory.")

while True:
    time.sleep(1)
    os.system("clear")
    print("INVENTORY")
    print("=========")
    print()
    menu = input("1. Add item\n2. View item\n3. Remove item\n")
    if menu == "1":
        add_item()
    elif menu == "2":
        viewItem()
    else:
        remove_item()

    f= open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()