from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    INEFFICIENCY_DUE_TO_AIR_CONDITIONER = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + Car.INEFFICIENCY_DUE_TO_AIR_CONDITIONER) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    INEFFICIENCY_DUE_TO_AIR_CONDITIONER = 1.6
    HOLE_IN_THE_TANK_REDUCTION = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + Truck.INEFFICIENCY_DUE_TO_AIR_CONDITIONER) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.HOLE_IN_THE_TANK_REDUCTION


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)

# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
