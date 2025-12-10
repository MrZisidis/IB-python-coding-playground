import random

i = 10
# def add(no1, no2):
#     sum = no1 + no2
#     return sum

def odds(n):
    for i in range(n+1):  #i local variBLE
        if i % 2 == 1:
            print(i)

randomNumber = random.randint(0,100)

print(randomNumber)
odds(randomNumber)

print(n)
print(i)
print(x)

# value1 = int(input("Enter the first number: "))
# value2 = int(input("Enter the second number: "))
# print("the result is: ", add(value1, value2))
# newValue = 3
# newValue = newValue + add(value1, value2)
# print("The new value is: ", newValue)
