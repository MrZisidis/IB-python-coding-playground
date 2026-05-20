# if True:
#     student_info = input("Student information: ")
#     exercise_data = input("Exercises completed: ")
# else:
#     # now this is the False branch, and is never executed
#     student_info = "students1.csv"
#     exercise_data = "exercises1.csv"

# import csv
#
# with open("students.csv") as f:
#     reader = csv.reader(f, delimiter=";")

students = []
exercises = []

if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students.csv"
    exercise_data = "exercises.csv"

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


with open("students_stats.txt", "w") as my_file:
    # code to write something to the file
    for id in students:
        total_exercises = 0
        # if id[0] == exercises[0][0]:
        #     print(id[1] + " " + id[2])
        #     for item in range (1, len(exercises[0])):
        #         total_exercises = total_exercises + int(exercises[0][item])
        #     print("the number of exercises completed: ", total_exercises)
        for x in range(0, len(students)):
            if id[0] == exercises[x][0]:
                print(id[1] + " " + id[2])
                my_file.write(id[1] + " " + id[2] + " " )
                for item in range(1, len(exercises[x])):
                    total_exercises = total_exercises + int(exercises[x][item])
                print("the number of exercises completed: ", total_exercises)
                my_file.write(str(total_exercises) + "\n")

