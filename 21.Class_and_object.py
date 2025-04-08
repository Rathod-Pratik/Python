# Create a class
class employee:
    language="Python";
    salary=20000;

    def getInfo(self):
        print(f"Name is {self.name}. This Language is {self.language}.  The Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

# Create an instnace of class
Mohit = employee();

# instnace attribute
Mohit.name="Mohit Chauhan"

# update the Value of language
# Mohit.language="JavaScript"

# Class attribute
# print(Mohit.name,Mohit.language,Mohit.salary)

Mohit.getInfo()