from project.stations.base_station import BaseStation
from project.astronauts.engineer_astronaut import EngineerAstronaut

class MaintenanceStation(BaseStation):
    INITIAL_CAPACITY = 3
    SALARY_INCREASE = 3000

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if isinstance(astronaut, EngineerAstronaut) and astronaut.salary <= min_value:
                astronaut.salary += self.SALARY_INCREASE