class Student:

    def __init__(self, name, age):
        # Private variables (Encapsulation)
        self.__name = name
        self.__age = age

    # Getter method for name
    def get_name(self):
        return self.__name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Setter method for age
    def set_age(self, age):

        # Validation: age must be an integer
        if isinstance(age, int):
            self.__age = age
        else:
            print("Age must be an integer")

# Create object
s = Student("karthik", 21)

# Get name
print("Name:", s.get_name())

# Change name
s.set_name("pavu")

# Get updated name
print("Updated Name:", s.get_name())

# Change age
s.set_age(35)

# Get updated age
print("Age:", s.get_age())



# class student:
    
#     def __init__(self,name,age):
        
#         self.__name=name  #this is public
#         # self.__name = name this is private
#         self.__age = age 
        
#     def get__name(self):#getter
#         return self.__name
    
            
#     def get__age(self):#getter
#         return self.__age
        
#     def set__name(self,name):#setter
#         self.__name = name
        
#     def set__age(self,age):
#         if isinstance(age,int):
#             self.__age = age
#         else:
#             print("this is not a string try again ")
        
        
# s = student("karthik",21)
# # s.age = 20  no control
# print(s.get__name())

# s.set__name("pavu")
# print(s.age)
# s.set__age("34")
# # s.set__age(35)
# print(s.get__name())
# print(s.get__age())