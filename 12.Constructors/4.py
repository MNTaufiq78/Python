class Person:
    def __init__(self, name, age):
        self.name = name      
        self._id = 12345      
        self.__password = "abc123"  
    def display(self):
        print(f"Name: {self.name}, ID: {self._id}")

p = Person("John", 25)
p.display()

print(p.name)     
print(p._id)      
# print(p.__password)  #Not accessible. Raises error
