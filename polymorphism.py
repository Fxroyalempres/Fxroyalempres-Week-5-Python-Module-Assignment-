# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "The car is driving on the road 🚗."


# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "The plane is flying in the sky ✈️."


# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "The boat is sailing on the water 🚤."


# Example Usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for vehicle in vehicles:
        print(vehicle.move())