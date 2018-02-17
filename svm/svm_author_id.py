#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys

from sklearn import svm
from sklearn.metrics import accuracy_score

sys.path.append("../tools/")
from email_preprocess import preprocess
from timer import Timer


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
clf = svm.SVC(kernel='linear')
with Timer('training'):
    clf.fit(features_train, labels_train)

with Timer('predicting'):
    pred = clf.predict(features_test)

score = accuracy_score(labels_test, pred)
print score

#########################################################


