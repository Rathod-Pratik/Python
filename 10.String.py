name="rathod Pratik"

#use to Trim the String
print(name[0:6])  #Print character to index 0 to 6
print(name[7:])   #7 index to end
print(name[:])    #Start to end index
print(name[:7])   #0 to 7 index

#Negative slice
print(name[-4:-1])

#skip Character
print(name[1:10:3])

#find Length
print(len(name))

#find character start and end with
print(name.endswith('tik'))
print(name.endswith('ro'))

#make first Character capital
print(name.capitalize())

#make all character capital
print(name.upper())

#make all character Small
print(name.lower())

#replace word
replace_name=name.replace("rathod","Sharma")
print(replace_name)

#Escape sequence
Escape="Mohit is good Player \nBut bov \'botiyo\'"
print(Escape)