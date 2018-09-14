import Vehicle

class Car(Vehicle.Vehicle):
    def brag(self):
        print('Look how cool my car is!!')

car1 = Car()
car1.drive()
car1.add_warning("Be carefull!")
print(car1.get_warning())

car2 = Car(150)
car2.drive()


car3 = Car(200)
car3.drive()

print(car1.__dict__)
print(car3)