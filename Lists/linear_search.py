my_list = [5, 20, 3, 15, 4]
second_list = my_list

print(second_list)

max_element = my_list[0]

for element in my_list:
    if max_element < element:
        max_element = element
print(max_element)