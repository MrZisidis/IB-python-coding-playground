def check_inventory(items, stock):
    for i in range(len(items)):
        if stock[i] < 5:
            print("Warning: " + items[i] + " is low.")
        else:
            print(items[i] + " is OK.")

products = ["pencils", "pens", "notebooks", "glue", "scissors" ]
numbers = [5 ,2 ,3 , 3 , 7]

check_inventory(products, numbers)