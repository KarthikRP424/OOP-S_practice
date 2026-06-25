class Animal:
    def Make_sound(self):
        print("Animal is making sound")
        
class Dog(Animal):
    def Make_sound(self):
        super().Make_sound()
        print("Bow Bow")
        
d = Dog()
d.Make_sound()