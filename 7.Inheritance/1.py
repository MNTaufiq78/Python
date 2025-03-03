class A:
    def __init__(self):
        self.varA = "Variable in Class A"
    def methodA1(self):
        print("Method A1 of Class A")
    def methodA2(self):
        print("Method A2 of Class A")
    def display(self):
        print("Overridden display method in Class A")

class B(A):
    def __init__(self):
        super().__init__()  
        self.varB = "Variable in Class B"
    def methodB1(self):
        print("Method B1 of Class B")
    def methodB2(self):
        print("Method B2 of Class B")
    def display(self):
        print("Overridden display method in Class B")

class C(B):
    def __init__(self):
        super().__init__()  
        self.varC = "Variable in Class C"
    def methodC1(self):
        print("Method C1 of Class C")
    def methodC2(self):
        print("Method C2 of Class C")
    def display(self):
        print("Overridden display method in Class C")

class MainClass:
    def main():
        objA = A()
        objB = B()
        objC = C()
        print("\nCalling Methods Using Each Object")
        objA.methodA1()
        objA.methodA2()
        objA.display()
        objB.methodA1()
        objB.methodA2()
        objB.methodB1()
        objB.methodB2()
        objB.display()
        objC.methodA1()
        objC.methodA2()
        objC.methodB1()
        objC.methodB2()
        objC.methodC1()
        objC.methodC2()
        objC.display()
        print("\nCalling Overridden Method Using Superclass Reference")
        refA = objB  
        refA.display()  
        refA = objC  
        refA.display()  
        print("\nRuntime Polymorphism with Data Members")
        print("objA.varA:", objA.varA)
        print("objB.varA:", objB.varA)  
        print("objB.varB:", objB.varB)
        print("objC.varA:", objC.varA)  
        print("objC.varB:", objC.varB)  
        print("objC.varC:", objC.varC)  
MainClass.main()
