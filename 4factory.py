from machineFactory import MachineType, MachineFactory
from productFactory import ProductType, ProductFactory


if __name__ == "__main__":
    mFactory = MachineFactory()
    pFactory = ProductFactory()

    resources = [
        mFactory.create_object(MachineType.MachineA, 0),
        mFactory.create_object(MachineType.MachineB, 1),
        pFactory.create_object(ProductType.ProductA, 0),
        pFactory.create_object(ProductType.ProductB, 1)
    ]
    for res in resources:
        res.work()