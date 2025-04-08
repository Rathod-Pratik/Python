class Employee:
    name="Mohit Chauhan"
    salary=20000
    company="GIFC"
    def Show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

    
class Programmer(Employee):
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.company} Company")

    
b=Programmer()
b.Show();
b.showLanguage()
