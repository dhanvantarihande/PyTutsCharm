# Multilevel Inheritance
# Vehicle - Car is a Type of Vehicle - Tesla - type of Car
# is A - Car is Vehicle, Tesla is a Car

class Vehicle:

    def start_engine(self):
        print("Engine Started!")


class Car(Vehicle):

    def drive(self):
        print("Drive the Car")


class Tesla(Car):

    def race(self):
        print("Tesla Car")


my_car = Tesla()

my_car.start_engine()
my_car.drive()
my_car.race()