from typing import Final


class Animal:
  pass

class Dog(Animal):
  pass

class Box[T]:
    def __init__(self, content: T) -> None:
        self.content : Final = content # public attribut

def play_with_dog(box: Box[Animal]):
    print(f"Play in {type(box).__name__}")

box = Box(Dog()) # Box(Animal()) is also OK
play_with_dog(box)
