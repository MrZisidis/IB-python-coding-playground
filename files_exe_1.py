# by David Z
file = open("random_numbers.txt")

def largest():
    biggest = -9999999 #
    for line in file:
        if biggest < int(line):
            biggest = int(line)
        else :
            continue
    return biggest

print(largest())