a=[1,3,2,4]
for i in a:
    j=a.index(i)
    
    while j>0:
        if a[j-1] > a[j]:
            a[j-1],a[j]=a[j],a[j-1]
        else:
          break

print(a)