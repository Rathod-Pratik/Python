class Employee:
    company="ITC"
    name="Rathod Pratik"
    salary=20000
    def show(self):
        print(f"The name of employee is {self.name} and salary of employee is {self.salary}")


class Coder:
    language="Python"
    def PrintLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

class Programmer(Employee,Coder):
    def ShowLanguage(self):
        print(f"The name of employee is {self.name} and he is good with {self.language} language")


a=Programmer()
a.show();
a.PrintLanguage()
a.ShowLanguage();