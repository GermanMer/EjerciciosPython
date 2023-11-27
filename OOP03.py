#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

#Given:
#class Vehicle:
#    def __init__(self, name, max_speed, mileage):
#        self.name = name
#        self.max_speed = max_speed
#        self.mileage = mileage

#Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

#Expected Output:
#Vehicle Name: School Volvo Speed: 180 Mileage: 12

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Child class
class Car(Vehicle):
    pass

School_Volvo = Car('School Volvo', 180, 12)
print('Vehicle Name:', School_Volvo.name, 'Speed:', School_Volvo.max_speed, 'Mileage:', School_Volvo.mileage)
