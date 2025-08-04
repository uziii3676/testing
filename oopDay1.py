class car:
    def drive(self):
        print("I am Driving")
my_car=car()
my_car.drive()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greeting(self):
        print(f"I am {self.name},My age is {self.age}")

person1=person("Usman",19)
person1.greeting()