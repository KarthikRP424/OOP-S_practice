# class person:
    
#     def __init__(self,name,age):
        
#         self.name = name
#         self.age = age
        
#     def greet(self):
#         print(f"Helo, My name is {self.name} , I am {self.age} years old")
#         print("Thank YOu")
        
# person1 = person("karthu", 20)
# person2 = person("pavu",18)
# person3 = person("dhanu",16)

# person1.greet()
# person2.greet()
# person3.greet()

# class mobile:
    
#     def __init__(self,brand,prize):
#         self.brand = brand
#         self.prize = prize
        
        
#     def attributes(self):
#         print(f"the brand name is {self.brand}, And the prize is {self.prize}")
        
# phone1 = mobile("vivo", 19500)
# phone2 = mobile("samsung",45000)

# phone1.attributes()
# phone2.attributes()

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def about(self):
#         print(f"the name of the student is{self.name},and marks is {self.marks}")
        
        
# student1 = student("Ram",100)
# student2 = student("Shiv",100)

# student1.about()
# student2.about()

# 4. Optional Parameters (Default Values) in Constructors

class book:
    def __init__(self,title,author= "unknown"):
        
        self.title = title
        self.author = author
        
    def about(self):
        print(f"the title of the book is{self.title},and the author is {self.author}")
        
title1 = book("python programming")
title2 = book("the knowledge about oops ","karthik")

title1.about()
title2.about()