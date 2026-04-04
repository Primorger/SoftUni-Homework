import re
from abc import ABC, abstractmethod
from project.astronauts.base_astronaut import BaseAstronaut

class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list["BaseAstronaut"] = []
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not re.match(r'^[A-Za-z0-9-]+$', value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_salaries = sum(a.salary for a in self.astronauts)
        return f"{total_salaries:.2f}"

    def status(self):
        if self.astronauts:
            result = " #".join(sorted(a.id_number for a in self.astronauts))
        else:
            result = "N/A"
        return (f"Station name: {self.name}; "
                f"Astronauts: {result}; "
                f"Total salaries: {self.calculate_total_salaries()}")

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass
