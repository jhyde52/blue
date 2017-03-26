import sklearn

features, labels = GetMyData() # not defined
regression = Lasso()
regression.fit(features, labels)
regression.predict([[2,4]])
print regression.coef_