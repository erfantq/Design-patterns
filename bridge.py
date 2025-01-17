""" 
    Bridge 
    - A structural design pattern that lets you split a large class into two seperate
    hierarchies - abstraction and implementation - which can be developed independently of each other.
"""
from abc import ABC

class Shape(ABC):  # Abstraction
    def __init__(self, color):
        self.color = color
        
    def show(self):
        pass
    
class Circle(Shape):  # Refined Abstraction
    def show(self):
        self.color.paint(self.__class__.__name__)

class Square(Shape):  # Refined Abstraction
    def show(self):
        self.color.paint(self.__class__.__name__)

class Color(ABC):  # Implementation
    def paint(self, name):
        pass
    
class Red(Color):  # Concrete Implementation
    def paint(self, name):
        print(f'This is a red {name}')

class Blue(Color):
    def paint(self, name):
        print(f'This is a blue {name}')


red = Red()
circle = Circle(red)
circle.show()

