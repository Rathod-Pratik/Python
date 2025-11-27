a=[3,5,1,8,6,9];
x=int(input('Enter Number: '));
for i in range(len(a)):
    if a[i] == x:
        print("%d at %d position"%(x,i))
        break;
else:
    print("Number not found")