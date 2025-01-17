""" 
    Composit
    - A structural design pattern that lets you compose objects into tree structures
    and then work with this structures as if they were individual objects.
"""
from abc import ABC, abstractmethod

class Being(ABC):  # Abstract Component
    def add(self, child):
        pass
    
    def remove(self, child):
        pass
    
    def is_composite(self):
        return False
    
    @abstractmethod
    def execute(self):
        pass
    

class Animal(Being):  # Leaf
    def __init__(self, name):
        self.name = name
        
    def execute(self):
        print(f'Animal {self.name}')


class Human(Being):  # Concrete Composite
    def __init__(self):
        self.children = []
        
    def add(self, child):
        self.children.append(child)        

    def remove(self, child):
        self.children.remove(child)

    def is_composite(self):
        return True

    def execute(self):
        print('Human composite')
        
        for child in self.children:
            child.execute()


class Male(Human):  # Leaf
    def __init__(self, name):
        self.name = name
        
    def is_composite(self):
        return False
        
    def execute(self):
        print(f'\tMale {self.name}')


class Female(Human):  # Leaf
    def __init__(self, name):
        self.name = name
        
    def is_composite(self):
        return False
        
    def execute(self):
        print(f'\tFemale {self.name}')


def client_composite():
    f1 = Female('jane')
    f2 = Female('katty')
    m1 = Male('brad')

    h1 = Human()
    h1.add(f1)
    h1.add(f2)
    h1.add(m1)

    h1.execute()


client_composite()