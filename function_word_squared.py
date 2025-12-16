# Please write a function named hash_square(length), which takes an integer argument.
# The function prints out a square of hash characters, and the argument specifies
# the length of the side of the square.
def hash_square(length):
    for i in range(length):
        print("#" * length)
    # return "#" * length
print(hash_square(3))
print(hash_square(4))


# Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes.
# The function takes an integer argument, which specifies the length of the side of the board.
# See the examples below for details:

def chessboard(length):
    for i in range(length):



# Please write a function named squared, which takes a string argument
# and an integer argument, and prints out a square of characters
# as specified by the examples below.

def squared(aWord, aNumber):
    print(aWord * aNumber)

squared("hello", 2)
squared("world", 3)