l=[5,2,8,7]

for j in range(4):
    for i in range(0,3):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
    
print(l)