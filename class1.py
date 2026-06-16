class Human:
    def __init__(self,name,age):
        print("Construct is called",name)
        self.name = name
        self.age = age;
        
    def walk(self):
        print(f"{self.name} is walking")
        
pa = Human("pavan",20)
dh = Human("dh",21)

# pa.walk()
# dh.walk()
Human.walk(pa)