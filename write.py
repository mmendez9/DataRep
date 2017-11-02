import csv
import os

os.chdir('C:\Users\student\PycharmProjects\CSV_Files')

# Read the file
inFile = open('SalesReport2014.csv', 'r')
inRead = csv.reader(inFile)
inRead = list(inRead)

# Write the file
outFile = open('allD.csv', 'w')
outWriter = csv.writer(outFile)

for row in inRead:
    outWriter.writerow(row)

inFile.close()
outFile.close()
