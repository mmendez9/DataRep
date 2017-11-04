import csv

# Read the file
inFile = open('SalesReport2014.csv', 'r')
inRead = csv.reader(inFile)

# Write the file
outFile = open('allD.csv', 'w')
outWriter = csv.writer(outFile)

for row in inRead:
    outWriter.writerow(row)

inFile.close()
outFile.close()
