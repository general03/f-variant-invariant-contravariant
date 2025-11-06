from typing import Generic, TypeVar

class Dog:
    pass

T_co = TypeVar('T_co', covariant=True)
class Box(Generic[T_co]):
    def __init__(self, content: T_co) -> None:
        self._content = content

def do_something(dog: Box[Dog]):
    pass

do_something(Box(Dog()))