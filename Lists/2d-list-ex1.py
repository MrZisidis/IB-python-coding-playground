numbers=[[],[],[]]
for i in range(3):
    print(i)
    for j in range(3):
        print(j)
        usernumber= int(input("Enter a number: "))
        numbers[i].append(usernumber)
print(numbers)