for i in range (5):
  print(i)

import random
colors = ["Red", "Orange", "Yellow"]

while True:
  menu = input("1: Color or 2: Exist")
  if menu == "1":
    print(random.choice(colors)):
  else:
    break