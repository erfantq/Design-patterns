""" 
    Strategy
    - A behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
"""
import abc

class Read: # Context
    def __init__(self, sentence):
        self.sentence = sentence
        self._direction = None
        
    def set_direction(self, direction):
        self._direction = direction

    def read(self):
        self._direction.direct(self.sentence)

class Direction(abc.ABC): # Abstract strategy

    @abc.abstractmethod
    def direct(self, sentence):
        pass

class Right(Direction): # Concrete strategy
    def direct(self, sentence):
        print(sentence[::-1])

class Left(Direction): # Concrete strategy
    def direct(self, sentence):
        print(sentence[::1])

c = Read("Hello world")
c.set_direction(Right())
c.read()

# change the strategy in run time
c.set_direction(Left())
c.read()
        

