from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.research_station import ResearchStation
from project.stations.maintenance_station import MaintenanceStation

class SpaceAgency:
    ASTRONAUT_TYPES = {
        "EngineerAstronaut": EngineerAstronaut,
        "ScientistAstronaut": ScientistAstronaut,
    }
    STATION_TYPES = {
        "ResearchStation": ResearchStation,
        "MaintenanceStation": MaintenanceStation,
    }
    
    def __init__(self):
        self.astronauts = []
        self.stations = []
        
    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise ValueError("Invalid astronaut type!")
        
        if any(a.id_number == astronaut_id_number for a in self.astronauts):
            raise ValueError(f"{astronaut_id_number} has been already added!")
        
        astronaut = self.ASTRONAUT_TYPES[astronaut_type](astronaut_id_number, astronaut_salary)
        self.astronauts.append(astronaut)
        
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."
    
    def add_station(self, station_type: str, station_name: str):
        if station_type not in self.STATION_TYPES:
            raise ValueError("Invalid station type!")
        
        if any(s.name == station_name for s in self.stations):
            raise ValueError(f"{station_name} has been already added!")
        
        station = self.STATION_TYPES[station_type](station_name)
        self.stations.append(station)
        
        return f"{station_name} is successfully added as a {station_type}."
    
    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station = next((s for s in self.stations if s.name == station_name), None)
        if not station:
            raise ValueError(f"Station {station_name} does not exist!")
    
        astronaut = next((a for a in self.astronauts if type(a).__name__ == astronaut_type), None)
        
        if not astronaut:
            raise ValueError("No available astronauts of the type!")

        if station.capacity == 0:
            return "This station has no available capacity."

        self.astronauts.remove(astronaut)
        
        station.astronauts.append(astronaut)
        station.capacity -= 1
        
        return f"{astronaut.id_number} was assigned to {station_name}."
    
    def train_astronauts(self, station, sessions_number: int):
        for _ in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()
                
        total_stamina = sum(a.stamina for a in station.astronauts)
        
        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."
    
    def retire_astronaut(self, station, astronaut_id_number: str):
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)
        
        if not astronaut or astronaut.stamina == 100:
            return "The retirement process was canceled."
        
        station.astronauts.remove(astronaut)
        station.capacity += 1
        
        return f"Retired astronaut {astronaut_id_number}."
    
    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))

        total_capacity = sum(station.capacity for station in self.stations)
        station_lines = "\n".join(station.status() for station in sorted_stations)

        return (
            f"*Space Agency Up-to-Date Report*\n"
            f"Total number of available astronauts: {len(self.astronauts)}\n"
            f"**Stations count: {len(self.stations)}; Total available capacity: {total_capacity}**\n"
            f"{station_lines}"
        )