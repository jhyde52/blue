#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
def dt_author_id():
	t0 = time()
	clf = tree.DecisionTreeClassifier(min_samples_split=40)
	clf.fit(features_train, labels_train)
	pred = clf.predict(features_test)
	print "training time:", round(time()-t0, 3), "s"
	# show how many features are in the data
	# this is the number of columns in the training data
	# which is in a numpy array
	print len(features_train[0])

	t0 = time()
	accuracy = accuracy_score(labels_test, pred)
	print "prediction time:", round(time()-t0, 3), "s"    
	return accuracy

result = dt_author_id()
print result



#########################################################
# default all
# accuracy .989
# train time 128
# test time .01
# but in lecture min sample split 50 had 91.2% accuracy vs sample 2 has 90.8%



# easy to understand graphically
# prone to overfitting esp with many features
# be careful with parameters
# can build huge classifiers with them using ensemble methods





