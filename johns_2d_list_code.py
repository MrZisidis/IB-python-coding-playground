list_2d = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
dig_left_to_right = []
dig_right_to_left = []
for i in range(len(list_2d)):
    dig_left_to_right.append(list_2d[i][i])
    dig_right_to_left.append(list_2d[i][len(list_2d[0]) - i - 1])
print(dig_left_to_right)
print(dig_right_to_left)


