score = 0

def add_points(p):
    score = score + p

add_points(5)
print(score)

# Solution A
# score = 0
#
# def add_points(p):
#     global score
#     score = score + p
#
# add_points(5)
# print(score)



# Solution B
# score = 0
#
# def add_points(score, p):
#     return score + p
#
# score = add_points(score, 5)
# print(score)