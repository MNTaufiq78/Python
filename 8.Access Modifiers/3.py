class PublicClass:
    def __init__(self):
        self.public_var = "This is a public variable"
    def public_method(self):
        print("This is a public method")

class AnotherClass:
    def access_public(self):
        obj = PublicClass()
        print(obj.public_var) 
        obj.public_method()  

def main():
    print("\nAccessing from Main:")
    obj = PublicClass()
    print(obj.public_var)
    obj.public_method()
    print("\nAccessing from AnotherClass:")
    another_obj = AnotherClass()
    another_obj.access_public()

main()
