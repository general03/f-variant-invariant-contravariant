class Animal:
  pass

class Dog(Animal):
  pass

def feed_animals(animals: list[Animal]):
  for animal in animals:
    print(f"Feeding a(n) {type(animal).__name__}")

dogs = [Dog()]
feed_animals(dogs) # Mypy: Argument 1 to "feed_animals" has incompatible type "list[Dog]"; expected "list[Animal]" [arg-type]
