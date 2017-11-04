import os
import csv

# Change directory
loc = input("Enter files' location: ".strip())
os.chdir(loc)
list = os.listdir(loc)

# Create the new cvs file
new = open("allData.csv", "w")
wNew = csv.writer(new)

# List the files in the directory
for i in list:
    print(i)


# Open the CSV file
for file in list:
    ofile = open(file, 'r')
    # Read each file
    rfile = csv.reader(ofile)
    # Write the all data
    for d in rfile:
        wNew.writerow(d)
    wNew.writerow('\n')


