## test.py file ##############
import random
num = random.randint(10,100) # Need the random. to refer to the random library
def countdown():
  for i in range(num):
    print(i+1)
# Removed internal subroutine call.
### main.py file ###############
import test as tt # No such file as tt, that's the nickname I want to give the 'test' file
print("Countdown")
tt.countdown() # Referenced 'tt' file nickname before the call.