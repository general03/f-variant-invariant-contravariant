class Animal:
  pass

class Dog(Animal):
  pass

class Box[T]:
    def __init__(self, content: T) -> None:
        self._content = content

    def set_content(self, content: T) -> T: # This method infers the generic type
        self._content = content
        return self._content

def play_with_dog(box: Box[Animal]):
    print(f"Play in {type(box).__name__}")

box = Box(Dog())
play_with_dog(box) # Mypy: Argument 1 to "play_with_dog" has incompatible type "Box[Dog]"; expected "Box[Animal]"
