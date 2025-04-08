# Create a class
class employee:
    name="Anish Dusara"
    def getInfo(self):
        print(f"Name is {self.name}.")

    def __init__(self,name):
        self.name=name;
        print("I am creating object")

# Create an instnace of class
Rathod = employee("Krish Dusara");

Rathod.getInfo()