# Use to set and get Values
class Employee:
    # Getter function
   @property
   def name(self):
      return f"{self.fname} {self.lname}"

    #setter function
   @name.setter
   def name(self,value):
      self.fname=value.split(" ")[0]
      self.lname=value.split(" ")[1]

a=Employee();
a.name="Dax Chauhan"
print(a.name)