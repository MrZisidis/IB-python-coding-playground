# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
TABLE_WIDTH = 66            # Divider lines

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
headers = ["Name", "ID", "Q 1", "Q 2", "Q 3",
           "Q 4", "Yr Total"]
names = ["Adams", "Baker", "Collins", "Dalton", "East", "Ford",
         "Green", "Hill"]
empID = [434, 161, 427, 285, 460, 889, 275, 789]
salesQuarter1 = [942.45, 1566.99, 924.59, 197.71, 764.20,
                 279.43, 867.03, 880.43]
salesQuarter2 = [865.78, 337.10, 1597.64, 171.13, 552.89,
                 495.23, 637.09, 469.96]
salesQuarter3 = [973.25, 466.54, 288.54, 979.36, 2780.42,
                898.52, 522.45, 979.11]
salesQuarter4 = [535.84, 919.83, 661.63, 852.07, 315.02,
                120.78, 2748.53, 755.71]
salesTotalPerName = []

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# Calculate total sales for each employee and add it
#   to the salesTotalPerName array
for i in range(len(names)):
    total_per_name=  salesQuarter1[i] + salesQuarter2[i]+ salesQuarter3[i] + salesQuarter4[i]
    salesTotalPerName.append(total_per_name)
print(salesTotalPerName)
# Display the headers with a pipe symbol separating columns

# Display a divider for the width of the table

# Display a row to show data for each employee

# Display a divider for the width of the table

# Calculate total of all sales for all employees for the year

# Display a label and the total sales for the year

# Calculate mean of the total sales for the year

# Display a label and the mean of the total sales for the year