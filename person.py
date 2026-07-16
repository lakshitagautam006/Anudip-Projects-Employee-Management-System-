from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    # Getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    @abstractmethod
    def display(self):
        pass