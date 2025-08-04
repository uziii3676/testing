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

class father():
    def parent(self):
        print("My father name is Aamir shakoor")
class son(father):
    def son(self):
        print("I am Usman Aamir")

c=son()
c.son()
c.parent()

#Polymorphism
class person:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def details(self):
        print(f"Name:{self.name},Age:{self.age},Id:{self.id}")
    def intro(self):
        print("I am a Person")

class student(person):
    def __init__(self, name, age, id,grade):
        super().__init__(name, age, id)
        self.grade=grade
    def intro(self):
        print(f"My name is {self.name} and I am a student of grade{self.grade}")

class teacher(person):
    def __init__(self, name, age, id,subject):
        super().__init__(name, age, id)
        self.subject=subject
    def intro(self):
        print(f"I am a Teacher,My name is {self.name},I teach {self.subject}")
  
st1=student("Usman",19,8347,13)
T1=teacher("Ahsan",23,8374,"Pyyhon")
st1.details()
st1.intro()
T1.details()
T1.intro()

#Encapsulation

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def show_info(self):
        print(f"Name:{self.name},Salary:{self.__salary}")

    def set_salary(self,amount):
        if amount>0:
            self.__salary=amount
        else:
            print("invalid Salary")
    def get_salary(self):
        return self.__salary
    
emp=Employee("Usman",100000)
emp.show_info

print(emp.get_salary())