from abc import ABCMeta, abstractmethod

class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_object(self, type, level):
        pass