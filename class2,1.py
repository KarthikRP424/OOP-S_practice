class Human():
    def __init__(self,name,age,salary=-1):
        self.name = name
        self.age = age
        self.salary = salary
        
    def yes(self):
        print(f"{self.name} is walking ")
        
c = Human("Chan",26,5)
d = Human("dha",56)

c.yes()
print(c.name,"is the name of c")
print(d.age,"is the age of d")
print(c.salary,"is the salary of d")