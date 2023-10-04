
from typing import Any
from rich import print

class Person:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email
    
    # def __getattribute__(self, attr: str) -> Any:
    #     print(f'INFO: {attr=}')
        
    #     return super(Person, self).__getattribute__(attr)

    def __eq__(self, __value: object) -> bool:
        pass
    
    def __lt__(self, __value: object) -> bool:
        
        return self.age < __value.age
    
    def __le__(self, __value: object) -> bool:
        return self.age <= __value.age
    
    def __add__(self, __value: int):
        self.age += __value
        return self
    
    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.age}, '{self.email}')"



per1 = Person('John', 17, 'John@mail.ru')

per1 += 10

print(per1)

import math 

print(math.trunc(4.8))