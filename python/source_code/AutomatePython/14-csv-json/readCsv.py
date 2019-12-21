import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print(row)

exampleFile.close()