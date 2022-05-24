from abc import ABCMeta, abstractmethod

class Machine(metaclass=ABCMeta):
    @abstractmethod
    def work(self):
        pass

class MachineA(Machine):
    def __init__(self, level):
        print("Creating MachineA with level {0}".format(level))

    def work(self):
        print("MachineA::: working")

class MachineB(Machine):
    def __init__(self, level):
        print("Creating MachineB with level {0}".format(level))

    def work(self):
        print("MachineB::: working")