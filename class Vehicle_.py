class Vehicle: 
    def start(self): 
        return "Starting the car engine"
    def stop(self): 
        return "Stopping the vehicle"
class Car(Vehicle): 
    def start(self): 
        return "Starting the car engine"
class Bicycle(Vehicle): 
    def start(self): 
        return "Pedaling the bicycle"
    
vehicle = Vehicle()
car = Car()
bicycle = Bicycle()

print(vehicle.start())
print(vehicle.stop())
print(car.start())
print(bicycle.start())