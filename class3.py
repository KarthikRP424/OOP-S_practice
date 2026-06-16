class student: #encapsulation
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks
        
    def get_marks(self):
        return self.__marks

student1 = student("karthik",88)

print(student1.get_marks())