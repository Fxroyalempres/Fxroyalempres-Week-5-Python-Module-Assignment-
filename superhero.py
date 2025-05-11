# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def __str__(self):
        return f"{self.name} has the power of {self.power} and protects {self.city}."


# Subclass: Batman
class Batman(Superhero):
    def __init__(self, name, power, city):
        super().__init__(name, power, city)

    def use_gadgets(self):
        return f"{self.name} is using high-tech gadgets to fight crime in {self.city}."


# Subclass: Superman
class Superman(Superhero):
    def __init__(self, name, power, city):
        super().__init__(name, power, city)

    def fly(self):
        return f"{self.name} is flying over {self.city} to save the day!"


# Example Usage
if __name__ == "__main__":
    batman = Batman("Bruce Wayne", "Intelligence and Gadgets", "Gotham")
    superman = Superman("Clark Kent", "Super Strength and Flight", "Metropolis")

    print(batman)
    print(batman.use_gadgets())

    print(superman)
    print(superman.fly())