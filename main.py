import os
import csv

# Change directory
loc = input("Enter a directory: ".strip())
os.chdir(loc)
list = os.listdir(loc)

# Create the new cvs file
new = open("allData.csv", "w")
wNew = csv.writer(new)

# List the files in the directory
for i in list:
    print(i)


# Open the CSV file
# file = input("Enter a file's name".strip())
# ofile = open(file, 'r')

