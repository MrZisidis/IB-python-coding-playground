# lesson on python lists
anumber = 10
alist = [1, 2, 3, 4, 5, 6,7,8,9,10]

# print(anumber)
# print(type(anumber))
# print(alist)
# print(type(alist))
# my_list = []
# print(my_list)

my_list = [7, 2, 2, 5, 2]

# print(my_list[0])
# print(my_list[1])
# print(my_list[3])
#
# print("The sum of the first two items:", my_list[0] + my_list[1])
# print(my_list)

my_list = [7, 2, 2, 5, 2]
# print(len(my_list))





#Please write a program which initialises a list with the values [1, 2, 3, 4, 5].
# Then the program should ask the user for an index and a new value, replace the value at the given index,
# and print the list again.
# This should be looped over until the user gives -1 for the index.
# You can assume all given index values will fall within your list.

my_list = [1, 2, 3, 4, 5]
# print(my_list[-5])

# index = int(input("Enter your index of choice: "))
# new_value = int(input("Enter your new value: "))
# my_list[index] = new_value
# print(my_list)
# while index != 1:
while True:
    index = int(input("Enter your index of choice: "))
    if index ==  -1:
        print(my_list)
        break
    else:
        new_value = int(input("Enter your new value: "))
        my_list[index] = new_value
    print(my_list)



