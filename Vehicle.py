
class Vehicle:
    
    def __init__(self, vechicle_type: str, model: str, brand: str, year_of_manufacture: int, rate_per_day: float, availability: str) -> None:
        self.vehicle_type = vechicle_type
        self.model = model
        self.brand = brand
        self.year_of_manufacture = year_of_manufacture
        self.rate_per_day = rate_per_day
        self.availability = availability

    
    def get_vehicle_info(self):
        return "Vehicle Type: "+ {self.vehicle_type}+"Model: " +{self.model}