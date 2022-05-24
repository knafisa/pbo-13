from abstractFactory import AbstractFactory
from enum import Enum
from machine import MachineA, MachineB

class MachineType(Enum):
    MachineA = 0,
    MachineB = 1


class MachineFactory(AbstractFactory):

    def __init__(self):
        pass

    def create_object(self, type, level):
        if(type == MachineType.MachineA):
            return MachineA(level)
        elif(type == MachineType.MachineB):
            return MachineB(level)
        else:
            assert 0, "Invalid Machine Type"