# Please write a program which asks the user to choose between addition and removal.
# Depending on the choice, the program adds an item to or removes an item from the end of a list.
# The item that is added must always be one greater than the last item in the list.
# The first item to be added must be 1.
# The list is printed out in the beginning and after each operation.
# Have a look at the example execution below:
# You may assume that, if the list is empty, there will not be an attempt to remove items.

mylist = []
addingCounter = 0

print("the list is now: ", mylist)

while True:
    userChoice = input("Please enter your choice (1- Addition, 2-Removal or X for exit): ")

    if userChoice == "1":
        if addingCounter == 0:
            mylist.append(1)

        else:
            mylist.append(mylist[len(mylist)-1] + 1)
        addingCounter = addingCounter + 1
        print("the list is now: ", mylist)

    elif userChoice == "2":
        if addingCounter == 0:
            print("You cannot remove from an empty list. Choose another option\n(1- Addition, 2-Removal or X for exit):")
        else:
            print("the list is now: ", mylist)
            print("item to pop: ", mylist[len(mylist)-1])
            input()
            mylist.pop(len(mylist)-1)
        print("the list is now: ", mylist)

    elif userChoice.upper() == "X":
        break

    else:
        print("Choose a valid option")

print("the list is now: ", mylist)
print ("Bye!")




# # Initialize an empty list
# my_list = []
#
# while True:
#     # 1. Print the list at the beginning of the loop
#     print(f"The list is now {my_list}")
#
#     # 2. Ask for user input
#     choice = input("a(d)d, (r)emove or e(x)it: ")
#
#     # 3. Handle the choice
#     if choice == 'd':
#         # logic: if list is empty, add 1.
#         # Otherwise, take the last item and add 1 to it.
#         if len(my_list) == 0:
#             item_to_add = 1
#         else:
#             last_item = my_list[-1]
#             item_to_add = last_item + 1
#
#         my_list.append(item_to_add)
#
#     elif choice == 'r':
#         # Logic: remove the last item
#         # The instructions say we can assume we won't try to remove from an empty list
#         my_list.pop()
#
#     elif choice == 'x':
#         # Logic: print bye and break the loop
#         print("Bye!")
#         break