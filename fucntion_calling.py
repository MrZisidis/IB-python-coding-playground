# total = 10
# def add_bonus(amount):
#     bonus = 5
#     total = amount + bonus
#     return total
#
# result1 = add_bonus(total)
# total = total + result1
# print(total)

# print(add_bonus("hello"))


count = 0
num = int(input("Enter a positive integer: "))
while num > 0:
    count += 1
    num = int(input("Enter a positive integer: "))
print(count)