#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def with_name(key, value):
    value['name'] = key
    return value

def find_total_outlier(data_collection):
    return sorted(filter(lambda x: x['salary'] != 'NaN', data_collection), key=lambda x: x['salary'], reverse=True)[0]

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_collection = [with_name(key, value) for key, value in data_dict.items()]

data_dict.pop(find_total_outlier(data_collection)['name'], 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )




matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


