# if True:
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # now this is the False branch, and is never executed
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"

students = []
exercises = []

if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students.txt"
    exercise_data = "exercises.txt"

with open(student_info) as student_file:
    for line in student_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        # print(parts[0] + " " + parts[1] + " " + parts[2])
        students.append(parts)
    print(students)

with open(exercise_data) as exercise_file:
    for line in exercise_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        # print(parts[0] + " " + parts[1] + " " + parts[2])
        exercises.append(parts)
    print(exercises)

for id in students:
    total_exercises = 0
    # if id[0] == exercises[0][0]:
    #     print(id[1] + " " + id[2])
    #     for item in range (1, len(exercises[0])):
    #         total_exercises = total_exercises + int(exercises[0][item])
    #     print("the number of exercises completed: ", total_exercises)
    for x in range (0, len(students) ):
        if id[0] == exercises[x][0]:
            print(id[1] + " " + id[2])
            for item in range (1, len(exercises[x])):
                total_exercises = total_exercises + int(exercises[x][item])
            print("the number of exercises completed: ", total_exercises)

with open("new_file.txt", "w") as my_file:
    # code to write something to the file
    my_file.write("Hello there!\n")