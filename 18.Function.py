# 1.function without Parameter
# def average():
#     a=float(input("enter year: "))
#     b=float(input("enter amount: "))
#     c=float(input("enter interest: "))

#     i=a*b*c/100

#     print("Interest is: ",i)

# average()

# 2.function with Parameter
# def GoodDay(name="Mohit"):
#     print("Good morning ",name)

# GoodDay("Anish")
# GoodDay()

# 3.function with return
# def Sum(a,b):
#     return a+b

# a=Sum(12,50)
# print(a)


# 4.recursion
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n=int(input("enter number: "));

print("factorial of number is: ",factorial(n))