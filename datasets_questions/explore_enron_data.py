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

def with_feature(feature):
    return lambda x: x[feature] != 'NaN'

def without_feature(feature):
    return lambda x: x[feature] == 'NaN'


print 'How many people are in the dataset?'
print len(enron_data.keys())
print 'For each person, how many features are available?'
print len(enron_data.values()[0])
print 'How many POIs are there in the E+F dataset?'
print len([True for person in enron_data.values() if person['poi']])

print 'What is the total value of the stock belonging to James Prentice?'
print enron_data['PRENTICE JAMES']['total_stock_value']


print 'How many email messages do we have from Wesley Colwell to persons of interest?'
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "What's the value of stock options exercised by Jeffrey K Skilling?"
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print """Of these three individuals (Lay, Skilling and Fastow),
who took home the most money (largest value of "total_payments" feature)?

How much money did that person get?"""
people = ['LAY KENNETH L', 'FASTOW ANDREW S', 'SKILLING JEFFREY K']
print ['{}: {}'.format(name, enron_data[name]["total_payments"]) for name in people]

print 'How many folks in this dataset have a quantified salary?'
print len(filter(with_feature('salary'), enron_data.values()))
print 'What about a known email address?'
print len(filter(with_feature('email_address'), enron_data.values()))

print "How many people in the E+F dataset (as it currently exists) have 'NaN' for their total payments?"
print len(filter(without_feature('total_payments'), enron_data.values()))

print 'What percentage of people in the dataset as a whole is this?'
print float(len(filter(without_feature('total_payments'), enron_data.values())))/len(enron_data.values())


print "How many POIs in the E+F dataset have 'NaN' for their total payments?"
pois = filter(lambda x: x['poi'], enron_data.values())
print len(filter(without_feature('total_payments'), pois))
print "What percentage of POI's as a whole is this?"
print len(filter(without_feature('total_payments'), pois))/len(pois)
