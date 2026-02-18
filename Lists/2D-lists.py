# numbers = [ [1,2,3] ,[4,5,6] ,[7,8,9] ]
# print(numbers[0][1])
# # print(type(numbers))
# person1 = ["name", 1.86, 24]
# person2 = ["name2", 1.56, 33]
# persons = [person1, person2]
#
# print(persons)
persons = [["Betty", 10, 1.37],
           ["Peter", 7, 1.25],
           ["Emily", 32, 1.64],
           ["Alan", 39, 1.78]]
#  persons[i][0]   - this way i access all the names!!!
for i in range(len(persons)):
    # print(persons[i][0])
    if persons[i][0] =="Betty":
        print("FOUND!")
print(persons.__sizeof__())


# for person in persons:
# # person will be a whole list
#   for element in person:
#       #element will be one element of each list
#       # print(element)
#       if element == "Peter":
#           print("FOUND!")


