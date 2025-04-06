#Use to declare empty set
# sets=set() 
# print type of set
# print(type(sets))

#Sets can't accept the duplicate value
sets={1,3,4,6,7,"Mohit"}

#Add multiple element to set
sets.add("Karan")
print(sets)

#Add multiple methods to set
sets.update([10,50])
print(sets)

#Remove element from set 
sets.remove("Mohit"); #if element not found it return error
sets.discard(50) #if element not found it not return error
print(sets)

#Remove random element
a=sets.pop()
print(a)
print(sets)

#Remove all elements
sets.clear()
print(sets)

set1={10,30,50,70,90}
set2={20,40,60,80,90,70,100}

#print union value of two set
print(set1.union(set2))

#print intersect of two set
print(set1.intersection(set2))