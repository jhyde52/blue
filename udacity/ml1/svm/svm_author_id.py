#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# optionally shrink size of training data
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 


#########################################################
def svm_author_id():
	# add params for C and gamma to make decision boundary less smooth, more correct points
	clf = svm.SVC(kernel = "rbf", C=10000) # linear, poly, rbf, sigmoid, precomputed, a callable, custom
	t0 = time() # start a timer

	clf.fit(features_train, labels_train) # train classifier
	print "training time:", round(time()-t0, 3), "s" # round time to 3 decimals
	
	t0 = time()
	pred = clf.predict(features_test)
	# show predictions for examples 0 is Sara, 1 is Chris
	print pred[10]
	print pred[26]
	print pred[50]

	# show number predicted for each class
	import collections
	counter = collections.Counter(pred)
	print counter[1], counter[0]
	# 1 Chris = 877 and 0 Sara = 881

	accuracy = accuracy_score(labels_test, pred) # compare test labels with predictions
	print "prediction time:", round(time()-t0, 3), "s"   
	return accuracy

result = svm_author_id()
print result 

#########################################################


'''
with linear and no other params
# 236 seconds
# 24 seconds
# 0.984 

with only 1 percent of the features, 88 percent accurate

with rbf, C's best value for accuracy (with partial training set) 
10 = 61 percent
1000 = 82 percent
10000 = 89 percent
100,000 = 86 percent

for full training set, .9908
for full training set and C=100,000 I got .9943 and faster
'''


