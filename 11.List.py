Name=["Rahan","Mohan","Anish","Mohit","Dax"] 

#Print value using index from List
print(Name[1]) 

#Print multiple Value
print(Name[2:4]) 

#Count Mohan in List
print(Name.count('Mohan'));

#Short List
NumberList=[90,58,14,87,100,65,47,19,81]
NumberList.sort();
print(NumberList)

#Revese List
NumberList.reverse()
print(NumberList)

#Append Value at the end
Name.append("krish")
print(Name[5])

# Remove Value from the List
Name.pop(4)
print(Name)

# Insert Value at any index
Name.insert(2,"Karan")
print(Name)