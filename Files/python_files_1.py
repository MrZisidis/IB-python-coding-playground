myFile = open("names.txt")
# print(myFile) # prints that it's loaded in the memory

# contents = myFile.read()
# print(contents)
# print(type(contents))

for line in myFile:
    line = line.replace("\n", "")
    print(line)

myFile.close()

# f = open("numbers.txt", "w")
# f. write("First line")
# f.close()