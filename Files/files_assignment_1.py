file = open("random_numbers.txt")

def largest():
    biggest = 0
    for line in file:
        if biggest < int(line):
            biggest = int(line)
        else:
            continue
    return biggest

def smallest():
    small = 999999
    for line in file:
        if small > int(line):
            small = int(line)
        else :
            continue
    return small

def average():
    sum = 0
    count = 0
    for line in file:
        sum = int(line)+sum
        count = count + 1
    ave = sum/count
    return ave

def count_even():
    count = 0
    for line in file:
        if int(line)%2 == 0:
            count = count + 1
        else :
            continue
    return count


# print(average())
print("the largest is: ", largest())
print("the smallest is: ", smallest())
print(count_even())