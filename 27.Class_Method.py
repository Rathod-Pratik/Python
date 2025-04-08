# Class Method use to access class Value not object Values
class Employee:
    a=1;
    @classmethod
    def show(cls):
        print(f"the Value of a is {cls.a}") 


a=Employee();
a.a=500
a.show()