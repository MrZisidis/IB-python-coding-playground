# Please write a program which asks the user for words.
# If the user types in a word for the second time,
# the program should print out the number of different words typed in, and exit.

my_words=[]
wordCount = 0

while True:
    userWord = input("Word: ")

    if userWord in my_words:
        print("the number of different words: ", wordCount)
        break
    else:
        my_words.append(userWord)
        wordCount = wordCount +1