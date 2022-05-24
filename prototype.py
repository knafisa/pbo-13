from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass

class MachineA(Prototype):
    def __init__(self, level):
        if (level == 1):
            self.attribute1 = 234
            self.attribute2 = 34
            self.attribute3 = 5667
        elif (level == 2):
            self.attribute1 = 456
            self.attribute2 = 323
            self.attribute3 = 4323

        self.attribute4 = self.attribute1 * self.attribute2
        self.attribute5 = self.attribute2 + self.attribute3
        ### Read a file and initailize other attributes
        ### ... a complex logic goes in creating an instance of
        ### this class....

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return "Attribute1: {0}, \n" \
               "Attribute2: {1}, \n" \
               "Attribute3: {2}, \n" \
               "Attribute4: {3}, \n" \
               "Attribute5: {4}  \n".format(
            self.attribute1,
            self.attribute2,
            self.attribute3,
            self.attribute4,
            self.attribute5
        )

class MachineB(Prototype):
    def __init__(self, level):
        ### instance creation logic goes here
        ### which may include some complex calculation, file reading
        ### and other stuff
        self.attribute1 = -1
        if (level == 1):
            self.attribute1 = 3459
        elif (level == 2):
            self.attribute1 = 3234
        elif (level == 3):
            self.attribute1 = 3222

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return "Attribute1 :{0} \n".format(self.attribute1)


class PrototypeRepo():
    def __init__(self):
        self.prototypes = {
            "MachineA": {
                1: MachineA(1),
                2: MachineA(2),
            },
            "MachineB": {
                1: MachineB(1),
                2: MachineB(2),
                3: MachineB(3)
            }
        }

    def create_machine(self, machineType, level):
        return self.prototypes[machineType][level].clone()


if __name__ == "__main__":
    pRepo = PrototypeRepo()
    ma1 = pRepo.create_machine("MachineA", 1)
    ma2 = pRepo.create_machine("MachineB", 3)
    print(ma1)
    print(ma2)