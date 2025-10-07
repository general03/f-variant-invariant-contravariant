
class Dog:
  pass

class Box[T]:
    def __init__(self, content: T) -> None:
        self._content = content

def play_with_dog(box: Box[Dog]):
    print(f"Play in {type(box).__name__}")

box = Box(Dog())
play_with_dog(box)
