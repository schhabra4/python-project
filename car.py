class Vehicle:
   
    number_of_wheels = 4


    def __init__(self, make, model, fuel="gas"): 
        self.make = make
        self.model = model
        self.fuel = fuel
        print(self.make)


    @classmethod
    def get_number_of_wheels(cls):  
        return cls.number_of_wheels

class Car(Vehicle):
    def __init__(self, make, model, fuel="gas"):  
        super().__init__(make, model, fuel)


class Truck(Vehicle):
    number_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):  
        super().__init__(make, model, fuel)

    
    def start(self):
        return "Calling in truck"


my_car = Car("Toyota", "Corolla")
my_truck = Truck("Volvo", "VNL")


print(my_car.fuel) 
print(my_car.number_of_wheels) 
print(my_car.get_number_of_wheels())

print(my_truck.start()) 
print(my_truck.fuel)  
print(my_truck.number_of_wheels)  
print(my_truck.get_number_of_wheels()) 
my truck. start()= I do have 
