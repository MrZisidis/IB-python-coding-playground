names = {}  #dictionary
# words = {'hello':'γεια', 'goodbye':'γεια'}
# print(words)
# usrpwd= {'david':'pwd123','mary':'123456' }
with open("employees") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        names[parts[0]] = parts[1]  # names[080488-123X] = "Pekka Mikkola"
                                    # names [290274-044S] = 'Liisa Marttinen'

# print(names)
# print(names.keys())
# print(names.values())

salaries = {}

with open("salaries") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        salaries[parts[0]] = int(parts[1]) +int(parts[2])

print("incomes:")

for pic, name in names.items():
    if pic in salaries:
        salary = salaries[pic]
        print(f"{name:16} {salary} euros")
    else:
        print(f"{name:16} 0 euros")