# Base class representing a general vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make  # Make of the vehicle (e.g., Toyota)
        self.model = model  # Model of the vehicle (e.g., Camry)
        self.year = year  # Year of manufacture (e.g., 2020)
    
    def start_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine is now running."

    def stop_engine(self):
        return f"The {self.year} {self.make} {self.model}'s engine has been turned off."

# Car class inheriting from Vehicle (polymorphism)
class Car(Vehicle):
    def __init__(self, make, model, year, color, fuel_type):
        # Initialize the base class (Vehicle) using super()
        super().__init__(make, model, year)
        self.color = color  # Color of the car (e.g., red)
        self.fuel_type = fuel_type  # Fuel type (e.g., gasoline or electric)

    def display_details(self):
        # Polymorphism: Display car-specific details in a custom format
        return f"{self.year} {self.make} {self.model} ({self.color}), Fuel Type: {self.fuel_type}"

    def honk(self):
        return "Beep beep! This car is honking!"

    def drive(self):
        return f"The {self.year} {self.make} {self.model} is driving on the road."

# ElectricCar class inheriting from Car (demonstrates encapsulation and further polymorphism)
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        # Initialize the parent class (Car) using super()
        super().__init__(make, model, year, color, "electric")
        self.battery_capacity = battery_capacity  # Battery capacity (e.g., 100 kWh)

    def charge(self):
        return f"The {self.year} {self.make} {self.model} is charging. Battery capacity: {self.battery_capacity} kWh."

    # Overriding the honk method to demonstrate polymorphism
    def honk(self):
        return "Silent honk! It's an electric car."

# Creating objects of each class
my_car = Car("Toyota", "Camry", 2020, "blue", "gasoline")
my_electric_car = ElectricCar("Tesla", "Model S", 2021, "black", 100)

# Demonstrating polymorphism and inheritance
print(my_car.start_engine())  # Method from base class Vehicle
print(my_car.display_details())  # Method from Car class
print(my_car.honk())  # Method from Car class

print(my_electric_car.start_engine())  # Method from base class Vehicle
print(my_electric_car.display_details())  # Method from Car class
print(my_electric_car.honk())  # Overridden method in ElectricCar class
print(my_electric_car.charge())  # Method specific to ElectricCar
