import os
import csv

loc = input("Enter a directory (path):".strip())
os.chdir(loc)

file = input("Enter a file's name:".strip())
filecsv = open(file + '.csv', 'r')
rfile = csv.reader(filecsv)
rfile = list(rfile)

print(rfile)

filecsv.close()