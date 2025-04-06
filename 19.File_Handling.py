# Open the file for writing
file = open('20.file.txt', 'w')
file.write("Hello Rathod, what's going on?\n")
file.write("Is this a good day for you?\n")
file.write("Can you read Book?\n")
file.close()

# Open the file for reading
file = open('20.file.txt', 'r')
data = file.readline()
while data != "":
    print(data, end='')
    data = file.readline()
file.close()
