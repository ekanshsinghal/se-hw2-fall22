import csv

with open('../data/hw2-csv.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		print(row)
