import csv

reader = csv.DictReader(open('questions.tsv'))
for row in reader:
	print row