from abc import ABC, abstractmethod
#1. Create an abstract class with abstract and non-abstract methods. 
class AbstractClass(ABC):
    def __init__(self):
        self.message = "This is a non-abstract method in AbstractClass"
    @abstractmethod
    def abstract_method(self):
        pass  
    def non_abstract_method(self):
        print(self.message)
#2. Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods 
class ChildClass(AbstractClass): 
    def abstract_method(self):
        print("Abstract method implemented in ChildClass")
def main():
    obj = ChildClass()  
    obj.non_abstract_method()  
main()
#3. Create an instance for the child class in child class and call abstract methods
class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Abstract method implemented in ChildClass")
    def call_abstract_method(self):
        self.abstract_method()  
def main():
    obj = ChildClass()
    obj.call_abstract_method()  
main()
#4. Create an instance for the child class in child class and call non-abstract methods
class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Abstract method implemented in ChildClass")
    def call_non_abstract_method(self):
        self.non_abstract_method()
def main():
    obj = ChildClass()
    obj.call_non_abstract_method()  
main()
