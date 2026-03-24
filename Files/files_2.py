# text = "monkey,banana;harpsichord;sdfs;3434;045040r"
# words = text.split(";")
# print(type(words))
# for word in words:
#     print(word)
# print(words)

data = []
with open("splitting_example.txt") as f:
    #new_text = f.read()
    for line in f:
        # print(line)
        words = line.split()
        # print(words)
        data.append(words)
    print(data)

print(data[1][3])
print(data[2][3])
print(data[3][3])
print(data[4][3])
sum = 0
for i in range(1,5):
    sum = sum + int(data[i][3])
average = sum / 4
print(average)