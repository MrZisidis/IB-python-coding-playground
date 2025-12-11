# Please write a function named print_many_times(text, times),
# which takes a string and an integer as arguments.
# The integer argument specifies how many times the string argument should be printed out:

def print_many_times(text, times):
    for i in range(times):
        print(text)
    # print(text * times)

print_many_times("hi", 5)
user_text= input("Enter a string: ")
user_times = int(input("Enter a number of times: "))

print_many_times(user_text, user_times)