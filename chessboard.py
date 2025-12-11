def chessboard(number):
    for row in range(number):
        row_text = ""
        # print("row is: ", row)
        for col in range(number):
            # print("row is: ", row)
            # print("col is: ", col)
            # input()
            if (row + col) % 2 == 0:
                row_text = row_text + "1"
            else:
                row_text = row_text + "0"
        print(row_text)

chessboard(3)