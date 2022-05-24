from abstractFactory import AbstractFactory
from enum import Enum
from product import ProductA, ProductB

class ProductType(Enum):
    ProductA = 0,
    ProductB = 1

class ProductFactory(AbstractFactory):
    def create_object(self, type, level):
        if(type == ProductType.ProductA):
            return ProductA(level)
        elif(type == ProductType.ProductB):
            return ProductB(level)