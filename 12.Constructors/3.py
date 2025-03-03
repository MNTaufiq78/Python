class Test:
    def __init__(self):  
        print("Public constructor")

    def _protected_constructor(self): 
        print("Protected constructor")

    def __private_constructor(self): 
        print("Private constructor")

obj = Test()
obj._protected_constructor()  
#obj.__private_constructor() #Not accessible. Raises error