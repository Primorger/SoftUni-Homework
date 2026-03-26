from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 0.9)
        if fuel_needed > self.fuel_quantity:
            return "Car needs refueling"
        self.fuel_quantity -= fuel_needed
        return f"Car travelled {distance} km"

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if fuel_needed > self.fuel_quantity:
            return "Truck needs refueling"
        self.fuel_quantity -= fuel_needed
        return f"Truck travelled {distance} km"

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95