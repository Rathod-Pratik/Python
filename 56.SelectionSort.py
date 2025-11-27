a=[5,4,3,1];
i=0;

while i<len(a):
    small = min(a[i:])
    ind=a.index(small)
    a[i],a[ind]=a[ind],a[i]
    i=i+1
print(a)
