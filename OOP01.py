#OOP Exercise 1: Create a Class with instance attributes
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

VW_Jetta = Vehicle(210, 18)
print(VW_Jetta.max_speed, VW_Jetta.mileage)
