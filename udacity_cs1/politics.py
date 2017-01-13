from bs4 import BeautifulSoup
import urllib2
import json
import os
import csv

r = urllib2.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r,'html.parser')
#print type(soup)

letters = soup.find_all("div", class_="ec_statements")
#print(letters)
#print type(letters)

#print letters[0]

#create a (nested) dictionary
#using the get_text method on the a tags to extract out the text we want
#the a tags are active link tags
#We'll go through all of the items in our letters collection, and for each one, 
#pull out the name and make it a key in our dict. The value will be another dict, 
#but we haven't yet found the contents for the other items yet so we'll just create assign an empty dict object.
lobbying = {}
prefix = "www.aflcio.org"
for element in letters:
	date = element.find(id="legalert_date").get_text()
	lobbying[element.a.get_text()] = {}
	lobbying[element.a.get_text()]["link"] = prefix + element.a["href"]
	lobbying[element.a.get_text()]["date"] = date

for item in lobbying.keys():
	print item + ": " + "\n\t" + "link: " + lobbying[item]["link"] + "\n\t" + "date: " + lobbying[item]["date"] + "\n\n" 


#this writes to a json file:
#with open("lobbying.json", "w") as writeJSON:
#	json.dump(lobbying, writeJSON)

#this writes to a csv file:
os.chdir("/Users/jessicahyde/Documents/python/practice/")

with open("lobbying.tsv", "w") as toWrite:
    writer = csv.writer(toWrite, delimiter="\t")
    writer.writerow(["name", "link", "date"])
    for a in lobbying.keys():
        writer.writerow([a.encode("utf-8"), lobbying[a]["link"], lobbying[a]["date"]])

