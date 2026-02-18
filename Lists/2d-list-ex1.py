numbers=[[1,2,3],[4,5,6],[7,8,9]]
# total = 0
# for i in range(3):
#     for j in range(3):
#         userNumber= int(input("Enter a number: "))
#         total = total + userNumber
#         numbers[i].append(userNumber)
# print(numbers)
# print("total is: ", total)
# print("average is: ", round(total/9,2))
for row in numbers:
    print(row)

#ex.2   - Sum of all elements per column,
#         Average of all elements per row
for row in range(3):
    average_per_row = 0
    sum_per_row = 0
    for column in range(3):
        sum_per_row = sum_per_row + numbers[row][column]
    average_per_row = sum_per_row / 3
    print("The Average for row ", row , " is ", average_per_row)

for j in range(3):
    sum_per_column = 0
    for i in range(3):
        sum_per_column =  sum_per_column + numbers[i][j]
    print("The Sum for column ", j, " is ", sum_per_column)