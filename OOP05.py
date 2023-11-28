#OOP Exercise 5: Define a property that must have the same value for every class instance (object)

#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

#Use the following code for this exercise.

#class Vehicle:
#    def __init__(self, name, max_speed, mileage):
#        self.name = name
#        self.max_speed = max_speed
#        self.mileage = mileage

#class Bus(Vehicle):
#    pass

#class Car(Vehicle):
#    pass

#Expected Output:
#Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
#Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

class Vehicle:
    color = 'White' #ATRIBUTO DE CLASE!
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
Audi_suv = Car("Audi Q5", 240, 18)

print("Color:", Vehicle.color, "Vehicle name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
print("Color:", Vehicle.color, "Vehicle name:", Audi_suv.name, "Speed:", Audi_suv.max_speed, "Mileage:", Audi_suv.mileage)
