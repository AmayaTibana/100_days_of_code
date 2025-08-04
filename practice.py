class animal:
  species = None
  name = None
  sound = None

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound
  def talk(self):
    print((f"{self.name} says {self.sound}"))
class bird(animal):
 def __init__(self, color):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color
   
cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)



polly = bird("Green") 
polly.talk()
print(polly.color)