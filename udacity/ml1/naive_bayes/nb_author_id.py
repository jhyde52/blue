#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
##



#########################################################

def nb_author_id():
### create classifier
    clf = GaussianNB() # what type of classifier

### fit the classifier on the training features and labels
    t0 = time() # start a timer
    clf.fit(features_train, labels_train) # train classifier
    print "training time:", round(time()-t0, 3), "s" # round time to 3 decimals
### use the trained classifier to predict labels for the test features
    t0 = time()
    pred = clf.predict(features_test) # use model to make predictions on test data

    ### calculate and return the accuracy on the test data
    accuracy = accuracy_score(labels_test, pred) # compare test labels with predictions
    print "prediction time:", round(time()-t0, 3), "s"    
    return accuracy

result = nb_author_id()
print result

#########################################################
'''
0.973265073948
training time: 4.828 s
prediction time: 0.326 s
'''
