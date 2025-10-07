from typing import Callable

class A:  
  pass

class B(A):  
  pass

def process_a(data: A) -> None:
  print("Processing A")

def process_b(data: B) -> None:
  print("Processing B")

def handler(func: Callable[[A], None]):
   func(B())

handler(process_a) # Ceci est valide  
handler(process_b) # Fails mypy check, car process_b prend un type B, qui est plus spécifique que A.