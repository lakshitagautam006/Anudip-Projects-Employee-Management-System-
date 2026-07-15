from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @abstractmethod
    def display(self):
        pass