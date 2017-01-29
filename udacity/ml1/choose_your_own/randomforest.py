#!/usr/bin/python

from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")

################################################################################


### name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

def rando_author_id():
	t0 = time()
	clf = RandomForestClassifier(n_estimators=50)
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

result = rando_author_id()
print result






try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass


# with n_estimators = 40 or 50, accuracy = .92
# with n_estimators = 35, accuracy = .92
# with n_estimators = 30, accuracy = .908
