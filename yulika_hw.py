#Question 3
# student = "Bob"
# def changeOfName(st):
#    st = "Jim"
#    print("Student inside the method:", st)
#    return st
# student = changeOfName(student)
# print("Student outside the method:", student)


#Question 3
student = "Bob"
print("Student's name is: ", student)

def changeOfName(newName):
   global student
   student = newName
   return student

changeOfName("Stuart")
print("Student's new name is: ", student)

# print("Student outside the method:", )