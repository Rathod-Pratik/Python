class Employee:
    a=1
    def __init__(self):
        print("constructor of Employee")
    
class Programmer(Employee):
    b=2
    def __init__(self):
        print("constructor of Programmer")

class Manager(Programmer):
    c=3
    def __init__(self):
        print("constructor of Manager")
        super().__init__()


o= Manager()
print(o.a);
print(o.b);
print(o.c);