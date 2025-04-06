age=int(input("Enter your age: "))

# 1.If condition
# if(age<18):
#     print("You are not eligible for vote")


# # 2.If else condition
# if(age<18):
#     print("You are not eligible for vote")

# else:
#     print("You are eligible for vote")


# 3.If else Leadder condition
if(age<0):
    print("You enter nagative age")
elif(age==0):
    print("You enter zero Which is not valid")
elif(age<18):
    print("You are not eligible for vote")
else:
    print("You are eligible for vote")