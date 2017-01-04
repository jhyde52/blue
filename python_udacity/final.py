#The files to submit are
#1-the problem definition document
#2-the solution design document
#3-all program files
#4-instructions on how to run your project.

#1
#I have two dictionaries in two different files. The first dictionary (RPC) has more synonyms listed 
#than the second dictionary (CatClassiifer). I need to create a list off all the categories and 
#variations that are missing from the second dictionary.


#2 
#A)
#The first dictionary (dictionary1.tsv) is a CSV (tab delimited) file with five columns. 
#The third column is a single string that is the category name I want to define. 
#This may be one to four words long. 
#The fifth column is a list of strings that are synonyms or variations for the item. 
#I need to create a one-to-one pairing of all the categories with all the variations.
#So I need to initialize the variables and write a counter that will "loop" through the values
#What needs to happen in each loop is to put the category name in the first variable,
#and take the second column's data and if it contains commas, create a new entry in the list
#which has the same category and one of the comma split values
#B)
#I have another file (dictionary2.tsv) that has all the categories in the first column and all the 
#comma separated variations in the second column.
#I need to create a one-to-one pairing of all the categories with all the variations.
#C)
#I need to do a comparison of the two lists. I need to create a list of all the 
#key-value pairs in list one that do not occur in list two.


import csv

with open('dictionary1.tsv', 'rb') as dictionary1:
	reader = csv.reader(dictionary1, delimiter='\t')
	for row in reader:
		print row

