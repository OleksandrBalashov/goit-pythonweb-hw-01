from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)

class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self):
        raise ValueError("Треба створити экземпляр")
      

class Car(Vehicle):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car():
        pass

    @abstractmethod
    def create_motorcycle():
        pass   

class USVehicleFactory(VehicleFactory):
    def create_car(self, marka: str, model: str):
        return Car(marka, model, "US")
    
    def create_motorcycle(self, marka, model):
        return Motorcycle(marka, model, "US")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, marka: str, model: str):
        return Car(marka, model, "EU")
    
    def create_motorcycle(self, marka: str, model: str):
        return Motorcycle(marka, model, "EU")

eu_vehicle = EUVehicleFactory()
us_vehicle = USVehicleFactory()

# Використання
vehicle1 = eu_vehicle.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = us_vehicle.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
