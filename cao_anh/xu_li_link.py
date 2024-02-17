import csv
with open('link.csv', mode ='r')as file1:
  csvFile = csv.reader(file1)
  for lines in csvFile:
        print(lines)