import os, time, sys

pizza = []

try:
  f = open("pizza.txt", "r")
  pizza = eval(f.read())
  f.close()
except:
  print("ERROR: No existing pizza No file found")

def viewPizza():
  h1 = "Name"
  h2 = "Topping"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Total"
  print(f"{h1:^10}{h2:^10}{h3:^10}{h4:^10}{h5:^10}")
  for row in pizza:
    print(f"{row[0]:^10}{row[1]:^10}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
    time.sleep(2)

def addPizza():
  time.sleep(1)
  os.system("clear")
  name = input("Name : ")
  topping = input("Topping : ")
  size = input("Size : ").lower()
  while True:
    try:
      qty = int(input("Quantity : "))
      break
    except:
      print("ERROR: Invalid input must be a whole number")
  cost = 0
  if size == "s":
    cost = 6.99
  elif size == "m":
    cost = 8.99
  else:
    cost = 10.99
    total = cost * qty
    total = round(total, 2)
    row = [name, topping, size, qty, total]
    pizza.append(row)

while True:
 time.sleep(1)
 os.system("clear")
 menu = input("1) Add: \n2) View:\n")
 if menu == "1":
    addPizza()
 else:
    viewPizza()
    f = open("pizza.txt", "w")
    f.write(str(pizza))
    f.close()