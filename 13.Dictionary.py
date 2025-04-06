marks={
    "Hindi":82,
    "English":78,
    "Math":84,
    "science":77
}
#Print Type of Marks
print(type(marks))

#print value by key
print(marks["Math"])

#print all Key and value
print(marks.items())

#Print All key
print(marks.keys())

#print All Value
print(marks.values())

#update Value
marks.update({"Math":100,"gujrati":80})
print(marks.items())

#find specific value
print(marks.get('Math2')) #Return None if not found
# print(marks["Math2"]) #return error if not found

#Remove all Key and Value
# marks.clear(); 
# print(marks.items())

#Remove Value from dictionary
marks.pop("Math")
print(marks.items())

#Remove Last inserted key and value
marks.popitem();
print(marks.items())
