from project.stations.base_station import BaseStation
from project.astronauts.scientist_astronaut import ScientistAstronaut

class ResearchStation(BaseStation):
    INITIAL_CAPACITY = 5
    SALARY_INCREASE = 5000

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if isinstance(astronaut, ScientistAstronaut) and astronaut.salary <= min_value:
                astronaut.salary += self.SALARY_INCREASE