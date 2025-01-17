""" 
    A structural design pattern that allows adding new behaviors to objects dynamically
    by placing them inside special wrapper objects, called decorators.
"""
from abc import ABC, abstractmethod

class Page(ABC):  # Abstract component
    
    @abstractmethod
    def show(self):
        pass


class AuthPage(Page):  # Concrete component 1
    def show(self):
        print('Wellcome to authenticated page.')

class AnonPage(Page):  # Concrete component 2
    def show(self):
        print('Wellcome to anonymous page.')

class PageDecorator(Page, ABC):
    def __init__(self, component):
        self._component = component
        
    @abstractmethod
    def show(self):
        pass

class AuthPageDecorator(PageDecorator):
    def show(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if username == 'admin' and password == 'admin':
            self._component.show()
        else: 
            print('You are not authenticated.')
            

def client_decorator():
    page = AuthPage()
    authenticated = AuthPageDecorator(page)
    authenticated.show()
    
client_decorator()
