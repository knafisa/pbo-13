from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
    @abstractmethod
    def work(self):
        pass

class ProductA(Product):
    def __init__(self, level):
        print("Creating ProductA with level {0}".format(level))

    def work(self):
        print("ProductA::: working")

class ProductB(Product):
    def __init__(self, level):
        print("Creating ProductB with level {0}".format(level))

    def work(self):
        print("ProductB::: working")