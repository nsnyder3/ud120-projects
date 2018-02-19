#!/usr/bin/python

import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]



### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
clf = neighbors.KNeighborsClassifier(weights='distance', algorithm='auto')
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print 'Accuracy {}'.format(accuracy_score(labels_test, pred))
try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
