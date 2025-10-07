from typing import Sequence

class Animal:
  pass

class Dog(Animal):  
  pass

def feed_animals(animals: Sequence[Animal]):
  for animal in animals:
    print(f"Feeding a(n) {type(animal).__name__}")

dogs = [Dog(), Dog()]
feed_animals(dogs) # Ceci est valide