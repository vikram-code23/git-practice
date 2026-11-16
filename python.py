class Vikram:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Person(Vikram):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll = roll
    def study(self):
        print("Vikram is studying")

p = Person("Vikram",24,25)
print(p.name)
print(p.age)
print(p.roll)
print(p.study())