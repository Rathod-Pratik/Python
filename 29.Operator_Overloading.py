class Number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num): #Override addition
        return self.n * num.n
    
    def __truediv__(self,num): #Override devision
        return self.n / num.n
    
    def __mul__(self,num): #Override multiplication
        return self.n - num.n
    
    def __sub__(self,num): #Override substraction
        return self.n + num.n
    
    def __floordiv__(self,num): #Override DoubleDivision
        return self.n + num.n

m= Number(8)
n= Number(2)

print(m+n)
print(m/n)
print(m*n)
print(m-n)
print(m//n)