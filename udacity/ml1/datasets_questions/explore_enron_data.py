#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


# print len(enron_data) # 146 keys
# print len(enron_data['GLISAN JR BEN F']) # 21 features

# number of persons of interest in the dataset: 18 (but 35 total so we are missing data)
'''
count = 0
for person_name in enron_data:
	if enron_data[person_name]["poi"]==1:
		count += 1
print count


print enron_data['PRENTICE JAMES']['total_stock_value']


counter = 0
for email in enron_data['WESLEY COLWELL']:
    if enron_data[from_this_person_to_poi]:
        counter += 1
print counter

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

#ceo
print enron_data['SKILLING JEFFREY K']['total_payments']
#founder, chairman
print enron_data['LAY KENNETH L']['total_payments']
#CFO
print enron_data['FASTOW ANDREW S']['total_payments']

# print enron_data

counting = 0
for person_name in enron_data:
        if enron_data[person_name]["total_payments"] == 'NaN':
            counting +=1
x= counting
print x


countin = 0
for person_name in enron_data:
    if enron_data[person_name]:
        countin +=1
y= countin

print float(x)/y


counting = 0
for person_name in enron_data:
    if enron_data[person_name]['poi']==True:
        if enron_data[person_name]["total_payments"] == 'NaN':
            counting +=1
x= counting
print x

countin = 0
for person_name in enron_data:
    if enron_data[person_name]:
        countin +=1
y= countin

print float(x)/y

'''


counting = 0
for person_name in enron_data:
    if enron_data[person_name]['poi']==True:
        counting +=1
print counting

