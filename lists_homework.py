# 1. Please write a program which asks the user to choose between addition and removal.
# 2. Depending on the choice, the program adds an item to or removes an item from the end of a list.
# The item that is added must always be one greater than the last item in the list.
# The first item to be added must be 1.


my_list=[1,2,3,4,5]
# print(len(my_list))
# print(my_list[-1])
print(my_list)
# choice = input("add (d) , remove(r) or exit(x)? : ")
#
# my_list[len(my_list)-1]  #accessing the last item
my_list.append(my_list[-1] +1)
print(my_list)
