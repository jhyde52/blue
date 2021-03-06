#!/usr/bin/python
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
# from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from time import time
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

n_neighbors = 2
### name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
def knn_author_id():
	t0 = time()
	# clf = NearestCentroid(metric='euclidean', shrink_threshold=None)
	clf = KNeighborsClassifier(n_neighbors=22)
	clf.fit(features_train, labels_train)
	pred = clf.predict(features_test)
	print "training time:", round(time()-t0, 3), "s"
	
	t0 = time()
	accuracy = accuracy_score(labels_test, pred)
	print "prediction time:", round(time()-t0, 3), "s"    
	return accuracy

result = knn_author_id()
print result




try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass


# got .908 with centroid
# got .944 with regular knn and n_neighbors=22 (more of less was worse)

